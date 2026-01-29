# 12-Factor Agents

## Overview

The [12-Factor Agent](https://github.com/humanlayer/12-factor-agents) methodology provides a set of best practices for building scalable, maintainable, and portable agentic AI applications. Inspired by the 12-Factor App methodology, these principles ensure agents can be deployed consistently across different environments.

## The Twelve Factors

### I. Codebase
**One codebase tracked in revision control, many deploys**

- Maintain agent code in version control (Git)
- Use branching strategies for different environments
- Deploy the same codebase to development, staging, and production
- Avoid environment-specific code branches

```yaml
# Example: Agent configuration structure
agent/
├── src/           # Core agent logic
├── config/        # Environment configurations
├── tests/         # Test suites
└── deploy/        # Deployment scripts
```

### II. Dependencies
**Explicitly declare and isolate dependencies**

- Use dependency management tools (pip, npm, poetry)
- Pin specific versions of LLM APIs and frameworks
- Isolate dependencies using virtual environments or containers
- Never rely on system-wide packages

```python
# requirements.txt
langchain==0.1.0
openai==1.3.0
pinecone-client==2.2.4
```

### III. Config
**Store config in the environment**

- Separate configuration from code
- Use environment variables for API keys and endpoints
- Never commit secrets to version control
- Support different configurations per environment

```python
import os

class AgentConfig:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-4')
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))
```

### IV. Backing Services
**Treat backing services as attached resources**

- Connect to databases, APIs, and services via URLs
- Make no distinction between local and third-party services
- Use service discovery and configuration management
- Enable easy swapping of service implementations

```python
# Service abstraction
class VectorStore:
    def __init__(self, connection_string):
        self.client = self._create_client(connection_string)
    
    def _create_client(self, url):
        if url.startswith('pinecone://'):
            return PineconeClient(url)
        elif url.startswith('weaviate://'):
            return WeaviateClient(url)
```

### V. Build, Release, Run
**Strictly separate build and run stages**

- **Build**: Convert code into executable bundle
- **Release**: Combine build with configuration
- **Run**: Execute the agent in the runtime environment
- Use immutable releases with unique identifiers

```bash
# Build stage
docker build -t agent:v1.2.3 .

# Release stage
docker tag agent:v1.2.3 registry/agent:v1.2.3
docker push registry/agent:v1.2.3

# Run stage
docker run -e OPENAI_API_KEY=$API_KEY registry/agent:v1.2.3
```

### VI. Processes
**Execute the agent as one or more stateless processes**

- Design agents to be stateless
- Store persistent data in backing services
- Use shared-nothing architecture
- Enable horizontal scaling through process replication

```python
class StatelessAgent:
    def __init__(self, config):
        self.llm = LLM(config.model_name)
        self.memory = ExternalMemory(config.memory_url)
    
    def process_request(self, request):
        # No local state - all data from request or external services
        context = self.memory.get_context(request.session_id)
        response = self.llm.generate(request.prompt, context)
        self.memory.store_interaction(request.session_id, request, response)
        return response
```

### VII. Port Binding
**Export services via port binding**

- Agents should be self-contained and expose services via ports
- Use web frameworks to expose HTTP APIs
- Enable service-to-service communication
- Support load balancing and service discovery

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
agent = Agent()

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = agent.process(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
```

### VIII. Concurrency
**Scale out via the process model**

- Scale by running multiple agent processes
- Use process managers for different workload types
- Implement proper resource isolation
- Design for horizontal scaling

```yaml
# Process types
web: gunicorn app:app --workers 4
worker: celery worker -A agent.tasks
scheduler: celery beat -A agent.tasks
```

### IX. Disposability
**Maximize robustness with fast startup and graceful shutdown**

- Minimize startup time for quick scaling
- Handle SIGTERM gracefully for clean shutdown
- Design for crash-only software principles
- Implement proper cleanup procedures

```python
import signal
import sys

class Agent:
    def __init__(self):
        self.running = True
        signal.signal(signal.SIGTERM, self._shutdown_handler)
    
    def _shutdown_handler(self, signum, frame):
        print("Received shutdown signal, cleaning up...")
        self.running = False
        self._cleanup()
        sys.exit(0)
    
    def _cleanup(self):
        # Close connections, save state, etc.
        pass
```

### X. Dev/Prod Parity
**Keep development, staging, and production as similar as possible**

- Minimize gaps between environments
- Use the same backing services across environments
- Deploy frequently to reduce deployment risk
- Use containerization for consistency

```dockerfile
# Dockerfile for consistent environments
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "agent.py"]
```

### XI. Logs
**Treat logs as event streams**

- Write logs to stdout/stderr
- Use structured logging (JSON format)
- Aggregate logs using external systems
- Include correlation IDs for tracing

```python
import logging
import json

class StructuredLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setFormatter(self._json_formatter)
        self.logger.addHandler(handler)
    
    def _json_formatter(self, record):
        log_entry = {
            'timestamp': record.created,
            'level': record.levelname,
            'message': record.getMessage(),
            'agent_id': getattr(record, 'agent_id', None),
            'session_id': getattr(record, 'session_id', None)
        }
        return json.dumps(log_entry)
```

### XII. Admin Processes
**Run admin/management tasks as one-off processes**

- Use the same codebase for admin tasks
- Run administrative tasks in identical environments
- Implement proper tooling for common operations
- Automate routine maintenance tasks

```python
# Management commands
class AgentManager:
    def migrate_memory(self):
        """Migrate agent memory to new format"""
        pass
    
    def cleanup_old_sessions(self):
        """Remove expired session data"""
        pass
    
    def health_check(self):
        """Verify agent system health"""
        pass
```

## Implementation Guidelines

### Development Workflow
1. **Local Development**: Use docker-compose for local services
2. **Testing**: Implement comprehensive test suites
3. **CI/CD**: Automate build, test, and deployment pipelines
4. **Monitoring**: Implement health checks and metrics collection

### Deployment Patterns
- **Container Orchestration**: Use Kubernetes or Docker Swarm
- **Service Mesh**: Implement service-to-service communication
- **Auto-scaling**: Configure based on metrics and load
- **Blue-Green Deployment**: Enable zero-downtime deployments

### Monitoring and Observability
- **Metrics**: Track agent performance and usage
- **Tracing**: Implement distributed tracing
- **Alerting**: Set up proactive monitoring
- **Dashboards**: Create operational visibility

## Benefits

### Scalability
- Horizontal scaling through stateless processes
- Independent scaling of different components
- Efficient resource utilization

### Maintainability
- Clear separation of concerns
- Consistent deployment practices
- Simplified debugging and troubleshooting

### Portability
- Environment-agnostic design
- Consistent behavior across platforms
- Easy migration between cloud providers

## See Also
- [Architecture Components Selection](components-selection.md)
- [Multi-Agent Systems](multi-agent-system.md)
- [Agent Observability](../Observability/Readme.md)
- [Best Practices](../BestPractices/README.md)