# Basic MCP Client (TypeScript)

A minimal TypeScript MCP client that connects to the [basic server](../../servers/basic/) and exercises all three capability types: tools, resources, and prompts.

## What it does

1. Connects to the basic MCP server via stdio
2. Lists all available **prompts**, **resources**, **resource templates**, and **tools**
3. Calls each one with sample arguments and prints the results

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

By default the client resolves the server path relative to the repo root (`servers/basic/dist/server.js`). Override with:

```bash
MCP_SERVER_PATH=/absolute/path/to/server.js npm start
```

> The basic server must be built before running this client (`cd servers/basic && npm run build`).

## Project Structure

```
clients/basic-ts/
├── src/
│   └── index.ts     Client entry point
├── dist/            Compiled output (after build)
├── package.json
└── tsconfig.json
```
