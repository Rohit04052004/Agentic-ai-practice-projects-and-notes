
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()


async def main():
    # Get keys from environment variables
    openai_key = os.getenv("OPENAI_API_KEY")
    owm_key = os.getenv("OWM_API_KEY")

    if not openai_key:
        raise ValueError("OPENAI_API_KEY not found in .env or environment variables.")
    if not owm_key:
        raise ValueError("OWM_API_KEY not found in .env or environment variables.")


    # Set up the multi-server MCP client to connect to weather and calculator tools
mcp_client = MultiServerMCPClient(
        {
            "weather": {
                "transport": "stdio",
                "command": "E:/langraph_mcp-demo/mcp-openweather/mcp-weather.exe",
                "args": [],
                "env": {"OWM_API_KEY": owm_key}  
            },
            "calculator": {
                "transport": "stdio",
                "command": "python",
                "args": ["-m", "mcp_server_calculator"]
            }
            
        }
    )
    
    # Get the tools from the MCP client
available_tools = await mcp_client.get_tools()  
    
    # Initialize the language model
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)    
    

    def call_model(state: MessagesState):
        response = llm.bind_tools(available_tools).invoke(state["messages"])
        return {"messages": response}
        
        
    # Building the LangGraph workflow 
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_node("tools", ToolNode(available_tools))
    
    builder.add_edge(START, "call_model")
    
    builder.add_conditional_edges("call_model", tools_condition)
    builder.add_edge("tools", "call_model")
    
    # building the graph
    # Compile the graph into a runnable workflow
workflow = builder.compile()

    print("\n--- Weather Query ---")
    
    while True:
        user_question = input("\nAsk me anything (weather or calculation) → ")
        if user_question.strip().lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        print("\n--- Agent is thinking... ---")
        # Invoke the workflow with the user's question
final_result = await workflow.ainvoke({"messages": user_question})
        print("\n--- Answer ---")
        print(final_result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())