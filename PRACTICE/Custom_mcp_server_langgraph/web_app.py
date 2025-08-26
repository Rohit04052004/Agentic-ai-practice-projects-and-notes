import asyncio
import streamlit as st
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

async def run_mcp_query(user_input):
    # Get keys from environment variables
    openai_key = os.getenv("OPENAI_API_KEY")
    
    # Initialize the OpenAI model (using a free tier model)
    llm_model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)

    # Connect to the MCP server via HTTP
    mcp_client = MultiServerMCPClient(
        {
            "math": {
                "transport": "streamable_http",
                "url": "http://127.0.0.1:8000/mcp"  # URL of the MCP server
            }
        }
    )

    math_tools = await mcp_client.get_tools()
    model_with_tools = llm_model.bind_tools(math_tools)
    tool_node = ToolNode(math_tools)

    def should_continue(state: MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return END

    async def call_model(state: MessagesState):
        messages = state["messages"]
        response = await model_with_tools.ainvoke(messages)
        return {"messages": [response]}

    # LangGraph pipeline
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_node("tools", tool_node)
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", should_continue)
    builder.add_edge("tools", "call_model")

    # Compile the graph into a runnable workflow
    workflow = builder.compile()
    final_result = await workflow.ainvoke({"messages": [{"role": "user", "content": user_input}]})

    # Extract the content from the last message
    last_message_content = final_result["messages"][-1].content
    return last_msg if isinstance(last_msg, str) else str(last_msg)


def main():
    st.set_page_config(page_title="MCP Math Chat", page_icon="🧮")
    st.title("🧮 MCP Math Chat (Streamlit)")

    user_input = st.text_input("Ask me something math-related:")
    if st.button("Send") and user_input.strip():
        with st.spinner("Thinking..."):
            answer = asyncio.run(run_mcp_query(user_input))
            st.success(answer)


if __name__ == "__main__":
    main()
