# example_use.py

import asyncio
from ppwdump import generate_history_list, generate_playwright_code, generate_pytest_playwright_code

async def main():
    my_browser_model = "q25c"
    my_code_model = "msm"
    my_url  = "http://192.168.1.25:11434/v1"
    headless = False
    api_key = "your_api_key_here"  # Add your API key here
    task = "Goto https://formy-project.herokuapp.com/form and fill out the elements of the form with sample data including radio buttons and checkboxes then submit the form. Make sure all entries make sense as if made by a human applicant."
    
    history_list = await generate_history_list(task, model=my_browser_model, base_url=my_url, headless=headless, api_key=api_key)
    
    playwright_code_content = generate_playwright_code(history_list, model=my_code_model, base_url=my_url, api_key=api_key)
    print("Playwright Code:\n")
    print(playwright_code_content)

    pytest_playwright_code = generate_pytest_playwright_code(playwright_code_content, model=my_code_model, base_url=my_url, api_key=api_key)
    print("\nPytest Playwright Code:\n")
    print(pytest_playwright_code)

if __name__ == "__main__":
    asyncio.run(main())