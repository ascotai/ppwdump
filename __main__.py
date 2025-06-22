# ppwdump/__main__.py

import asyncio
import argparse
from .code_generation import generate_playwright_code, generate_pytest_playwright_code, generate_history_list  # Update import


async def main():
    if args.task:
        task = args.task
    else:
        task = input("Enter the initial task: ")

    history_list = await generate_history_list(task, headless=args.headless)  # Pass the headless argument here
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
    parser.add_argument('--task', type=str, help='Initial task to execute')
    parser.add_argument('--headless', action='store_true', help='Run the browser in headless mode')  # Add the new argument

    args = parser.parse_args()

    asyncio.run(main())