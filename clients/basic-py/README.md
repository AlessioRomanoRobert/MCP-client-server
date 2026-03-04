# Cliente MCP básico (Python)

Cliente MCP mínimo asíncrono en Python que se conecta al [servidor basic](../../servers/basic/) y ejercita los tres tipos de capacidades: tools, resources y prompts.

## Qué hace

1. Se conecta al servidor MCP básico a través de stdio
2. Lista todos los **prompts**, **resources**, **resource templates** y **tools** disponibles
3. Llama a cada uno con argumentos de ejemplo e imprime los resultados

---

## Instalación

**Requisitos:** Python 3.11+, [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

## Ejecución

```bash
uv run main.py
```

Por defecto el cliente resuelve la ruta del servidor relativa a la raíz del repositorio (`servers/basic/dist/server.js`). Para sobreescribirla:

```bash
MCP_SERVER_PATH=/ruta/absoluta/al/server.js uv run main.py
```

> El servidor basic debe estar compilado antes de ejecutar este cliente (`cd servers/basic && npm run build`).

## Estructura del proyecto

```
clients/basic-py/
├── main.py          Punto de entrada del cliente
└── pyproject.toml   Configuración del proyecto Python y dependencias
```
