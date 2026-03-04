# Servidor MCP de Notas (Python)

Servidor MCP escrito en Python con [FastMCP](https://github.com/jlowin/fastmcp) que expone un sistema de notas persistentes respaldado por **SQLite**. Las notas sobreviven entre reinicios del servidor — a diferencia del servidor TODO en memoria.

Este ejemplo demuestra el caso de uso real más potente de MCP con un LLM: **darle al modelo una memoria persistente** a través de herramientas de lectura y escritura.

---

## Por qué es útil en un cliente de chat

Cuando conectas este servidor a un cliente como `ollama-py` o `ollama-ts`, el LLM puede:

- Recordar información que le dices: `"apunta que la reunión con Pedro es el lunes"`
- Recuperarla más tarde: `"¿qué tenía apuntado sobre Pedro?"`
- Organizar conocimiento por etiquetas: `"muéstrame todas las notas de trabajo"`
- Actuar como un segundo cerebro conversacional

Las notas se guardan en `~/.mcp-notes.db` y persisten entre sesiones.

---

## Tools

| Nombre | Argumentos | Descripción |
|---|---|---|
| `create_note` | `title`, `content`, `tags?` | Crea una nota nueva. `tags` es una lista separada por comas |
| `list_notes` | `tag?` | Lista todas las notas, opcionalmente filtradas por etiqueta |
| `get_note` | `id` | Devuelve el contenido completo de una nota |
| `search_notes` | `query` | Busca notas por texto en título o contenido |
| `update_note` | `id`, `title?`, `content?`, `tags?` | Actualiza los campos indicados de una nota existente |
| `delete_note` | `id` | Elimina una nota de forma permanente |

---

## Instalación y ejecución

**Requisitos:** Python 3.11+, [uv](https://docs.astral.sh/uv/)

```bash
cd servers/notes-py
uv sync
uv run server.py
```

El servidor escucha por **stdio** y está diseñado para ser lanzado por un cliente MCP.

---

## Cómo funciona FastMCP aquí

FastMCP convierte automáticamente cada función decorada con `@mcp.tool()` en una tool MCP. El nombre, la descripción y el esquema de argumentos se infieren del código — sin boilerplate:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Notes MCP Server")

@mcp.tool()
def create_note(title: str, content: str, tags: str = "") -> str:
    """
    Crea una nueva nota con título y contenido.
    El parámetro tags es una lista de etiquetas separadas por comas.
    Devuelve el ID de la nota creada.
    """
    # ... lógica SQLite
```

Lo que FastMCP hace por ti:
- **Nombre** → tomado del nombre de la función (`create_note`)
- **Descripción** → tomada del docstring (el LLM la usa para decidir cuándo llamarla)
- **Esquema JSON** → inferido de los type hints (`str`, `int`, valores por defecto)
- **Transporte** → `mcp.run(transport="stdio")` en una línea

---

## Estructura del proyecto

```
servers/notes-py/
├── server.py        Servidor FastMCP — definición de todas las tools
└── pyproject.toml   Configuración del proyecto y dependencias
```

La base de datos se crea automáticamente en `~/.mcp-notes.db` al arrancar el servidor.

---

## Conectar un cliente Python

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="uv",
    args=["run", "path/to/servers/notes-py/server.py"],
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()

        # Crear una nota
        result = await session.call_tool("create_note", {
            "title": "Ideas para el proyecto",
            "content": "Usar SQLite para persistencia. Explorar FastMCP.",
            "tags": "trabajo,ideas"
        })
        print(result)  # Nota creada con ID 1.

        # Buscar notas
        result = await session.call_tool("search_notes", {"query": "SQLite"})
        print(result)
```
