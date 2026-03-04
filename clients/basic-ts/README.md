# Cliente MCP básico (TypeScript)

Cliente MCP mínimo en TypeScript que se conecta al [servidor basic](../../servers/basic/) y ejercita los tres tipos de capacidades: tools, resources y prompts.

## Qué hace

1. Se conecta al servidor MCP básico a través de stdio
2. Lista todos los **prompts**, **resources**, **resource templates** y **tools** disponibles
3. Llama a cada uno con argumentos de ejemplo e imprime los resultados

## Quién decide qué tool llamar

**Este cliente, no un LLM.** El código llama a las tools de forma hardcodeada y directa — es el equivalente a hacer peticiones a una API REST. No hay inteligencia en medio: tú controlas exactamente qué se ejecuta y cuándo.

```
Tu código  ──►  tools/call  ──►  Servidor MCP  ──►  resultado  ──►  Tu código
```

Si quieres que sea un LLM quien decida qué tools llamar según el contexto de una conversación, mira [`ollama-ts`](../ollama-ts/).

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

Por defecto el cliente resuelve la ruta del servidor relativa a la raíz del repositorio (`servers/basic/dist/server.js`). Para sobreescribirla:

```bash
MCP_SERVER_PATH=/ruta/absoluta/al/server.js npm start
```

> El servidor basic debe estar compilado antes de ejecutar este cliente (`cd servers/basic && npm run build`).

## Estructura del proyecto

```
clients/basic-ts/
├── src/
│   └── index.ts     Punto de entrada del cliente
├── dist/            Salida compilada (tras el build)
├── package.json
└── tsconfig.json
```
