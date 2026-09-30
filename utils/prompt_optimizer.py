def optimize_prompt(user_request, role, tone, output_format, audience, constraints):
    audience_text = audience.strip() if audience.strip() else "a general audience"
    constraints_text = constraints.strip() if constraints.strip() else "Be accurate, clear, relevant, and avoid unnecessary information."

    return f"""You are a {role}.

TASK:
{user_request.strip()}

CONTEXT AND AUDIENCE:
The response is intended for {audience_text}.

TONE:
Use a {tone.lower()} tone.

INSTRUCTIONS:
1. Understand the user's intent before answering.
2. Include only information relevant to the task.
3. State assumptions when important information is missing.
4. Follow the requested output format exactly.
5. {constraints_text}

OUTPUT FORMAT:
{output_format}

QUALITY CHECK:
Before finalizing, check clarity, correctness, completeness, and consistency with the requested tone and format.
"""

def generate_demo_response(optimized_prompt, original_request, output_format, tone):
    task = original_request.lower()
    if "email" in task or output_format == "Email":
        return """Subject: Leave Request

Dear Manager,

I would like to request two days of leave due to a personal commitment. I will complete or hand over any urgent work before my leave and remain available for critical matters if required.

Please let me know if the requested dates can be approved.

Thank you for your consideration.

Best regards,
[Your Name]"""
    if "explain" in task or "learn" in task:
        return """A clear way to approach this is:
1. Identify the main concept.
2. Break it into smaller ideas.
3. Explain each idea with a simple example.
4. Summarize the key points at the end.

This structure improves clarity and makes the answer easier to understand."""
    if "code" in task or output_format == "Code":
        return """# Example Python structure
def solve():
    # Read input
    # Process the problem
    # Produce the required output
    pass

if __name__ == "__main__":
    solve()
"""
    return """The optimized prompt provides a clear role, task, audience, tone, constraints, output format, and quality checks. In a production version, this optimized prompt would be sent to a Generative AI model such as an LLM API to produce the final response."""
