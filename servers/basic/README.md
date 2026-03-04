# Servidor MCP básico

Servidor MCP escrito en TypeScript que demuestra los tres tipos de capacidades principales de MCP: **tools**, **resources** y **prompts**.

## Capacidades

### Tools

| Nombre | Descripción |
|---|---|
| `get_random_quotes` | Obtiene entre 1 y 10 citas aleatorias desde una API pública |
| `lcm` | Calcula el mínimo común múltiplo de una lista de números |

### Resources

| URI | Descripción |
|---|---|
| `got://quotes/random` | Resource estático — devuelve 5 citas aleatorias |
| `person://properties/{name}` | Resource con plantilla — devuelve las propiedades de una persona por nombre (`alexys`, `mariana`) |

### Prompts

| Nombre | Argumentos | Descripción |
|---|---|---|
| `got_quotes_analysis` | `theme?` (opcional) | Prepara a la IA para analizar citas, con temática opcional |
| `code_review` | `code` | Prepara a la IA para realizar una revisión de código exhaustiva |

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

El servidor escucha por **stdio** — está diseñado para ser lanzado por un cliente MCP, no para ejecutarse directamente como servidor HTTP independiente.

## Estructura del proyecto

```
servers/basic/
├── src/
│   └── server.ts     Servidor principal — tools, resources y prompts
├── dist/             Salida JavaScript compilada (tras el build)
├── package.json
└── tsconfig.json
```

## Conectar un cliente

Desde un cliente, lanza este servidor a través del transporte stdio:

```typescript
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["path/to/servers/basic/dist/server.js"],
});
```

Consulta [`clients/basic-ts`](../../clients/basic-ts/) o [`clients/basic-py`](../../clients/basic-py/) para ver ejemplos funcionales.
