# System Design Cheetsheet


## To Do
    1. Clarify functional requirements
    2. Clarify non-functional requirements
        - Availability reqs
        - Consitency reqs
        - Latency reqs
        - Confirm: Are any more important than the other?
    3. Clarify load estimates and volume of entities
        - how many page views do we get?
        - how many requests per second?

## Timing

_Note: Have a timer visible to make sure you don't spend too much time on one section_

60 min breakdown
- 5 min: Reqs
- 3 min: Security (ex. payments, identity, etc.)
- 10 min: High level overview
- 10 min: Fine tune/iterate on solution
- 5 min: metrics: measuring things like avaiability, latency, page views, RPS, etc.

## Other
- SQL vs. NoSQL: You usually do not have to pick one, but if you do, make sure you have a strong justification for why.

## Design Fundamentals

Design Fundamental
- 


System Design Fundamentals
1. Underlying/Foundational Knowledge, ex. client-server relationship
2. Key Characteristics, ex. latency, availbility, redudancy, consistency, throughput 
3. Components of a system, ex. load balancers, proxies, caches, rate-limiting, leader-election
4. Real existing products and services that you can use as actual components or achieve your system, ex. Zookeeper, Redis, GCP, AWS

### Storage

- disk: ex. writing to a file, data will persist
- memory: ex. if your server goes down and gets booted back up, it won't have it when you want it go up; reading/writing from memory is much faster

- latency: the time it takes for a certain operation to complete in a system, usually measured in milliseconds or seconds
- throughput: number of operations a system can handle properly per unit per time

availability
- how resistant is your sytem to failures (how fault tolerance is your system)
- % of uptime in a year, usually very, very high percentages

- SLA/SLO
- Nines: percentages with the number nines; 99.9% 3 nines, 99.99% 4 nines, 5 nines + are "highly available systems" <-- REAL TERM
- Redundancy: eliminate single points of failure; duplicate/triple specific parts of your system


### CACHE

Can cache at all levels, ex. client, server, intermediate, etc.
- use when making a ton of network requests; if you cache the network request, it will speed up the system
- use when getting the same DB request again and again and again; store the result in mem at each server so it doesn't have to go directly into the DB drive every time
TODO List of key terms

write-to cache: in the same operation, writes it to the DB and the cache; cache and DB always in sync; downside: you always have to go to the DB
write-back cache: only updates the cache with the write, then every X minutes it will send the info in the cache to udpate the DB

caches can become stale if they don't get updated often enough
viewcount is an OK stale cache; the data for that does not need to be 100% correct at all time; however, comments should always show most updated (what if someone responded to a comment that is not changed forit, but once the stale cache got updated, it's different! unacceptable)