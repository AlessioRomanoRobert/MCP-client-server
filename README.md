# MCP Client-Server Examples

A practical reference implementation of the **Model Context Protocol (MCP)** — covering servers, clients, and LLM integrations in TypeScript, Python, and Go.

---

## What is MCP?

**Model Context Protocol (MCP)** is an open standard that lets AI models securely connect to external tools, data sources, and services. Think of it as a universal plugin system for AI: instead of baking capabilities into a model's weights, you expose them as MCP servers and any compatible client (or LLM host) can use them dynamically.

### The problem MCP solves

Without a standard protocol, every AI application has to write custom integration code for every tool — file systems, databases, APIs, calculators, etc. This creates a combinatorial explosion of one-off connectors.

MCP defines a single interface so that **one server works with any client**, and **one client works with any server**.

```
┌──────────────────────┐           MCP           ┌─────────────────────┐
│   AI App / LLM Host  │ ◄────────────────────── │     MCP Server      │
│      (Client)        │  discover + call tools   │  (your tools/data)  │
└──────────────────────┘                          └─────────────────────┘
```

---

## Core Concepts

| Concept | Description |
|---|---|
| **Server** | A process that exposes capabilities (tools, resources, prompts) over MCP |
| **Client** | A process that connects to an MCP server and uses its capabilities |
| **Tool** | A function the AI can call — receives arguments, returns a result |
| **Resource** | Data the AI can read, identified by a URI (static or templated) |
| **Prompt** | A reusable message template that primes the AI for a specific task |
| **Transport** | The communication channel — `stdio` for local processes, HTTP/SSE for remote |

### Lifecycle

```
Client                          Server
  │                               │
  │──── initialize ──────────────►│   Exchange capabilities
  │◄─── initialized ──────────────│
  │                               │
  │──── tools/list ──────────────►│   Discover available tools
  │◄─── tools/list result ────────│
  │                               │
  │──── tools/call ──────────────►│   Execute a tool
  │◄─── tool result ──────────────│
  │                               │
```

---

## Project Structure

```
.
├── servers/
│   ├── basic/           TypeScript — quotes, math tools, code review prompt
│   ├── todo-ts/         TypeScript — full TODO CRUD via MCP tools
│   └── calculator-py/   Python     — arithmetic calculator (FastMCP)
│
└── clients/
    ├── basic-ts/        TypeScript — discovers and exercises the basic server
    ├── basic-py/        Python     — same, async version
    ├── ollama-ts/       TypeScript — Ollama LLM + MCP tool calling (interactive chat)
    └── ollama-py/       Python     — same, async version
```

---

## Quick Start

### Prerequisites

| Tool | Version |
|---|---|
| Node.js | v18+ |
| Python | 3.11+ |
| [uv](https://docs.astral.sh/uv/) | latest |
| Ollama *(only for ollama clients)* | latest |

---

### 1. Build and run the basic server

```bash
cd servers/basic
npm install
npm run build
npm start
```

### 2. Run the TypeScript client

```bash
cd clients/basic-ts
npm install
npm run build
npm start
```

> The client auto-discovers the server at `servers/basic/dist/server.js` relative to the repo root.
> Override with: `MCP_SERVER_PATH=/absolute/path/to/server.js npm start`

### 3. Run the Python client

```bash
cd clients/basic-py
uv sync
uv run main.py
```

### 4. Interactive chat with Ollama

Make sure [Ollama](https://ollama.com) is running and you have a model pulled (e.g. `ollama pull mistral`).

```bash
cd clients/ollama-ts
npm install
npm run build
npm start
```

Type messages in the terminal. The LLM will call MCP tools automatically when needed.
Type `/exit` to quit.

---

## Servers

| Server | Language | Description |
|---|---|---|
| [`basic`](servers/basic/) | TypeScript | Quotes API, LCM math tool, person resource, code review prompt |
| [`todo-ts`](servers/todo-ts/) | TypeScript | In-memory TODO list with full CRUD |
| [`calculator-py`](servers/calculator-py/) | Python | add, subtract, multiply, divide |

## Clients

| Client | Language | Description |
|---|---|---|
| [`basic-ts`](clients/basic-ts/) | TypeScript | Exercises all capabilities of the basic server |
| [`basic-py`](clients/basic-py/) | Python | Same as basic-ts, async |
| [`ollama-ts`](clients/ollama-ts/) | TypeScript | Interactive chat — Ollama LLM with MCP tool calling |
| [`ollama-py`](clients/ollama-py/) | Python | Same as ollama-ts, async |

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `MCP_SERVER_PATH` | *(relative to client)* | Absolute path to the MCP server JS file |
| `OLLAMA_URL` | `http://localhost:11434` | Ollama API base URL *(ollama clients only)* |

---

## License

[Apache 2.0](LICENSE)
