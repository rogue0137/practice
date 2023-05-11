
# Web Crawler

Web crawlers are useful for accomplishing the following tasks.
1. How search engines get their data (ex. Google, Baidu)
2. Test web page links
3. Monitor content or structure updates on a page
4. Mirroring 
    - mirroring: making a copy of a website
5. Copyright infrigement checks

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

_what the system does_

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

_how the system does it_

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

<style>
tr:nth-child(odd) {
  background-color: #b2b2b2;
  color: #f4f4f4;
}
</style>

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
### Bandwidth Estimation


## Diagram the System

![WebCrawlerBasicDiagram](https://docs.google.com/drawings/d/e/2PACX-1vS6BAMa4y_QqfJCCoKDtA03qRuektVrvxu0cGKFF7C_NUmQ6SiAU8ySr75mqJrBX7UKJsnNiR6epwzl/pub?w=960&h=720)
## Define Data Models
## Define APIs
## Deep Dive on Diagram Section
## Faults and Failures

- Load balancing
- Throttling
