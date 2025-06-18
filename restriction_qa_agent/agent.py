from google.adk.agents import SequentialAgent

from .sub_agents.triage_agent import triage_agent
from .sub_agents.compliance_agent import compliance_agent
from .sub_agents.report_agent import report_agent


root_agent = SequentialAgent(
    name="restriction_qa_agent",
    sub_agents=[triage_agent, compliance_agent, report_agent],
    description="A pipeline agent that triages product information, checks compliance, and generates a structured report on product restrictions.",
)
