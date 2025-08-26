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
    # Create an agent with multiple MCP tools for calculation and Wikipedia search
multi_tool_agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini", api_key=openai_key),
    
    tools=[
            MCPTools("python -m mcp_server_calculator"),
            MCPTools("python -m mcp_wikipedia"),              
        ],
        description="AI agent that can calculate and also search Wikipedia using MCP servers.",
        markdown=True,        
        
    )

    # Ask the agent to perform a calculation and a Wikipedia search in the same query
multi_tool_agent.print_response("What is 30 * 15 and who is the founder of Wikipedia?", stream=True)

if __name__ == "__main__":
    asyncio.run(main())
