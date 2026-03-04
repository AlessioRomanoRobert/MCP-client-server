# Servidor MCP Calculadora

Servidor MCP mínimo escrito en Python usando [FastMCP](https://github.com/jlowin/fastmcp). Expone una tool `calculate` que realiza operaciones aritméticas básicas.

## Tools

| Nombre | Argumentos | Descripción |
|---|---|---|
| `calculate` | `a: float`, `b: float`, `operation: str` | Realiza `add`, `subtract`, `multiply` o `divide` sobre dos números |

**Operaciones válidas:** `add` · `subtract` · `multiply` · `divide`

La división por cero lanza un `ValueError`.

---

## Instalación

**Requisitos:** Python 3.11+, [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

## Ejecución

```bash
uv run server.py
```

El servidor se comunica por **stdio** y está diseñado para ser lanzado por un cliente MCP.

## Estructura del proyecto

```
servers/calculator-py/
├── server.py        Servidor FastMCP — definición de la tool
└── pyproject.toml   Configuración del proyecto Python y dependencias
```

## Conectar un cliente

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
