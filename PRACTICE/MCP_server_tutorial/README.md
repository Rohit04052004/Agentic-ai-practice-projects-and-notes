
# MCP Server Tutorial

This project demonstrates how to build a conversational agent that can interact with multiple MCP (Machine Communication Protocol) servers for different tools. The agent can answer questions related to weather and perform calculations.

## Files

- `1.py`: This script sets up a `MultiServerMCPClient` to connect to two separate MCP servers: one for weather information and another for calculations. It uses `langgraph` to create a workflow that allows a `ChatOpenAI` model to use these tools to answer user queries in a conversational loop.

## Author

- Rohit Chigatapu
