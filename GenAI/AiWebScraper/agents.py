from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import litellm

# Load environment variables
load_dotenv()

# Configure litellm
os.environ["OPENAI_API_KEY"] = os.getenv("GOOGLE_API_KEY")
litellm.api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the model using litellm wrapped in ChatOpenAI
llm = ChatOpenAI(
    model_name="gemini/gemini-pro",  # Specify the model with provider prefix
    temperature=0.5,
    openai_api_key=os.getenv("GOOGLE_API_KEY"),
    max_tokens=1000
)

# Create agents with the configured LLM
news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)