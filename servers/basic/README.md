# Basic MCP Server

A feature-rich MCP server written in TypeScript that demonstrates the three core MCP capability types: **tools**, **resources**, and **prompts**.

## Capabilities

### Tools

| Name | Description |
|---|---|
| `get_random_quotes` | Fetches 1–10 random quotes from a public quotes API |
| `lcm` | Calculates the least common multiple of a list of numbers |

### Resources

| URI | Description |
|---|---|
| `got://quotes/random` | Static resource — returns 5 random quotes |
| `person://properties/{name}` | Template resource — returns properties for a named person (`alexys`, `mariana`) |

### Prompts

| Name | Arguments | Description |
|---|---|---|
| `got_quotes_analysis` | `theme?` (optional) | Primes the AI to analyze quotes, optionally focused on a theme |
| `code_review` | `code` | Primes the AI to perform a thorough code review |

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

The server listens on **stdio** — it is designed to be launched by an MCP client, not run directly as a standalone HTTP server.

## Project Structure

```
servers/basic/
├── src/
│   └── server.ts     Main server — tools, resources, and prompts
├── dist/             Compiled JavaScript output (after build)
├── package.json
└── tsconfig.json
```

## Connecting a Client

From a client, launch this server via stdio transport:

```typescript
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["path/to/servers/basic/dist/server.js"],
});
```

See [`clients/basic-ts`](../../clients/basic-ts/) or [`clients/basic-py`](../../clients/basic-py/) for working examples.
