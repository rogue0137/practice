
# Web Crawler

**Uses**

Web crawlers are useful for accomplishing the following tasks.
- How search engines get their data (ex. Google, Baidu)
- Test web page links
- Monitor content or structure updates on a page
- Mirroring 
    - mirroring: making a copy of a website
- Copyright infrigement checks

This specific solution does not attempt to address both the crawler AND a use case above. It is only attempting to address the crawler design.

**Design Specifications Needed to Pass this Interview**
Here are the specific sections you will need to address in a web crawler system design interview.
1. [Ask questions](#ask-questions)
2. [Functional Requirements](#functional-requirements)
3. [Non-functional Requirements](#non-functional-requirements)
4. [Estimation](#estimation)
5. [Diagram the System](#diagram-the-system)
6. [Define Data Models](#define-data-models)
7. [Define APIs](#define-apis)
8. [Deep Dive on Diagram Section](#deep-dive-on-diagram-section)
9. [Faults and Failures](#faults-and-failures)

## Ask questions

You are asking questions to clarify the requirements and constraings of the system you are building.

- **Goal**:
    - Do I want to index all web pages?
    - Do I want to index all pages within a specific domain?
    - Do I want to index specific pages within a specific domain?
    - Do I want to index specific pages across domains?
- **Scale**
    - How many web pages will be crawled?
    - How often should these pages be crawled?
    - (Do different pages have different crawl rates?)
- **Content**
    - What is the distribution of content types?
        - text
        - images
        - videos
        - etc.
    - Does it need to handle one type, multiple types or all types?
    - Duplicates
        - Do duplicates need to be removed?
        - What constitutes a duplicate in our system?
- **Politeness**
    - Do we want a "polite" web crawler?
        - polite = a web crawler that crawls a specified domain at specific intervals so as not to overwhelm that domain


## Functional Requirements

_What the system does..._

These requirements determine the function an application (or part of an application) should perform.

Some types of functional requirements
- Business requirements
- User requirements
- System requirements

Sometimes it is easiest to think of these requirements as, "if user supplies INPUT, what is the expected OUTPUT". 

Examples of potential functional requirements for a web crawler
- Must take input URLs and crawl from there
- URL content must be extractable
- URL content must be storable via BLOb (Binary Large Object) store
- Must be schedule-able/Data must be regularly updated

## Non-functional Requirements

_How the system does it..._

These requirements determine performance and quality standards.

Some examples of non-functional requireents are:
- availability
    - _reminder_: According to CAP theory, if you pick availability, you can not have consistency
- capacity
- consistency
    - _reminder_: According to CAP theory, if you pick consistency, you can not have availability
- extensibility
    - Should not HTTP protocols be supported?
    - Should additional storage formats be supported?
- recoverability
- reliability
- scalability
- security
- supportability
    - Should you limit crawling?
        - Throttling?
            - Time spent cutoff
            - Visted # of URLs cutoff
- usability
    - Should there be a user interface for easier scheduling?

## Estimation

Normally you will have to perform up to four types of estimation for web crawlers.
1. [Resource estimation](#resource-estimation)
2. [Storage estimation](#storage-estimation)
3. [Traversal estimation](#traversal-estimation)
4. [Bandwidth estimation](#bandwidth-estimation) 


### Resource Estimation

Resource estimations help us compute all of the estimations that come after it. The following estimations are not chosen for any specific reason besides giving us a tool set to use to make estimations.

1. How many web pages does the system need to crawl? **3 billion**
2. How much content does each web page have? In KB? **2050 KB**
3. How much metadata does each web page have? Bytes? **500 bytes**


### Storage Estimation

Use google to do the calculations for you.


| |
| ---- |
| (Storage for Content + Storage Per Metadata) x Total Web Pages|
| (2050 KB + 500 bytes) x 3 Billion |
| (Total Individual Web Page Storage) x Total Web Pages |
| (2.0505 MB) x 3 Billion |
| 6.1515 PB |
| _Round to a cleaner number_ |
| ~6.2 PB |

### Traversal Estimation

Scenario 1 Assumptions:
- AVG https traversal per web page is 45 seconds
- We have 1 crawler
- 3 Billion Web Pages (from above)

||
| ---- |
| # of Web Pages x AVG HTTPs traversal per web page|
| 3 billion x 45 seconds => 0.135 billion seconds => 4.3 years|


Scenario 2 Assumptions
- AVG https traversal per web page is 45 seconds
- We have 5 crawlers
- 3 Billion Web Pages (from above)

_Divide above numbers by 5._
4.3 years/ 5 crawlers = .9 years

Scenario 3 Assumptions:
- AVG https traversal per web page is 45 seconds
- We have to crawl all webpages in one day
- 3 Billion Web Pages (from above)

_We need to look at how many days are in a 4.3 years._
4.3 years ~= 1571 days

If we had one crawler per server, we would need 1571 servers.
However, if our servers were multi-threaded and each server had 10 threads, 1571/10 = ~157 servers.



### Bandwidth Estimation

Above we figured out we want to process ~6.2 PB of data per day.
- 1 day = 86400 seconds
- 6.2 PB/ 86400 ~= 72 GB per second
- Need to converst to Gb because bandwidth is measured in bits not bytes => 72 GB ~= 576 Gb per second
- If we have 157 servers, we need to distribute the above bandwidth to find it by server => 576 Gb per second/ 157 servers ~= 459 MB per server per second 


## Diagram the System

Very Basic System
![WebCrawler1](https://docs.google.com/drawings/d/e/2PACX-1vS6BAMa4y_QqfJCCoKDtA03qRuektVrvxu0cGKFF7C_NUmQ6SiAU8ySr75mqJrBX7UKJsnNiR6epwzl/pub?w=960&h=720)

Slightly More Advanced System
![WebCrawler2](https://docs.google.com/drawings/d/e/2PACX-1vRZT8NuVXd3Hv39XusnzV2sUaB3qZagwDRvdqRLQ6hGJk6yUrD7y5ESqjlYfENQLakEoQ4n-_Nh0-2u/pub?w=960&h=720)

Slightly More Advanced Focusing on Prioritization and Politeness
![WebCrawler3](https://docs.google.com/drawings/d/e/2PACX-1vSTQPKmdDurg3vbYPH1hJLSFhZfy5T7Krp0dGIdZDdsebj2x1-7TSuIOhWJ9fX-bfv1k55wlw2RmVWk/pub?w=960&h=720)


## Define Data Models

| Metadata Table |
|---|--|
| id  | |
| url | |

## Define APIs
## Deep Dive on Diagram Section

Zooming in on Prioritization and Politeness
![PrioritizationAndPolitenessService](https://docs.google.com/drawings/d/e/2PACX-1vSeZRceEkpbp2jmtzLKqJlZStwcqJHHBXP4shMNfAbIfea8zK-Yv0KtiQ2ZByS7wEQgMGItWsTc3Q4C/pub?w=960&h=720)

Polite Feeder Service makes use of a crawl capacity limit and robots.txt files for websites.
## Faults and Failures

General Ways to Address Faults and Failures
- Load balancing
- Throttling
- Log failures and set alerts
- Continually tes and monitor performance

Solve Duplicates
_when uniqueness is listed as a requirement_
- hash value for each page (has limitations)
- simhash (has limitations)
 - simhash: an algorithm to estimate how similar to sets are
- crawl delays



## Extras

Breadth-first versus Depth-first Crawlers:

| | Pros | Cons|
|--|--|--|
| **Breadth-first**| <ul><li>comprehensive coverage of a specific domain</li><li>easily parallelizable</li></ul> |<ul><li>increased complexity through managing a queue of URLs</li><li>slower performance</li></ul>|
| **Depth-first**| <ul><li>in depth coverage of a specific domain</li><li>faster</li></ul>| <ul><li>can miss important information that is further away from the starting URL</li><li>difficulty prioritizing pages</li> 
