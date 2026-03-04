# Basic MCP Client (Python)

A minimal async Python MCP client that connects to the [basic server](../../servers/basic/) and exercises all three capability types: tools, resources, and prompts.

## What it does

1. Connects to the basic MCP server via stdio
2. Lists all available **prompts**, **resources**, **resource templates**, and **tools**
3. Calls each one with sample arguments and prints the results

---

## Setup

**Prerequisites:** Python 3.11+, [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

## Run

```bash
uv run main.py
```

By default the client resolves the server path relative to the repo root (`servers/basic/dist/server.js`). Override with:

```bash
MCP_SERVER_PATH=/absolute/path/to/server.js uv run main.py
```

> The basic server must be built before running this client (`cd servers/basic && npm run build`).

## Project Structure

```
clients/basic-py/
├── main.py          Client entry point
└── pyproject.toml   Python project and dependency config
```
