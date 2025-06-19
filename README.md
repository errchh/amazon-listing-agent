# Amazon Restricted Product Screening Agent

This project implements an AI-driven agent designed for automated screening of product listings against Amazon's restricted product policies. The system provides a comprehensive assessment framework, encompassing:

-   **Information Sufficiency Analysis:** Evaluates the completeness and adequacy of provided product data for accurate restriction compliance determination.
-   **Policy Violation Identification:** Identifies potential breaches of Amazon's product restriction guidelines.
-   **Decision Rationale Generation:** Furnishes a concise and clear justification for each screening outcome.
-   **Structured Data Output:** Generates machine-readable, JSON-formatted results to facilitate integration with downstream automated processes.
-   **Human-in-the-Loop Integration:** Flags listings requiring manual review with concise reasoning, optimising human resource allocation with minimal needs for exhaustive manual checking.

This agent enhances the efficiency and accuracy of compliance operations, enabling proactive adherence to Amazon's dynamic regulatory landscape.

## Setup and Usage

To set up and run the agent, follow these steps:

1.  **Install Dependencies:** Utilise `uv` to synchronise project dependencies.
    ```bash
    uv sync
    ```
2.  **Activate Virtual Environment** 
    ```bash
    source .venv/bin/activate
    ```
3.  **Launch Dev UI Web Interface** 
    ```bash
    adk web
