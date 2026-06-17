# Knowledge Intelligence Service

## Purpose

The Knowledge Intelligence Service provides structured, API-based access to the Garden Knowledge Repository.

The service acts as the operational interface between AI agents and the Knowledge Layer.

---

## Architecture

```text
Custom GPT
    ↓
Knowledge Intelligence Service
    ↓
GitHub API
    ↓
Knowledge Intelligence Platform Repository
```

The service does not maintain a local repository copy.

GitHub remains the single source of truth.

Knowledge objects are retrieved directly from the GitHub repository at runtime.

---

## Repository

Repository:

PendragonXIII/Knowledge-Intelligence-Platform

Repository Visibility:

Private

Access Method:

GitHub Contents API

Authentication:

GitHub Personal Access Token

Environment Variable:

GITHUB_TOKEN

---

## Deployment

Platform:

Railway

Runtime:

FastAPI

Application Server:

Uvicorn

Start Command:

python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT

---

## Environment Variables

### GITHUB_TOKEN

Used to authenticate against the private GitHub repository.

Required:

Yes

Purpose:

Repository access and knowledge retrieval.

### API_KEY

Used to authenticate API consumers.

Required:

Yes

Purpose:

Protects production endpoints from unauthorized access.

---

## Available Endpoints

### Health Check

GET /

Returns service health information.

### Get Knowledge Object

GET /objects/{object_id}

Returns a parsed knowledge object.

Example:

GET /objects/EID.08

### Get Context Pack

GET /context/{object_id}

Returns a depth-2 context pack assembled from related knowledge objects.

Example:

GET /context/EID.08

---

## Authentication

Protected endpoints require the header:

X-API-Key: <API_KEY>

Protected Endpoints:

* /objects/{object_id}
* /context/{object_id}

Requests without a valid API key return:

HTTP 401 Unauthorized

---

## Retrieval Strategy

Knowledge objects are resolved dynamically through GitHub.

Object resolution searches the repository for matching knowledge object IDs.

Supported repository areas:

* Capabilities
* Contraints
* Standards
* Playbooks
* Roadmaps
* Opportunities
* Learnings
* Architectual Decisions

The first matching knowledge object is retrieved and parsed.

---

## Context Assembly

Context packs are assembled using repository relationships.

Current configuration:

Depth = 2

Context packs include:

* Target object
* Directly related objects
* Second-level related objects

This enables AI agents to consume contextual knowledge instead of isolated documents.

---

## Testing

Run all tests:

python -m pytest

Current Status:

19 passing tests

Test Coverage Includes:

* Markdown parsing
* Link parsing
* Object resolution
* Retrieval service
* Relationship service
* Context assembly
* GitHub repository integration
* Authentication

---

## Current Capability Status

Knowledge Retrieval

Status:

Operational MVP

Capabilities:

* GitHub-native retrieval
* Railway deployment
* Private repository support
* Context assembly
* API authentication
* Automated testing

Next Planned Capabilities:

1. Search
2. GPT Integration
3. Knowledge Object Creation
4. Knowledge Object Update
5. Repository Synchronization
6. Knowledge Graph Intelligence
