FINAL HEDEF
Senin geliştireceğin sistem:
Enterprise Agentic AI Platform
Şunları yapacak:


document ingestion


RAG


vector search


agent workflows


tool calling


REST APIs


Azure OpenAI integration


Databricks pipelines


Dockerized deployment


Azure DevOps CI/CD


monitoring/logging


Ve bunu:


gerçek repo structure


gerçek engineering practices


gerçek deployment mindset


ile yapacağız.

PROJE MİMARİSİ
Frontend (later maybe)        ↓FastAPI Backend        ↓Agent Layer (LangGraph)        ↓RAG Pipeline        ↓Azure OpenAI        ↓Vector Store / Databricks        ↓Document Pipeline

30 GÜNLÜK PLAN
Bu plan:


yoğun ama gerçekçi


tutorial değil


tamamen production-oriented



WEEK 1 — SOFTWARE ENGINEERING FOUNDATION
Amaç:

“Enterprise backend sistemi nasıl organize edilir?”


DAY 1 — Environment + Repo Setup
Öğreneceklerin


professional repo structure


uv


virtual environments


pyproject.toml


linting


formatting


.env


configuration management


Git workflow


Yapacağımız


repo oluşturma


enterprise folder structure


uv setup


FastAPI installation


initial app setup


Gün Sonu
Şuna benzeyen structure:
app/api/services/core/models/tests/

DAY 2 — FastAPI Fundamentals
Öğreneceklerin


REST APIs


routes


request/response lifecycle


pydantic


schemas


validation


Yapacağımız


first API endpoints


health checks


structured responses


Gün Sonu
Gerçek backend endpointleri.

DAY 3 — Backend Architecture
Öğreneceklerin


service layer


separation of concerns


dependency injection


clean architecture


Yapacağımız


routers/services split


reusable logic


config management


Gün Sonu
Kod spaghetti olmayacak.

DAY 4 — Async + Production Backend
Öğreneceklerin


async/await


why async matters


concurrency basics


API performance mindset


Yapacağımız


async endpoints


async services



DAY 5 — Docker
Öğreneceklerin


container nedir


Dockerfile


images vs containers


ports


env vars


Yapacağımız


backend dockerization


Gün Sonu
App container içinde çalışacak.

DAY 6 — Docker Compose + Services
Öğreneceklerin


multi-service systems


networking


volumes


Yapacağımız


FastAPI + database compose setup



DAY 7 — Logging + Debugging
Öğreneceklerin


production logging


structured logs


debugging mindset


Yapacağımız


logging system


request tracing basics



WEEK 2 — CLOUD + AZURE + DEVOPS
Amaç:

“Cloud deployment nasıl çalışıyor?”


DAY 8 — Azure Fundamentals
Öğreneceklerin


Azure ecosystem


subscriptions


resource groups


Azure OpenAI


storage basics



DAY 9 — Azure OpenAI Integration
Yapacağımız


GPT integration


embeddings


inference APIs


Gün Sonu
Gerçek LLM backend.

DAY 10 — Azure DevOps Basics
Öğreneceklerin


repos


pipelines


artifacts


CI/CD basics


Yapacağımız


first pipeline



DAY 11 — CI/CD
Yapacağımız


automated testing


automated docker build


Gün Sonu
Code push → pipeline çalışacak.

DAY 12 — Azure Deployment
Öğreneceklerin


App Service


Container Apps


deployments


Yapacağımız


first cloud deployment


Gün Sonu
App Azure’da live olacak.

DAY 13 — Secrets + Configs
Öğreneceklerin


Key Vault


secret management


env separation



DAY 14 — Monitoring + Observability
Öğreneceklerin


logs


metrics


observability mindset


OpenTelemetry basics



WEEK 3 — AI ENGINEERING + RAG
Amaç:

“Gerçek AI platform”


DAY 15 — Embeddings + Vector Search
Öğreneceklerin


embeddings


semantic search


chunking



DAY 16 — RAG Pipeline
Yapacağımız


retrieval pipeline


chunk storage


retrieval flow



DAY 17 — Databricks Basics
Öğreneceklerin


