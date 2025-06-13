# example_use.py

import asyncio
from ppwdump import generate_history_list, generate_playwright_code, generate_pytest_playwright_code

async def main():
    my_model = "msm"
    my_ollama_url  = "http://127.0.0.1:11434"
    headless = False
    task = "Goto https://formy-project.herokuapp.com/form and fill out all elements of the form with sample data including all radio buttons and checkboxes then submit the form."
    
    history_list = await generate_history_list(task, model=my_model, base_url=my_ollama_url, headless=headless)

    playwright_code_content = generate_playwright_code(history_list, model=my_model, base_url=my_ollama_url).content
    print("Playwright Code:\n")
    print(playwright_code_content)

    pytest_playwright_code = generate_pytest_playwright_code(playwright_code_content, model=my_model, base_url=my_ollama_url)
    print("\nPytest Playwright Code:\n")
    print(pytest_playwright_code.content)

if __name__ == "__main__":
    asyncio.run(main())
