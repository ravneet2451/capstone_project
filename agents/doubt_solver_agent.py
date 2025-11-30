"""Doubt Solver Agent
Wraps a call to the LLM of your choice.
Replace the _call_llm method with a call to Gemini/OpenAI/your-provider.
"""




class DoubtSolverAgent:
def __init__(self, model_name=None):
self.model = model_name or "gemini-placeholder"


def _call_llm(self, prompt: str) -> str:
# Placeholder implementation: replace with real LLM SDK call
# Example: use google.generativeai or openai.ChatCompletion.create
return (
"(LLM placeholder) Here's a concise explanation of the chain rule:\n"
"If y = f(g(x)), then dy/dx = f'(g(x)) * g'(x).\nExample: y = (3x^2 + 2)^4. Let u = 3x^2+2, y = u^4. dy/du = 4u^3, du/dx=6x, so dy/dx=24x(3x^2+2)^3."
)


def answer_question(self, question: str) -> str:
prompt = f"Answer the following student question clearly and with a simple example:\n\n{question}"
return self._call_llm(prompt)
