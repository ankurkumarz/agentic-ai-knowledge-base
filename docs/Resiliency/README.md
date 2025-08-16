

## Retry / Failover Solutions

- [Restate](https://restate.dev/): Developed in Rust, it has a Core Runtime to handle Durable Execution, Retries & Fault Tolerance, Timers & Scheduling, and more. It sits in front of  services like a reverse-proxy / message broker and handles all the communication with backend services. Restate implements its own distributed log + processors (no external DB/log required for durability). It uses Object storage (e.g., AWS S3, GCS, Azure Blob, MinIO, etc.) for durable async snapshots of the log and state.[Click here](https://github.com/restatedev/ai-examples) for AI examples. For LLM apps, it is useful for parallel processing, async execution, retry calls to underlying LLMs, workflow-based execution, and more.


## Caching
