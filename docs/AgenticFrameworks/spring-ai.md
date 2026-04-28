# Spring AI

## Overview

[Spring AI](https://spring.io/projects/spring-ai) is inspired by LangChain and leverages the Spring ecosystem to build GenAI applications in the Java ecosystem. It provides seamless integration with the broader Spring ecosystem to leverage libraries available for data connectivity, asynchronous processing, system integration, and more.

## High-level Architecture

![Spring AI for Building Agentic Systems](../assets/images/frameworks-spring-ai-architecture.jpeg)

*Source: [Spring AI for Building Agentic Systems](https://spring.io/blog/2025/01/21/spring-ai-agentic-patterns)*

## Key Features

- **Multiple LLM support**: Works with a wide range of language model providers
- **Observability features**: Built-in observability within the Spring ecosystem
- **Model evaluation**: Tools for evaluating model outputs and performance
- **[Advisors API](https://docs.spring.io/spring-ai/reference/api/advisors.html)**: Encapsulates recurring Generative AI patterns for reuse
- **Chat conversations**: Native support for conversational AI patterns
- **RAG support**: Retrieval-Augmented Generation capabilities built in
- **Spring ecosystem integration**: Seamless integration with Spring Boot, Spring Data, Spring Integration, and more

## Suitable for (Pros)

- **Enterprise GenAI applications leveraging the Spring ecosystem**: Alleviates the need for learning additional frameworks or languages
- **Seamless integration** with the broader Spring ecosystem to leverage libraries available for data connectivity, asynchronous processing, system integration, and more
- **Java-first teams**: Natural fit for organizations already standardized on Java and Spring

## Where other frameworks flare better (Cons)

- **Spring AI is relatively novel and still in the early stages**: It needs to be compared with features required in a complex business scenario to consider alternative frameworks
- **Limited complex scenario testing**: Not yet widely proven in highly complex enterprise agentic deployments
- **Java-only**: Less suitable for teams working in Python or other languages

## Resources

- **Official Documentation**: [Spring AI](https://spring.io/projects/spring-ai)
- **Observability Docs**: [Spring AI Observability](https://docs.spring.io/spring-ai/reference/observability/index.html)
- **Advisors API**: [Spring AI Advisors](https://docs.spring.io/spring-ai/reference/api/advisors.html)
- **Blog**: [Spring AI Agentic Patterns](https://spring.io/blog/2025/01/21/spring-ai-agentic-patterns)

## See Also
- [Agent Development Frameworks](README.md)
- [Multi-Agent Systems](../Architecture/multi-agent-system.md)
- [LangChain](langchain.md)
