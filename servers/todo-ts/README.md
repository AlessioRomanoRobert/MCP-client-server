# TODO MCP Server

An MCP server written in TypeScript that exposes a full TODO list manager through MCP **tools**. Uses in-memory storage — state resets when the server restarts.

## Tools

| Name | Arguments | Description |
|---|---|---|
| `TODO-Create` | `task: string` | Add a new TODO item |
| `TODO-List` | — | List all TODO items (pending and completed) |
| `TODO-Complete` | `id: string` | Mark an item as completed |
| `TODO-Update` | `id: string`, `task: string` | Update the text of an existing item |
| `TODO-Delete` | `id: string` | Delete an item permanently |
| `TODO-ClearCompleted` | — | Remove all completed items at once |

---

## Setup

**Prerequisites:** Node.js v18+

```bash
npm install
npm run build
```

## Run

```bash
npm start
```

The server communicates over **stdio** and is meant to be launched by an MCP client.

## Project Structure

```
servers/todo-ts/
├── src/
│   ├── index.ts             Server entry point — tool definitions
│   └── todo/
│       └── todo.service.ts  In-memory store and CRUD helpers
├── dist/                    Compiled JavaScript output (after build)
├── package.json
└── tsconfig.json
```

## Connecting a Client

```typescript
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["path/to/servers/todo-ts/dist/index.js"],
});
```
