# ppwdump/main.py


import os
from .config import OLLAMA_MODEL, OLLAMA_BASE_URL, OLLAMA_NUM_CTX, USE_VISION, ANONYMIZED_TELEMETRY, ENABLE_MEMORY

#Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = ANONYMIZED_TELEMETRY

import asyncio
from langchain_ollama import ChatOllama
from .browser_utils import run_initial_task
from .code_generation import generate_playwright_code, generate_pytest_playwright_code

async def main():
    # Step 1: Ask the user for the initial task
    task = input("Enter the initial task: ")

    # Step 2: Use Ollama as the language model
    llm = ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        num_ctx=OLLAMA_NUM_CTX
        )
    use_vision = USE_VISION
    enable_memory = ENABLE_MEMORY

    # Step 3: Run the initial task and get the history list
    history_list = await run_initial_task(task, llm, use_vision, enable_memory)
    print("\n\n", history_list.model_actions())

    # Step 4: Generate Playwright code based on the history list
    playwright_code = generate_playwright_code(history_list)
    playwright_code_content = playwright_code.content
    print(playwright_code_content)
    pytest_playwright_code = generate_pytest_playwright_code(playwright_code_content)
    print(pytest_playwright_code.content)

if __name__ == "__main__":
    asyncio.run(main())