notebooks


clusters


Delta Lake


jobs



DAY 18 — Databricks Pipelines
Yapacağımız


ingestion pipeline


ETL jobs



DAY 19 — LangChain + Tools
Öğreneceklerin


tools


tool calling


orchestration



DAY 20 — LangGraph Agents
Yapacağımız


agent workflow


planning


multi-step execution



DAY 21 — AI Evaluation
Öğreneceklerin


hallucinations


evaluation


guardrails


prompt engineering



WEEK 4 — ENTERPRISE SYSTEM
Amaç:

“Gerçek production AI system”


DAY 22 — Authentication


auth basics


tokens


protected endpoints



DAY 23 — Background Jobs


queues


workers


async processing



DAY 24 — Document Processing


PDF ingestion


parsing


chunking pipeline



DAY 25 — Production Architecture


scalability


stateless services


infra thinking



DAY 26 — Testing


unit tests


integration tests


API testing



DAY 27 — Production Hardening


retries


timeout


rate limits


error handling



DAY 28 — System Design Review
Şunları konuşacağız:


neden böyle tasarladık


alternatives neydi


production riskleri ne



DAY 29 — Interview + Engineering Communication
Şunları öğreneceksin:


sistemi nasıl anlatırsın


architecture discussion


tradeoff explanation



DAY 30 — Final Production Deployment
Final Result
Senin:


deployed


dockerized


cloud-hosted


CI/CD enabled


agentic AI platformun olacak.



VE EN ÖNEMLİ KAZANIM
30 gün sonunda:
Şunu duyunca panik olmayacaksın:
“Azure pipeline failed after deployment because container env vars were missing and retrieval service timeout exceeded.”
Çünkü artık:


deployment ne biliyor olacaksın


container ne biliyor olacaksın


env vars ne biliyor olacaksın


retrieval service ne biliyor olacaksın 🙂


Ve bu gerçekten büyük dönüşüm.



-------------------------------------------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------
------------------------


# Enterprise AI Platform — 30 Day Engineering Roadmap

# FINAL GOAL

Build a production-style Agentic AI Platform using:

- FastAPI
- Docker
- Azure OpenAI
- Azure DevOps
- Databricks
- RAG
- LangGraph
- PostgreSQL
- Redis
- CI/CD
- Monitoring
- Containerized deployment

Main purpose:

Not just coding.

Understanding:
- enterprise systems
- architecture
- cloud engineering
- AI engineering
- software engineering mindset

---

# WEEK 1 — SOFTWARE ENGINEERING FOUNDATIONS

Goal:

Understand how enterprise backend systems work internally.

---

# DAY 1 — PROJECT FOUNDATION

## Concepts

- project structure
- virtual environments
- uv
- FastAPI basics
- config management
- environment variables

## Why?

Enterprise projects become large.

Without structure:
- code becomes chaotic
- debugging becomes difficult
- teamwork becomes painful

We learned:
- backend app structure
- why configs matter
- why .env exists
- why hardcoded values are dangerous

## Technical Work

- create project
- setup uv
- create FastAPI app
- create folder structure
- create config system

## Main Engineering Lesson

Software engineering is:
- organization
- maintainability
- scalability

not just writing code.

---

# DAY 2 — BACKEND ARCHITECTURE

## Concepts

- routers
- schemas
- services
- separation of concerns

## Why?

Business logic should not live inside HTTP routes.

We separate:
- HTTP layer
- validation layer
- business layer

This makes systems:
- scalable
- reusable
- maintainable

## Technical Work

- create routers
- create schemas
- create service layer
- create chat endpoint

## Main Engineering Lesson

Large systems survive through:
- separation
- modularity
- clear responsibilities

---

# DAY 3 — REQUEST FLOW + DEPENDENCY INJECTION

## Concepts

- request lifecycle
- FastAPI internals
- dependency injection
- inversion of control
- logging basics

## Why?

We must understand:
- how frameworks work internally
- how dependencies are created
- how systems communicate

Dependency Injection solves:
- tight coupling
- hardcoded dependencies
- testing problems
- scaling complexity

