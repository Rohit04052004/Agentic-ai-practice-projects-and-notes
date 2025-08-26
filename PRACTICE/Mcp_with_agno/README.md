
# MCP with Agno

This project demonstrates how to use the `agno` library to create AI agents that can interact with MCP (Machine Communication Protocol) servers. It includes examples of single, multiple, and custom MCP server integrations.

## Files

- `custom_mcp_server.py`: Defines a custom `FastMCP` server with mathematical tools like `add`, `multiply`, `divide`, `square_root`, and `factorial`.
- `multipl_mcp_custom.py`: Shows how to create an `agno` agent that connects to multiple MCP servers, including a calculator, Wikipedia, and the custom math server defined in `custom_mcp_server.py`.
- `multipl_mcp_server.py`: An example of an `agno` agent that uses both a calculator and a Wikipedia MCP server to answer queries.
- `single_mcp_server.py`: A simple example of an `agno` agent that connects to a single MCP calculator server.
- `4.py`: Demonstrates how to connect an `agno` agent to a remote MCP server using a URL.

## Author

- Rohit Chigatapu