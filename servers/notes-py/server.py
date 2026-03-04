import json
import sqlite3
from datetime import datetime
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Notes MCP Server")

DB_PATH = Path.home() / ".mcp-notes.db"


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                title      TEXT NOT NULL,
                content    TEXT NOT NULL,
                tags       TEXT NOT NULL DEFAULT '[]',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@mcp.tool()
def create_note(title: str, content: str, tags: str = "") -> str:
    """
    Crea una nueva nota con título y contenido.
    El parámetro tags es una lista de etiquetas separadas por comas (p. ej. "trabajo,ideas,python").
    Devuelve el ID de la nota creada.
    """
    now = datetime.now().isoformat()
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []

    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO notes (title, content, tags, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (title, content, json.dumps(tag_list), now, now),
        )
        note_id = cursor.lastrowid

    return f"Nota creada con ID {note_id}."


@mcp.tool()
def list_notes(tag: str = "") -> str:
    """
    Lista todas las notas, opcionalmente filtradas por etiqueta.
    Devuelve un resumen con ID, título, etiquetas y fecha de creación.
    """
    with get_db() as conn:
        if tag:
            rows = conn.execute(
                'SELECT id, title, tags, created_at FROM notes WHERE tags LIKE ? ORDER BY created_at DESC',
                (f'%"{tag}"%',),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT id, title, tags, created_at FROM notes ORDER BY created_at DESC"
            ).fetchall()

    if not rows:
        msg = f"No hay notas con la etiqueta '{tag}'." if tag else "No hay notas guardadas."
        return msg

    lines = []
    for row in rows:
        tag_str = ""
        parsed = json.loads(row["tags"])
        if parsed:
            tag_str = f" [{', '.join(parsed)}]"
        lines.append(f"[{row['id']}] {row['title']}{tag_str} — {row['created_at'][:10]}")

    return "\n".join(lines)


@mcp.tool()
def get_note(id: int) -> str:
    """
    Devuelve el contenido completo de una nota a partir de su ID.
    """
    with get_db() as conn:
        row = conn.execute("SELECT * FROM notes WHERE id = ?", (id,)).fetchone()

    if not row:
        return f"No existe ninguna nota con ID {id}."

    tags = json.loads(row["tags"])
    tag_str = f"\nEtiquetas: {', '.join(tags)}" if tags else ""
    return (
        f"# {row['title']}{tag_str}\n"
        f"Creada: {row['created_at'][:10]} | Actualizada: {row['updated_at'][:10]}\n\n"
        f"{row['content']}"
    )


@mcp.tool()
def search_notes(query: str) -> str:
    """
    Busca notas cuyo título o contenido contenga el texto indicado.
    Devuelve las notas encontradas con un fragmento de su contenido.
    """
    with get_db() as conn:
        rows = conn.execute(
            "SELECT id, title, content, tags FROM notes "
            "WHERE title LIKE ? OR content LIKE ? "
            "ORDER BY updated_at DESC",
            (f"%{query}%", f"%{query}%"),
        ).fetchall()

    if not rows:
        return f"No se encontraron notas para '{query}'."

    results = []
    for row in rows:
        tags = json.loads(row["tags"])
        tag_str = f" [{', '.join(tags)}]" if tags else ""
        snippet = row["content"][:120].replace("\n", " ")
        if len(row["content"]) > 120:
            snippet += "..."
        results.append(f"[{row['id']}] {row['title']}{tag_str}\n  {snippet}")

    return "\n\n".join(results)


@mcp.tool()
def update_note(id: int, title: str = "", content: str = "", tags: str = "") -> str:
    """
    Actualiza una nota existente. Solo se modifican los campos que se proporcionen.
    Si se pasan tags, reemplazan completamente a las anteriores.
    """
    with get_db() as conn:
        row = conn.execute("SELECT * FROM notes WHERE id = ?", (id,)).fetchone()
        if not row:
            return f"No existe ninguna nota con ID {id}."

        new_title   = title   if title   else row["title"]
        new_content = content if content else row["content"]
        new_tags    = json.dumps([t.strip() for t in tags.split(",") if t.strip()]) if tags else row["tags"]

        conn.execute(
            "UPDATE notes SET title=?, content=?, tags=?, updated_at=? WHERE id=?",
            (new_title, new_content, new_tags, datetime.now().isoformat(), id),
        )

    return f"Nota {id} actualizada correctamente."


@mcp.tool()
def delete_note(id: int) -> str:
    """
    Elimina una nota de forma permanente a partir de su ID.
    """
    with get_db() as conn:
        row = conn.execute("SELECT title FROM notes WHERE id = ?", (id,)).fetchone()
        if not row:
            return f"No existe ninguna nota con ID {id}."
        conn.execute("DELETE FROM notes WHERE id = ?", (id,))

    return f"Nota '{row['title']}' eliminada."


# ---------------------------------------------------------------------------

init_db()

if __name__ == "__main__":
    mcp.run(transport="stdio")
