# ppwdump/main.py

import asyncio
import os
import argparse
from .config import OLLAMA_MODEL, OLLAMA_BASE_URL, OLLAMA_NUM_CTX, USE_VISION, ANONYMIZED_TELEMETRY, ENABLE_MEMORY

# Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = ANONYMIZED_TELEMETRY

from browser_use import Agent, BrowserProfile, BrowserSession
from langchain_ollama import ChatOllama
from .code_generation import generate_playwright_code, generate_pytest_playwright_code

# Define the browser profile
browser_profile = BrowserProfile(
    headless=False,
    disable_security=False
    # Add other configurations as needed
)

# Define the browser session using the profile
browser_session = BrowserSession(
    browser_profile=browser_profile,
    # Add other configurations as needed
)

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
    agent = Agent(
        task=task,
        llm=llm,
        use_vision=use_vision,
        enable_memory=enable_memory,
        browser_session=browser_session  # Use the session instead of browser
    )

    history_list = await agent.run()  # Ensure this is awaited
    await browser_session.close()

    if args.no_out:
        pass  # Output nothing
    elif args.history or args.pytest:
        if args.history:
            print("\n\n", history_list.model_actions())
        if args.pytest:
            playwright_code_content = generate_playwright_code(history_list).content
            pytest_playwright_code = generate_pytest_playwright_code(playwright_code_content)
            print(pytest_playwright_code.content)
    elif args.all:
        playwright_code_content = generate_playwright_code(history_list).content
        pytest_playwright_code = generate_pytest_playwright_code(playwright_code_content)
        print("\n\n", history_list.model_actions())
        print(playwright_code_content)
        print(pytest_playwright_code.content)  
    else:  # Default behavior: output Python code
        playwright_code_content = generate_playwright_code(history_list).content
        print(playwright_code_content)

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Run the main task with optional outputs. Default behavior: output python code", prog='python -m ppwdump')
    parser.add_argument('--no-out', action='store_true', help='Output nothing')
    parser.add_argument('--pytest', action='store_true', help='Output only pytest code')
    parser.add_argument('--history', action='store_true', help='Output only history list')
    parser.add_argument('--all', action='store_true', help='Output history list, python code and pytest code')

    args = parser.parse_args()

    asyncio.run(main())