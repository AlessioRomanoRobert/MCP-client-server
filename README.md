# MCP Client-Server — Ejemplos prácticos

Una implementación de referencia del **Model Context Protocol (MCP)** — con servidores, clientes e integraciones con LLMs en TypeScript, Python y Go.

---

## ¿Qué es MCP?

**Model Context Protocol (MCP)** es un estándar abierto que permite a los modelos de IA conectarse de forma segura a herramientas externas, fuentes de datos y servicios. Piensa en él como un sistema universal de plugins para IA: en lugar de integrar capacidades directamente en los pesos del modelo, se exponen como servidores MCP y cualquier cliente compatible puede usarlas de forma dinámica.

### El problema que resuelve MCP

Sin un protocolo estándar, cada aplicación de IA tiene que escribir código de integración personalizado para cada herramienta — sistemas de ficheros, bases de datos, APIs, calculadoras, etc. Esto provoca una explosión combinatoria de conectores ad hoc.

MCP define una interfaz única para que **un servidor funcione con cualquier cliente** y **un cliente funcione con cualquier servidor**.

```
┌──────────────────────┐           MCP           ┌─────────────────────┐
│   App de IA / Host   │ ◄────────────────────── │     Servidor MCP    │
│      (Cliente)       │  descubrir + llamar      │  (tus tools/datos)  │
└──────────────────────┘                          └─────────────────────┘
```

---

## Conceptos clave

| Concepto | Descripción |
|---|---|
| **Server** | Proceso que expone capacidades (tools, resources, prompts) a través de MCP |
| **Client** | Proceso que se conecta a un servidor MCP y usa sus capacidades |
| **Tool** | Función que la IA puede invocar — recibe argumentos y devuelve un resultado |
| **Resource** | Dato que la IA puede leer, identificado por una URI (estática o con plantilla) |
| **Prompt** | Plantilla de mensaje reutilizable que prepara a la IA para una tarea concreta |
| **Transport** | Canal de comunicación — `stdio` para procesos locales, HTTP/SSE para remotos |

### Ciclo de vida

```
Cliente                         Servidor
  │                               │
  │──── initialize ──────────────►│   Intercambio de capacidades
  │◄─── initialized ──────────────│
  │                               │
  │──── tools/list ──────────────►│   Descubrir herramientas disponibles
  │◄─── tools/list result ────────│
  │                               │
  │──── tools/call ──────────────►│   Ejecutar una herramienta
  │◄─── tool result ──────────────│
  │                               │
```

---

## Estructura del proyecto

```
.
├── servers/
│   ├── basic/           TypeScript — citas aleatorias, herramienta matemática, prompt de revisión de código
│   ├── todo-ts/         TypeScript — gestor TODO completo con CRUD vía MCP
│   └── calculator-py/   Python     — calculadora aritmética (FastMCP)
│
└── clients/
    ├── basic-ts/        TypeScript — explora todas las capacidades del servidor basic
    ├── basic-py/        Python     — igual que basic-ts, versión asíncrona
    ├── ollama-ts/       TypeScript — chat interactivo con Ollama LLM + tool calling MCP
    └── ollama-py/       Python     — igual que ollama-ts, versión asíncrona
```

---

## Inicio rápido

### Requisitos previos

| Herramienta | Versión |
|---|---|
| Node.js | v18+ |
| Python | 3.11+ |
| [uv](https://docs.astral.sh/uv/) | última |
| Ollama *(solo para los clientes ollama)* | última |

---

### 1. Compilar y arrancar el servidor básico

```bash
cd servers/basic
npm install
npm run build
npm start
```

### 2. Ejecutar el cliente TypeScript

```bash
cd clients/basic-ts
npm install
npm run build
npm start
```

> El cliente resuelve automáticamente la ruta del servidor relativa a la raíz del repositorio (`servers/basic/dist/server.js`).
> Para sobreescribirla: `MCP_SERVER_PATH=/ruta/absoluta/al/server.js npm start`

### 3. Ejecutar el cliente Python

```bash
cd clients/basic-py
uv sync
uv run main.py
```

### 4. Chat interactivo con Ollama

Asegúrate de que [Ollama](https://ollama.com) está en marcha y tienes un modelo descargado (p. ej. `ollama pull mistral`).

```bash
cd clients/ollama-ts
npm install
npm run build
npm start
```

Escribe mensajes en la terminal. El LLM llamará a las herramientas MCP de forma automática cuando lo necesite.
Escribe `/exit` para salir.

---

## Servidores

| Servidor | Lenguaje | Descripción |
|---|---|---|
| [`basic`](servers/basic/) | TypeScript | API de citas, herramienta LCM, resource de persona, prompt de revisión de código |
| [`todo-ts`](servers/todo-ts/) | TypeScript | Lista TODO en memoria con CRUD completo |
| [`calculator-py`](servers/calculator-py/) | Python | suma, resta, multiplicación, división |

## Clientes

| Cliente | Lenguaje | Descripción |
|---|---|---|
| [`basic-ts`](clients/basic-ts/) | TypeScript | Ejercita todas las capacidades del servidor basic |
| [`basic-py`](clients/basic-py/) | Python | Igual que basic-ts, versión asíncrona |
| [`ollama-ts`](clients/ollama-ts/) | TypeScript | Chat interactivo — Ollama LLM con tool calling MCP |
| [`ollama-py`](clients/ollama-py/) | Python | Igual que ollama-ts, versión asíncrona |

---

## Variables de entorno

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `MCP_SERVER_PATH` | *(relativa al cliente)* | Ruta absoluta al fichero JS del servidor MCP |
| `OLLAMA_URL` | `http://localhost:11434` | URL base de la API de Ollama *(solo clientes ollama)* |

---

## Licencia

[Apache 2.0](LICENSE)
