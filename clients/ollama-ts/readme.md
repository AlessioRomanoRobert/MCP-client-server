# Ollama MCP Client (TypeScript)

An interactive chat client that connects a local [Ollama](https://ollama.com) LLM to an MCP server, enabling **function calling** — the model can invoke MCP tools automatically in response to user messages.

## How it works

```
User input ──► Ollama (LLM) ──► tool_call? ──► MCP Server ──► result ──► Ollama ──► final response
```

1. User sends a message
2. The LLM decides whether to answer directly or call an MCP tool
3. If a tool call is requested, the client executes it via the MCP server
4. The tool result is fed back to the LLM for the final answer

---

## Prerequisites

- Node.js v18+
- [Ollama](https://ollama.com) running locally
- A model with function calling support (e.g. `mistral`, `llama3`)

```bash
ollama pull mistral
```

## Setup

```bash
npm install
npm run build
```

## Run

```bash
npm start
```

The client will:
1. Verify the Ollama connection
2. Connect to the MCP server
3. Start an interactive chat session

Type `/exit` (or `/quit`, `/salir`) to end the session.

## Configuration

| Variable | Default | Description |
|---|---|---|
| `MCP_SERVER_PATH` | *(relative to repo root)* | Absolute path to the MCP server JS file |

```bash
MCP_SERVER_PATH=/path/to/server.js npm start
```

The default model is `mistral:latest`. Change `DEFAULT_MODEL` in `src/ollamaApp.ts` to use another.

## Project Structure

```
clients/ollama-ts/
├── src/
│   ├── ollamaApp.ts   Main application — OllamaAgent, chat loop, tool execution
│   └── mcpClient.ts   MCP client wrapper (connect, list tools, execute)
├── dist/              Compiled output (after build)
├── package.json
└── tsconfig.json
```

## Troubleshooting

**Ollama not responding**
```bash
ollama serve      # make sure it's running
ollama list       # verify you have a model downloaded
```

**MCP server not connecting** — check that the server is built and the path is correct:
```bash
cd servers/basic && npm run build
```
