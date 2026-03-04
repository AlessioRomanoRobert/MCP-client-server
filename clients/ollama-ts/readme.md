# Cliente MCP con Ollama (TypeScript)

Cliente de chat interactivo que conecta un LLM local de [Ollama](https://ollama.com) con un servidor MCP, habilitando **function calling** — el modelo puede invocar tools MCP de forma automática en respuesta a los mensajes del usuario.

## Cómo funciona

```
Mensaje del usuario ──► Ollama (LLM) ──► ¿tool_call? ──► Servidor MCP ──► resultado ──► Ollama ──► respuesta final
```

1. El usuario envía un mensaje
2. El LLM decide si responde directamente o llama a una tool MCP
3. Si se solicita una llamada a tool, el cliente la ejecuta contra el servidor MCP
4. El resultado se devuelve al LLM para que genere la respuesta final

---

## Requisitos previos

- Node.js v18+
- [Ollama](https://ollama.com) en ejecución local
- Un modelo con soporte de function calling (p. ej. `mistral`, `llama3`)

```bash
ollama pull mistral
```

## Instalación

```bash
npm install
npm run build
```

## Ejecución

```bash
npm start
```

El cliente:
1. Verifica la conexión con Ollama
2. Se conecta al servidor MCP
3. Inicia una sesión de chat interactivo

Escribe `/exit` (o `/quit`, `/salir`) para terminar la sesión.

## Configuración

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `MCP_SERVER_PATH` | *(relativa a la raíz del repositorio)* | Ruta absoluta al fichero JS del servidor MCP |

```bash
MCP_SERVER_PATH=/ruta/al/server.js npm start
```

El modelo por defecto es `mistral:latest`. Cámbialo modificando `DEFAULT_MODEL` en `src/ollamaApp.ts`.

## Estructura del proyecto

```
clients/ollama-ts/
├── src/
│   ├── ollamaApp.ts   Aplicación principal — OllamaAgent, bucle de chat, ejecución de tools
│   └── mcpClient.ts   Wrapper del cliente MCP (conexión, listado de tools, ejecución)
├── dist/              Salida compilada (tras el build)
├── package.json
└── tsconfig.json
```

## Resolución de problemas

**Ollama no responde**
```bash
ollama serve      # asegúrate de que está en marcha
ollama list       # verifica que tienes algún modelo descargado
```

**El servidor MCP no conecta** — comprueba que el servidor está compilado y la ruta es correcta:
```bash
cd servers/basic && npm run build
```
