from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="openrouter/microsoft/mai-ds-r1:free"), # LiteLLM model string format
    name="amazon_listing_agent",
    instruction="You are a helpful assistant powered by openrouter.",
    # ... other agent parameters
)

