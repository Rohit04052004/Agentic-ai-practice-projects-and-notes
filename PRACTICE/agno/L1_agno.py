# !pip install -U agno
# !pip install python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_api_key


from agno.agent import Agent
from agno.models.openai import OpenAIChat
# Create an Agno agent for Q&A
qa_agent = Agent(
    model=OpenAIChat(id="gpt-3.5-turbo"),  #"gpt-4o-mini"
    description="Agno Q&A agent",
    markdown=False
)

# Ask the agent a question and stream the response
qa_agent.print_response("What is the currency of Japan?", stream=True)
