# Key Terms

Interview Checklist
- [ ] Functional Requirements
    - ask "Who is the user?"
- [ ] Non-functional Requirements
- [ ] Estimates
- [ ] Diagram the System 
    - Dig you go through the whole flow?
    - Did you talk about tradeoffs out loud?
- [ ] Define Data Models
    - Are you thinking of the entire lifecycle of the model?
- [ ] Define APIs
- [ ] Deep Dive on Diagram Section
    - What happens if a component goes down?
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

Wordsmith the following:
Optimistic locking is a technique for concurrency control that allows multiple transactions to access the same data simultaneously without acquiring locks on those resources, assuming that conflicts are rare. [2]

When using optimistic locking, a version number or timestamp is assigned to each record. Before committing a transaction that modifies a record, the system checks whether the version number or timestamp has changed since the record was last read. If the check reveals conflicting modifications, the committing transaction rolls back and can be restarted. [2]

Optimistic locking is most applicable to high-volume systems and three-tier architectures where you do not necessarily maintain a connection to the database for your session. This is because the client cannot actually maintain database locks as the connections are taken from a pool and you may not be using the same connection from one access to the next. [0]

Optimistic locking works even across multiple database transactions since it doesn’t rely on locking physical records. [3]

To implement optimistic locking with version number, each item has an attribute that acts as a version number. If you retrieve an item from a table, the application records the version number of that item. You can update the item, but only if the version number on the server side has not changed. If there is a version mismatch, it means that someone else has modified the item before you did. The update attempt fails, because you have a stale version of the item. If this happens, you simply try again by retrieving the item and then trying to update it. [4]

Wordsmith the following:

Materialization is also a term used in the context of databases. In a relational database, for example, materialization refers to the process of creating a materialized view, which is a database object that contains the results of a query. Materialized views are particularly useful for speeding up queries that run frequently or for generating reports.

The process of materializing a view involves creating a table and populating it with data from the original query. When a query is run against the materialized view, the results are retrieved from the table rather than being computed again. This can significantly speed up query performance, especially for complex queries that involve multiple tables or aggregations.

Materialization can be used to speed up queries and generate reports. Materialized views can be created in most relational database management systems, and they can be refreshed periodically to keep the data fresh. Materialized views can also be used to replicate data across different databases or to provide a consistent view of data that is spread across multiple tables.
