import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { fileURLToPath } from "url";
import path from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Path to the basic server — override with MCP_SERVER_PATH env var
const serverPath = process.env.MCP_SERVER_PATH ||
  path.resolve(__dirname, "../../../servers/basic/dist/server.js");

const transport = new StdioClientTransport({
  command: "node",
  args: [serverPath]
});

// Create a client
const client = new Client(
  {
    name: "basic-client",
    version: "1.0.0"
  },
  {
    capabilities: {
      prompts: {},
      resources: {},
      tools: {}
    }
  }
);

await client.connect(transport);

// List prompts
const prompts = await client.listPrompts();
console.log(JSON.stringify(prompts, null, 2));

// List resources
const resources = await client.listResources();
console.log(JSON.stringify(resources, null, 2));

// List template resources
const templateResources = await client.listResourceTemplates();
console.log(JSON.stringify(templateResources, null, 2));

// List tools
const tools = await client.listTools();
console.log(JSON.stringify(tools, null, 2));

// Get a prompt
console.log("========================================")
console.log("Getting prompt: code_review")
const prompt = await client.getPrompt({
  name: prompts.prompts[1].name,
  arguments: {
    code: "print('Hello, world!')"
  }
});
console.log(JSON.stringify(prompt, null, 2));

// Read a resource
const resource = await client.readResource({
  uri: "got://quotes/random"
});
console.log("========================================")
console.log("Resource fetched");
console.log(JSON.stringify(resource, null, 2));

// Read a template resource
const templateResource = await client.readResource({
  uri: "person://properties/alexys"
});
console.log("========================================")
console.log("Template resource fetched");
console.log(JSON.stringify(templateResource, null, 2));

// Call a tool
const tool = await client.callTool({
  name: tools.tools[1].name,
  arguments: {
    numbers: [1, 2, 3, 4, 5]
  }
});
console.log("========================================")
console.log("Tool result");
console.log(JSON.stringify(tool, null, 2));
