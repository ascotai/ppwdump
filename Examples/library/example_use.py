# example_use.py

import asyncio
from ppwdump import generate_history_list, generate_playwright_code, generate_pytest_playwright_code

async def main():
    model_provider = "ollama"
    my_browser_model = "msm32"
    my_code_model = "msm32"
    ollama_host  = "127.0.0.1:11434"
    headless = False
    task = "Goto https://www.ecosia.org. Put Giant Panda in the search box. Click on the search button. Click on the link for the Giant Panda Wikipedia page. Finish."
    
    history_list = await generate_history_list(task, model_provider=model_provider, model=my_browser_model, ollama_host=ollama_host, headless=headless)
    
    playwright_code_content = await generate_playwright_code(history_list, model_provider=model_provider, model=my_code_model, ollama_host=ollama_host)
    print("Playwright Code:\n")
    print(playwright_code_content)

    pytest_playwright_code = await generate_pytest_playwright_code(playwright_code_content, model_provider=model_provider, model=my_code_model, ollama_host=ollama_host)
    print("\nPytest Playwright Code:\n")
    print(pytest_playwright_code)

if __name__ == "__main__":
    asyncio.run(main())