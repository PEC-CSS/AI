from crewai import Agent
from tools import tool
from crewai import Tool
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import litellm
import logging

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

# Configure logging
logging.basicConfig(
    filename="visited_urls.log",  # Log file name
    level=logging.INFO,  # Log only important information
    format="%(asctime)s - Visited URL: %(message)s",  # Log timestamp and URL
)

# List to store visited URLs
visited_urls = []

# Function to log visited URLs
def log_url(url):
    visited_urls.append(url)
    logging.info(url)

# Create a tool to log URLs
url_logger = Tool(
    name="URL Logger",
    description="Logs the URL of visited sources.",
    function=log_url
)

# Custom Research Agent with URL Logging
class ResearchAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.visited_urls = []

    def log_url(self, url):
        """Logs a visited URL."""
        self.visited_urls.append(url)
        log_url(url)

    def get_logged_urls(self):
        """Returns all visited URLs."""
        return self.visited_urls

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
    tools=[tool , url_logger],  # Add URL logging tool
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