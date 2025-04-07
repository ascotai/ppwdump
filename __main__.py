# ppwdump/main.py


import os
from .config import LLM_MODEL, LLM_BASE_URL, LLM_NUM_CTX,USE_VISION, ANONYMIZED_TELEMETRY

#Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = ANONYMIZED_TELEMETRY

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.agent.views import AgentHistoryList
import asyncio
from langchain_ollama import ChatOllama
from .browser_utils import run_initial_task
from .code_generation import generate_playwright_code, generate_pytest_playwright_code

async def main():
    # Step 1: Ask the user for the initial task
    task = input("Enter the initial task: ")

    # Step 2: Use Ollama as the language model
    llm = ChatOllama(
        model=LLM_MODEL,
        base_url=LLM_BASE_URL,
        num_ctx = LLM_NUM_CTX
        )
    use_vision = USE_VISION

    # Step 3: Run the initial task and get the history list
    history_list = await run_initial_task(task, llm, use_vision)
    print("\n\n", history_list.model_actions())

    # Step 4: Generate Playwright code based on the history list
    playwright_code = generate_playwright_code(history_list)
    playwright_code_content = playwright_code.content
    print(playwright_code_content)
    pytest_playwright_code = generate_pytest_playwright_code(playwright_code_content)
    print(pytest_playwright_code.content)

if __name__ == "__main__":
    asyncio.run(main())