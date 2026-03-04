import asyncio
import os
import pathlib
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Path to the basic server — override with MCP_SERVER_PATH env var
_HERE = pathlib.Path(__file__).parent
server_path = os.environ.get(
    "MCP_SERVER_PATH",
    str(_HERE / "../../../servers/basic/dist/server.js"),
)

server_params = StdioServerParameters(
    command="node",
    args=[server_path],
    env=None,
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()
            print("Prompts:")
            print(prompts)

            # Execute a prompt
            prompt = await session.get_prompt(
                prompts.prompts[1].name,
                arguments={
                    "code": "console.log('Hello, world!');"
                }
            )
            print("Prompt:")
            print(prompt)

            # List available resources
            resources = await session.list_resources()
            print("Resources:")
            print(resources)

            # List dynamic resource templates
            template_resources = await session.list_resource_templates()
            print("Template Resources:")
            print(template_resources)

            # Read a resource
            resource = await session.read_resource("got://quotes/random")
            print("Resource:")
            print(resource)

            # Read a template resource
            resource = await session.read_resource("person://properties/alexys")
            print("Resource:")
            print(resource)

            # List available tools
            tools = await session.list_tools()
            print("Tools:")
            print(tools)

            # Call a tool
            tool_result = await session.call_tool(
                tools.tools[1].name,
                arguments={
                    "numbers": [1, 2, 3, 4, 5]
                },
            )
            print("Tool Result:")
            print(tool_result)

if __name__ == "__main__":
    asyncio.run(run())
