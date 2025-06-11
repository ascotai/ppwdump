# ppwdump/code_generation.py

from langchain_ollama import ChatOllama
from .config import OLLAMA_MODEL, OLLAMA_BASE_URL, OLLAMA_NUM_CTX



def generate_playwright_code(history_list,model=OLLAMA_MODEL,base_url=OLLAMA_BASE_URL,num_ctx=OLLAMA_NUM_CTX):
    # Create a new prompt based on the history list
    prompt = f"""
    for each json element of the array the first item represent a python playwright command action the interacted element represent the element to be acted on for example this   ```json
    {{
      "click_element": {{
        "index": 36
      }},
      "interacted_element": {{
        "tag_name": "a",
        "xpath": 
    "html/body/div[3]/div/div[12]/div[4]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/span/a",
        "highlight_index": 36,
        "entire_parent_branch_path": ["div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", 
    "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "div", "span", "a"],
        "attributes": {{
          "jsname": "UWckNb",
          "href": "https://en.wikipedia.org/wiki/Giant_panda",
          "data-ved": "2ahUKEwj-1euBzfiLAxXyJDQIHTGvDEwQFnoECEgQAQ",
          "ping": "/url?sa=t&source=web&rct=j&opi=89978449&url=https://en.wikipedia.org/wiki/Giant_panda&ved=2ahUKEwj-1euBzfiLAxXyJDQIHTGvDEwQFnoECEgQAQ"
        }},
        "shadow_root": false,
        "css_selector": "html > body > div:nth-of-type(3) > div > div:nth-of-type(12) > div:nth-of-type(4) > div > div > div:nth-of-type(2) > div > div > div > div > div > 
    div > div > div > div > div > div > div > div > div > div:nth-of-type(3) > div > div > div > div > div > div > div > div > div > div > span > 
    a[href=\"https://en.wikipedia.org/wiki/Giant_panda\"]",
        "page_coordinates": null,
        "viewport_coordinates": null,
        "viewport_info": null
      }}
    }}
    ``` would give this page.click("a[href='https://en.wikipedia.org/wiki/Giant_panda']") give one command for each element in the array. If using attributes use multiple attributes if possible.

    {history_list.model_actions()}
    """
    messages = [
    (
        "system",
        "You are a helpful assistant that converts json instructions into runnable python playwright code. You always return just python code. You do not need to explain anything, just return the code.",
    ),
    ("human", prompt),
]
    # Use ChatOllama to generate Playwright code based on the prompt
    llm = ChatOllama(
        model=model,
        base_url=base_url,
        num_ctx=num_ctx
    )

    response = llm.invoke(messages)  # Blocking call
    return response

def generate_pytest_playwright_code(playwright_code,model=OLLAMA_MODEL,base_url=OLLAMA_BASE_URL,num_ctx=OLLAMA_NUM_CTX):

    prompt = f""" convert the code below to pytest playwright include page objects tests and conftest.py. If it looks like a navigation occured make sure to return the code for a new page object for the visited page. Add variables for each locator in the page objects, you can define these locators in __init__ and then use them within the methods.


for example this code:

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False) # Modified line
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" # Modified line
    )
    page = context.new_page()

    # Navigate to Google
    page.goto('https://www.google.com')

    # Input text "Giant Pandas" into the search bar
    page.fill('textarea[title="Search"]', 'Giant Pandas')

    # Click the Google Search button
    page.click('input[name="btnK"][type="submit"]')

    # Click on the link for the Giant Panda Wikipedia Page
    page.click("a[href='https://en.wikipedia.org/wiki/Giant_panda']")

    # Close the browser (optional, if you want to close it after the actions)
    browser.close()


would produce this output:

# pages/google_search.py

from playwright.sync_api import Page

class GoogleSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_google(self):
        self.page.goto('https://www.google.com')

    def input_search_text(self, text: str):
        self.page.fill('textarea[title="Search"]', text)

    def click_search_button(self):
        self.page.click('input[name="btnK"][type="submit"]')

    


# pages/google_results.py

from playwright.sync_api import Page

class GoogleResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_wikipedia_link(self):
        self.page.click("a[href='https://en.wikipedia.org/wiki/Giant_panda']")


# tests/conftest.py

import pytest
from playwright.sync_api import sync_playwright
from pages.google_search import GoogleSearchPage
from pages.google_results import GoogleResultsPage

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def google_search_page(page):
    return GoogleSearchPage(page)

@pytest.fixture
def google_results_page(page):
    return GoogleResultsPage(page)


# tests/test_google_search.py

import pytest

def test_google_search(google_search_page, google_results_page):
    google_search_page.navigate_to_google()
    google_search_page.input_search_text('Giant Pandas')
    google_search_page.click_search_button()
    google_results_page.click_wikipedia_link()
    # Add assertions here if needed




Now convert this code as in the example:


{playwright_code}


"""



    messages = [
    (
        "system",
        "You are a helpful assistant that converts python playwright code into pytest-playwright code. You always return just runnable pytest-playwright code. You do not need to explain anything, just return the code.",
    ),
    ("human", prompt),
    ]


    # Use ChatOllama to generate Playwright code based on the prompt
    llm = ChatOllama(
        model=model,
        base_url=base_url,
        num_ctx=num_ctx 
    )

    response = llm.invoke(messages)  # Blocking call
    return response