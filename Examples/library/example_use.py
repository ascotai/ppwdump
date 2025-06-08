# example_use.py

import asyncio
from ppwdump import generate_history_list, generate_playwright_code

async def main():
    task = "Goto https://www.ecosia.com/. Put Giant Panda in the search box. Click on the search button. Click on the link for the Giant Panda Wikipedia page. Finish."
    history_list = await generate_history_list(task)
    playwright_code_content = generate_playwright_code(history_list).content
    print(playwright_code_content)

if __name__ == "__main__":
    asyncio.run(main())