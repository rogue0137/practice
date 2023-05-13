# Key Terms

Interview Checklist
- [ ] Functional Requirements
- [ ] Non-functional Requirements
- [ ] Estimates
- [ ] Diagram the System
- [ ] Define Data Models
- [ ] Define APIs
- [ ] Deep Dive on Diagram Section
- [ ] Faults, Failures, and Followups

Core system designs concepts
- gRPC vs. REST vs. GraphQL
- Synchronous vs. Async
- DB Type
    - SQL - why?
    - NoSQL - timestamp? document? graph?
    - Sharding & Federation 
- Retries
- Microservice architecturee
- Distributed everything
    - messaging system
        - queues, topics, subscribers, publishers
        - Kafka Streams vs. SNS
    - caching
        - CDN (if images)   
- Elasticsearch

Tradoffs
Benchmark/Load test
Followups

However, Kafka Streams is optimized for high-throughput, low-latency data processing, while AWS SNS is optimized for reliable message delivery and decoupling of message publishers from subscribers
