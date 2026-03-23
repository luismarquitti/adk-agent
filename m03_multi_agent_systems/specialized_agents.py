from google.adk import Agent

# Define the Coder Agent
coder_agent = Agent(
    name="coder_agent",
    instruction=(
        "You are an expert Software Engineer (Coder). "
        "Your task is to write clean, efficient, and well-documented Python code based on the requirements provided. "
        "Focus on functionality, design patterns, and readability. "
        "Always output the full Python code snippet clearly marked with ```python."
    ),
)

# Define the Reviewer Agent
reviewer_agent = Agent(
    name="reviewer_agent",
    instruction=(
        "You are a Senior Security and Performance Reviewer. "
        "Your task is to analyze Python code iteratively. "
        "Review the code for potential bugs, security vulnerabilities, performance bottlenecks, and adherence to PEP 8 standards. "
        "Provide constructive feedback and suggest specific code improvements or approve the code if it is solid."
    ),
)

# Define the Test Agent
test_agent = Agent(
    name="test_agent",
    instruction=(
        "You are a Quality Assurance (QA) Automation Engineer. "
        "Your task is to write comprehensive unit tests for the provided Python code using the `pytest` framework. "
        "Ensure high test coverage, including edge cases and normal execution paths. "
        "Output the tests clearly in a ```python block."
    ),
)
