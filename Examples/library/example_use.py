# example_use.py

import asyncio
from ppwdump import generate_history_list, generate_playwright_code, generate_pytest_playwright_code

async def main():
    use_chat_ollama = True
    my_browser_model = "msm32"
    my_code_model = "msm"
    ollama_host  = "127.0.0.1:11434"
    headless = False
    api_key = "your_api_key_here"  # Add your API key here
    task = "Goto https://formy-project.herokuapp.com/form and fill out the elements of the form with sample data including radio buttons and checkboxes then submit the form. Make sure all entries make sense as if made by a human applicant."
    
    history_list = await generate_history_list(task, use_chat_ollama=use_chat_ollama, model=my_browser_model, ollama_host=ollama_host, headless=headless, api_key=api_key)
    
    playwright_code_content = await generate_playwright_code(history_list, use_chat_ollama=use_chat_ollama, model=my_code_model, ollama_host=ollama_host)
    print("Playwright Code:\n")
    print(playwright_code_content)

    pytest_playwright_code = await generate_pytest_playwright_code(playwright_code_content, use_chat_ollama=use_chat_ollama, model=my_code_model, ollama_host=ollama_host)
    print("\nPytest Playwright Code:\n")
    print(pytest_playwright_code)

if __name__ == "__main__":
    asyncio.run(main())