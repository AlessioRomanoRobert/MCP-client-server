# Servidor MCP TODO

Servidor MCP escrito en TypeScript que expone un gestor completo de tareas pendientes a través de **tools** MCP. Usa almacenamiento en memoria — el estado se reinicia al reiniciar el servidor.

## Tools

| Nombre | Argumentos | Descripción |
|---|---|---|
| `TODO-Create` | `task: string` | Añade un nuevo elemento a la lista |
| `TODO-List` | — | Lista todos los elementos (pendientes y completados) |
| `TODO-Complete` | `id: string` | Marca un elemento como completado |
| `TODO-Update` | `id: string`, `task: string` | Actualiza el texto de un elemento existente |
| `TODO-Delete` | `id: string` | Elimina un elemento de forma permanente |
| `TODO-ClearCompleted` | — | Elimina todos los elementos completados de una vez |

---

## Instalación

**Requisitos:** Node.js v18+

```bash
npm install
npm run build
```

## Ejecución

```bash
npm start
```

El servidor se comunica por **stdio** y está diseñado para ser lanzado por un cliente MCP.

## Estructura del proyecto

```
servers/todo-ts/
├── src/
│   ├── index.ts             Punto de entrada del servidor — definición de tools
│   └── todo/
│       └── todo.service.ts  Almacén en memoria y helpers CRUD
├── dist/                    Salida JavaScript compilada (tras el build)
├── package.json
└── tsconfig.json
```

## Conectar un cliente

```typescript
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["path/to/servers/todo-ts/dist/index.js"],
});
```