## Technical Work

- create dependency providers
- inject services
- implement logging
- improve config structure

## Main Engineering Lesson

Good architecture isolates:
- business logic
from
- infrastructure details

---

# DAY 4 — DOCKER + CONTAINERIZATION

## Concepts

- Docker
- containers
- images
- runtime environments
- isolation
- portability
- scalability

## Why?

Applications fail in production because:
- environments differ
- dependencies differ
- operating systems differ

Containers solve:
- consistency
- deployment reproducibility
- portability

## Technical Work

- create Dockerfile
- build Docker image
- run containerized backend
- understand port mapping

## Main Engineering Lesson

Modern cloud systems deploy:
- container images
not
- raw source code

---

# DAY 5 — MULTI-CONTAINER SYSTEMS

## Concepts

- Docker Compose
- service-to-service communication
- internal networking
- persistence
- stateful vs stateless systems

## Why?

Real systems contain:
- backend
- databases
- caches
- vector stores

all running independently.

## Technical Work

- add PostgreSQL
- add Redis
- create docker-compose.yml
- connect services together

## Main Engineering Lesson

Production systems are:
- distributed systems

not single applications.

---

# DAY 6 — DATABASE FUNDAMENTALS

## Concepts

- relational databases
- PostgreSQL
- tables
- primary keys
- foreign keys
- indexing
- transactions

## Why?

Most enterprise systems are data systems.

Understanding:
- persistence
- relationships
- querying

is foundational.

## Technical Work

- connect PostgreSQL
- create tables
- perform CRUD operations
- integrate database with FastAPI

## Main Engineering Lesson

Applications are usually:
- interfaces over data systems

---

# DAY 7 — REDIS + CACHING

## Concepts

- caching
- Redis
- in-memory systems
- latency reduction

## Why?

LLM systems are expensive and slow.

Caching improves:
- speed
- scalability
- cost efficiency

## Technical Work

- add Redis cache
- cache responses
- understand cache invalidation

## Main Engineering Lesson

Performance engineering matters in production.

---

# WEEK 2 — CLOUD + AZURE + DEVOPS

Goal:

Understand how modern cloud deployment works.

---

# DAY 8 — AZURE FUNDAMENTALS

## Concepts

- Azure ecosystem
- resource groups
- cloud services
- Azure architecture basics

## Why?

Cloud platforms organize:
- infrastructure
- deployment
- networking
- security

## Technical Work

- create Azure resources
- explore Azure Portal

## Main Engineering Lesson

Cloud is:
- managed infrastructure abstraction

---

# DAY 9 — AZURE OPENAI

## Concepts

- inference APIs
- embeddings
- LLM integration
- token usage

## Why?

AI systems require:
- external AI services
- scalable inference
- API-based communication

## Technical Work

- integrate Azure OpenAI
- create first LLM endpoint

## Main Engineering Lesson

Modern AI apps orchestrate external AI services.

---

# DAY 10 — AZURE DEVOPS

## Concepts

- repositories
- pipelines
- CI/CD
- artifacts

## Why?

Deployment must be:
- automated
- repeatable
- reliable

## Technical Work

- setup Azure DevOps
- connect GitHub repo

## Main Engineering Lesson

Production engineering requires automation.

---

# DAY 11 — CI/CD PIPELINES

## Concepts

- continuous integration
- continuous deployment
- automated testing
- build pipelines

## Why?

Manual deployment does not scale.

## Technical Work

- create pipeline
- automate Docker builds

## Main Engineering Lesson

Deployment should become:
- predictable
- automated

---

# DAY 12 — CLOUD DEPLOYMENT

## Concepts

- Azure Container Apps
- App Services
- deployment lifecycle

## Why?

Applications must run:
- outside local machines

## Technical Work

- deploy backend to Azure

## Main Engineering Lesson

Cloud systems are:
- remotely orchestrated infrastructure

---

# DAY 13 — SECRETS MANAGEMENT

## Concepts

- Key Vault
- secret storage
- credentials management

## Why?

Production secrets must never:
- live in source code

## Technical Work

