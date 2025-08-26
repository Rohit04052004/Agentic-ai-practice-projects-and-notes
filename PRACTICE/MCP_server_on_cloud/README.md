# MCP Server on Cloud

This project demonstrates how to create and interact with a custom MCP (Machine Communication Protocol) server deployed on the cloud. It includes a server with mathematical tools and a client that uses `langgraph` to process mathematical queries.

## Files

- `custom_server.py`: This script sets up a `FastMCP` server with tools for basic arithmetic operations like addition and multiplication. It's configured to run as a streamable HTTP server.
- `mcp_client_langgraph.py`: This script shows how to connect to the MCP server, retrieve its tools, and use them within a `langgraph` workflow. It binds the tools to a `ChatOpenAI` model to answer mathematical questions.

## Author

- Rohit Chigatapu