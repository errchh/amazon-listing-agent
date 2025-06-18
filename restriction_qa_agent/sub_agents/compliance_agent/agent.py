import os
from ...utils import read_file
from .prompt import compliance_prompt

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm


# Load the policy documents
amazon_policy = read_file('../../../../docs/amazon_policy.md')
fda_restriction = read_file('../../../../docs/fda_restriction.md')
jurisdictional_restriction = read_file('../../../../docs/jurisdictional_restriction.md')


model = LiteLlm(
    model="openrouter/microsoft/mai-ds-r1:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


compliance_agent = LlmAgent(
    name="compliance_agent",
    model=model,
    instruction=compliance_prompt,
    description="Analyze product information against a specific set of provided policies to determine if the product is allowed for sale.",
    output_key="compliance_status",
)