- store API keys securely

## Main Engineering Lesson

Security is infrastructure responsibility.

---

# DAY 14 — OBSERVABILITY

## Concepts

- logging
- metrics
- tracing
- monitoring

## Why?

Production systems fail constantly.

Observability enables:
- debugging
- monitoring
- reliability

## Technical Work

- structured logging
- request tracing

## Main Engineering Lesson

You cannot manage systems you cannot observe.

---

# WEEK 3 — AI ENGINEERING + RAG

Goal:

Build real AI systems.

---

# DAY 15 — EMBEDDINGS + VECTOR SEARCH

## Concepts

- embeddings
- semantic similarity
- vector search

## Why?

LLMs cannot memorize enterprise knowledge dynamically.

## Technical Work

- generate embeddings
- store vectors

## Main Engineering Lesson

Modern AI systems rely on retrieval.

---

# DAY 16 — RAG PIPELINE

## Concepts

- retrieval augmented generation
- chunking
- retrieval flow

## Why?

RAG allows:
- factual grounding
- enterprise knowledge integration

## Technical Work

- build retrieval pipeline

## Main Engineering Lesson

AI systems combine:
- retrieval
- reasoning

---

# DAY 17 — DATABRICKS FUNDAMENTALS

## Concepts

- Spark
- Delta Lake
- notebooks
- distributed processing

## Why?

Enterprise AI requires:
- large-scale data engineering

## Technical Work

- create Databricks workflows

## Main Engineering Lesson

AI systems depend on data pipelines.

---

# DAY 18 — DATA PIPELINES

## Concepts

- ETL
- ingestion
- transformations
- orchestration

## Why?

Enterprise data constantly changes.

## Technical Work

- build ingestion pipeline

## Main Engineering Lesson

Reliable AI depends on reliable data flow.

---

# DAY 19 — LANGCHAIN + TOOLS

## Concepts

- tool calling
- orchestration
- agents

## Why?

LLMs become powerful when connected to tools.

## Technical Work

- implement tools
- connect APIs

## Main Engineering Lesson

AI systems are orchestration systems.

---

# DAY 20 — LANGGRAPH AGENTS

## Concepts

- agent workflows
- planning
- state machines

## Why?

Complex AI systems require:
- multi-step reasoning

## Technical Work

- build multi-agent workflows

## Main Engineering Lesson

Agents are:
- workflow systems around LLMs

---

# DAY 21 — AI EVALUATION

## Concepts

- hallucinations
- evaluation
- guardrails
- prompt engineering

## Why?

AI systems are probabilistic systems.

## Technical Work

- evaluate responses
- add protections

## Main Engineering Lesson

AI engineering is:
- reliability engineering

---

# WEEK 4 — PRODUCTION AI PLATFORM

Goal:

Transform prototype into production-style platform.

---

# DAY 22 — AUTHENTICATION

## Concepts

- auth
- tokens
- protected APIs

---

# DAY 23 — BACKGROUND WORKERS

## Concepts

- queues
- async jobs
- task systems

---

# DAY 24 — DOCUMENT INGESTION

## Concepts

- PDF parsing
- chunking
- indexing

---

# DAY 25 — SCALABILITY

## Concepts

- stateless services
- scaling
- distributed systems

---

# DAY 26 — TESTING

## Concepts

- unit tests
- integration tests
- mocking

---

# DAY 27 — PRODUCTION HARDENING

## Concepts

- retries
- timeouts
- error handling
- resilience

---

# DAY 28 — SYSTEM DESIGN REVIEW

## Concepts

- architecture review
- tradeoffs
- scaling analysis

---

# DAY 29 — ENGINEERING COMMUNICATION

## Concepts

- explaining systems
- architecture discussions
- interview communication

---

# DAY 30 — FINAL DEPLOYMENT

## Final Deliverable

Production-style:

- containerized
- cloud-deployed
- CI/CD-enabled
- AI-powered
- RAG-enabled
- agentic backend platform

## Final Engineering Outcome

Understanding:
- enterprise software systems
- cloud systems
- AI engineering
- production thinking
- scalable architecture
