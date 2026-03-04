# Calculator MCP Server

A minimal MCP server written in Python using [FastMCP](https://github.com/jlowin/fastmcp). Exposes a single `calculate` tool that performs basic arithmetic operations.

## Tools

| Name | Arguments | Description |
|---|---|---|
| `calculate` | `a: float`, `b: float`, `operation: str` | Performs `add`, `subtract`, `multiply`, or `divide` on two numbers |

**Valid operations:** `add` · `subtract` · `multiply` · `divide`

Division by zero raises a `ValueError`.

---

## Setup

**Prerequisites:** Python 3.11+, [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

## Run

```bash
uv run server.py
```

The server communicates over **stdio** and is meant to be launched by an MCP client.

## Project Structure

```
servers/calculator-py/
├── server.py        FastMCP server — tool definition
└── pyproject.toml   Python project and dependency config
```

## Connecting a Client

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["path/to/servers/calculator-py/server.py"],
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        result = await session.call_tool("calculate", {"a": 10, "b": 3, "operation": "add"})
        print(result)  # 13.0
```
