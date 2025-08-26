# /opt/mcp-server/server.py

import logging
import os
import uvicorn
from mcp.server.fastmcp import FastMCP  # ✅ correct import

logging.basicConfig(level=logging.INFO, format='[%(levelname)s]: %(message)s')
logger = logging.getLogger(__name__)

# Create an MCP server instance for math operations
math_mcp_server = FastMCP("Math")

@math_mcp_server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))  # avoid 8000 if something else is using it
    logger.info(f"🚀 Starting Streamable-HTTP MCP server on http://{host}:{port}/mcp")
    # This returns an ASGI app that serves the MCP endpoint at /mcp
    # Get the ASGI app from the MCP server
app = math_mcp_server.streamable_http_app()
    uvicorn.run(app, host=host, port=port)
