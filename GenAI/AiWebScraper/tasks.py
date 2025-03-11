from crewai import Task
from tools import tool
from agents import news_researcher,news_writer
import logging

logging.basicConfig(
    filename="visited_urls.log",  # Log file name
    level=logging.INFO,  # Log only important information
    format="%(asctime)s - Visited URL: %(message)s",  # Log timestamp and URL
)

def log_visited_url(url):
    """Logs URLs discovered during research."""
    logging.info(url)
    news_researcher.log_url(url)

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=news_researcher,
)
def fetch_research_urls():
    """Fetch URLs from the agent's research process."""
    urls = news_researcher.get_logged_urls()  # Get dynamically logged URLs
    if not urls:
        print("No URLs found during research.")
    else:
        for url in urls:
            log_visited_url(url)  # Log each found URL
visited_urls = news_researcher.get_sources() 
for url in visited_urls:
    log_visited_url(url)

fetch_research_urls()

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)