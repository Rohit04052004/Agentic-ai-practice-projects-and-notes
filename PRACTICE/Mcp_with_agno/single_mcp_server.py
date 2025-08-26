import asyncio
import os
from dotenv import load_dotenv
from agno.tools.mcp import MCPTools  
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

async def main():
    openai_key = os.getenv("OPENAI_API_KEY")

    # Attach MCP Calculator server as a tool
    # Create an agent with a single MCP tool for calculations
calculator_agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini", api_key=openai_key),
    
    tools=[
            MCPTools("python -m mcp_server_calculator")
        ],
        description="AI agent that can use MCP servers (like calculator).",
        markdown=True,        
        
    )

    # Ask the agent to perform a simple calculation
calculator_agent.print_response("What is the result of 15 * 9?", stream=True)

if __name__ == "__main__":
    asyncio.run(main())
