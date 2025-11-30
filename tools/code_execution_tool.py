"""Code Execution Tool
Small helper to execute short Python snippets safely (sandboxed). Use with caution.
"""
import subprocess
import sys
import tempfile
from typing import Tuple




class CodeExecutionTool:
def run_python(self, code: str, timeout: int = 5) -> Tuple[int, str, str]:
"""Run code in a temporary file using the system Python. Returns (exit_code, stdout, stderr).
This is a simple implementation and not fully secure — for production use a sandboxed runtime.
"""
with tempfile.NamedTemporaryFile(mode="w", suffix=".py", d
