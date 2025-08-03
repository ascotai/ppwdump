# ppwdump/code_generation.py
from .config import OPENAI_BASE_URL, BROWSER_MODEL_PROVIDER, CODE_MODEL_PROVIDER, BROWSER_MODEL, CODE_MODEL, OLLAMA_HOST, USE_VISION, ANONYMIZED_TELEMETRY, HEADLESS, GOOGLE_API_KEY, OPENAI_API_KEY
import os
#os.environ["BROWSER_USE_LOGGING_LEVEL"]="debug"
os.environ["ANONYMIZED_TELEMETRY"] = str(ANONYMIZED_TELEMETRY)
from browser_use.llm import ChatOpenAI, ChatOllama, ChatGoogle  # Import both LLM classes
from browser_use import Agent, BrowserProfile, BrowserSession
from browser_use.llm.messages import UserMessage, SystemMessage  # Import necessary message classes

def create_llm(model_provider="openai", model=BROWSER_MODEL_PROVIDER, ollama_host=OLLAMA_HOST, google_api_key=GOOGLE_API_KEY,openai_api_key=OPENAI_API_KEY, openai_base_url=OPENAI_BASE_URL):
    if (model_provider=="ollama"):
        return ChatOllama(
            model=model,
            host=ollama_host
        )
    elif (model_provider=="google"):
        return ChatGoogle(
            model=model,
            api_key=google_api_key        
        )
    else:
        return ChatOpenAI(
            model=model,
            api_key=openai_api_key,
            base_url=openai_base_url
        )

async def generate_history_list(task, headless=HEADLESS, use_vision=USE_VISION, model_provider=BROWSER_MODEL_PROVIDER, model=BROWSER_MODEL, ollama_host=OLLAMA_HOST, google_api_key=GOOGLE_API_KEY, openai_api_key=OPENAI_API_KEY, openai_base_url=OPENAI_BASE_URL):
    browser_profile = BrowserProfile(
        headless=headless,
        disable_security=False,
        user_data_dir=None
    )

    browser_session = BrowserSession(
        browser_profile=browser_profile,
    )

    llm = create_llm(model_provider, model, ollama_host, google_api_key, openai_api_key, openai_base_url)

    agent = Agent(
        task=task,
        llm=llm,
        use_vision=use_vision,
        max_history_items=250,
        llm_timeout=600,
		step_timeout=600,
        browser_session=browser_session,
        #extend_system_message="""<additional_browser_rules>- Always use a tool to select an option from a dropdown menu (select menu).</additional_browser_rules>"""
        extend_system_message="""<additional_browser_rules>- Always use the 'select_dropdown_option' tool to select an option from a dropdown menu by the exact text of the option. First verify available options using 'get_dropdown_options' if needed.</additional_browser_rules>"""
    )

    history_list = await agent.run()
    await browser_session.close()
    return history_list

async def generate_playwright_code(history_list, model_provider=CODE_MODEL_PROVIDER, model=CODE_MODEL, ollama_host=OLLAMA_HOST, google_api_key=GOOGLE_API_KEY, openai_api_key=OPENAI_API_KEY, openai_base_url=OPENAI_BASE_URL):
    prompt = f"""
-for each json element of the array the first item represent a python playwright command action the interacted element represent the element to be acted on for example this:
[
  {{
    "go_to_url": {{
      "url": "https://www.ecosia.org",
      "new_tab": false
    }},
    "interacted_element": null
  }},
  {{
    "input_text": {{
      "index": 1,
      "text": "Giant Panda"
    }},
    "interacted_element": DOMHistoryElement(
      tag_name='input',
      xpath='html/body/div[1]/div/div[2]/header/div/form/div/div/div/input',
      highlight_index=1,
      entire_parent_branch_path=[
        'div', 'div', 'div', 'header', 'div', 'form', 'div', 'div', 'div', 'input'
      ],
      attributes={{
        'placeholder': 'Search the web...',
        'aria-label': 'Search the web',
        'role': 'combobox',
        'aria-autocomplete': 'both',
        'aria-controls': 'search-form-suggestion-list',
        'aria-expanded': 'false',
        'aria-haspopup': 'listbox',
        'type': 'search',
        'name': 'q',
        'autocomplete': 'off',
        'autocapitalize': 'off',
        'autocorrect': 'off',
        'spellcheck': 'false',
        'required': 'required',
        'data-test-id': 'search-form-input',
        'value': '',
        'class': 'search-form__input',
        'data-v-bc2ad95e': ''
      }},
      shadow_root=false,
      css_selector='html > body > div:nth-of-type(1) > div > div:nth-of-type(2) > header > div > form > div > div > div > input.search-form__input[placeholder="Search the web..."][aria-label="Search the web"][role="combobox"][type="search"][name="q"][autocomplete="off"][required="required"]',
      page_coordinates=null,
      viewport_coordinates=null,
      viewport_info=null
    )
  }},
  {{
    "click_element_by_index": {{
      "index": 3
    }},
    "interacted_element": DOMHistoryElement(
      tag_name='button',
      xpath='html/body/div[1]/div/div[2]/header/div/form/div/div/button',
      highlight_index=3,
      entire_parent_branch_path=[
        'div', 'div', 'div', 'header', 'div', 'form', 'div', 'div', 'button'
      ],
      attributes={{
        'type': 'submit',
        'icon-class': 'searchf-form__submit-icon',
        'aria-label': 'Search',
        'data-test-id': 'search-form-submit',
        'variant': 'bare',
        'class': 'button search-form__submit button base-button base-button--variant-bare base-button--size-m base-button--elevation-0 base-button--text-size-m search-form__submit button button--icon-position-start button-icon',
        'data-v-ef413702': '',
        'data-v-bc2ad95e': ''
      }},
      shadow_root=false,
      css_selector='html > body > div:nth-of-type(1) > div > div:nth-of-type(2) > header > div > form > div > div > button.button.search-form__submit.button.base-button.base-button--variant-bare.base-button--size-m.base-button--elevation-0.base-button--text-size-m.search-form__submit.button.button--icon-position-start.button-icon[type="submit"][aria-label="Search"]',
      page_coordinates=null,
      viewport_coordinates=null,
      viewport_info=null
    )
  }},
  {{
    "click_element_by_index": {{
      "index": 41
    }},
    "interacted_element": DOMHistoryElement(
      tag_name='a',
      xpath='html/body/div[1]/div/main/div/section/div[1]/div[3]/div[3]/article/div/div[1]/div[1]/div/div[2]/a',
      highlight_index=41,
      entire_parent_branch_path=[
        'div', 'div', 'main', 'div', 'section', 'div', 'div', 'div', 'article', 'div', 'div', 'div', 'div', 'div', 'a'
      ],
      attributes={{
        'data-test-id': 'result-link',
        'tabindex': '-1',
        'href': 'https://en.wikipedia.org/wiki/Giant_panda',
        'target': '_self',
        'rel': 'noopener',
        'class': 'result__link result__source--ellipsis',
        'data-v-cba477c1': ''
      }},
      shadow_root=false,
      css_selector='html > body > div:nth-of-type(1) > div > main > div > section > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(3) > article > div > div:nth-of-type(1) > div:nth-of-type(1) > div > div:nth-of-type(2) > a.result__link.result__source--ellipsis[href="https://en.wikipedia.org/wiki/Giant_panda"][target="_self"]',
      page_coordinates=null,
      viewport_coordinates=null,
      viewport_info=null
    )
  }},
  {{
    "done": {{
      "text": "The task is complete. I have successfully navigated to the Giant Panda Wikipedia page.",
      "success": true,
      "files_to_display": []
    }},
    "interacted_element": null
  }}
]

-would give this: 


from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.ecosia.org')
    page.fill("input.search-form__input[placeholder='Search the web...'][aria-label='Search the web'][role='combobox'][type='search'][name='q'][autocomplete='off'][required='required']", 'Giant Panda')
    page.click("button.button.search-form__submit.button.base-button.base-button--variant-bare.base-button--size-m.base-button--elevation-0.base-button--text-size-m.search-form__submit.button.button--icon-position-start.button-icon[type='submit'][aria-label='Search']")
    page.click("a.result__link.result__source--ellipsis[href='https://en.wikipedia.org/wiki/Giant_panda'][target='_self']")
    browser.close()   
    
    
-give one command for each element in the array. If using attributes use multiple attributes if possible.
{history_list.model_actions()}
"""

    messages = [
        SystemMessage(content=(
            "You are a helpful assistant that converts json instructions into complete runnable python playwright code."
            "Make sure all output code is valid python playwright code. Do not output any javascript code."
            "This is very important: If there are one or more duplicate steps be sure to comment out any duplicate steps that appear after the original step."
            "Do not forget needed import statements at the the top of your code."
            "Use only from playwright.sync_api import sync_playwright in your code do not use async playwright."
            "Use ony browser = p.chromium.launch(headless=False) do not use headless=True."
            "When using page.goto() only pass in a url, do not pass in any other parameters."
            "Use CSS selector locators if possible instead of XPath locators."
            "You always return just python code. You do not need to explain anything, just return the code."
            "Do not output markdown i.e. ```python```."
            "Do not include any steps that writes to, reads from or opens local files."
        )),
        UserMessage(content=prompt),
    ]

    llm = create_llm(model_provider, model, ollama_host, google_api_key, openai_api_key, openai_base_url)

    response = await llm.ainvoke(messages)

    return response.completion

async def generate_pytest_playwright_code(playwright_code , model_provider=CODE_MODEL_PROVIDER, model=CODE_MODEL, ollama_host=OLLAMA_HOST, google_api_key=GOOGLE_API_KEY, openai_api_key=OPENAI_API_KEY, openai_base_url=OPENAI_BASE_URL):
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
        SystemMessage(content=(
            "You are a helpful assistant that converts python playwright code into pytest-playwright code. "
            "You always return just runnable pytest-playwright code. You do not need to explain anything, just return the code. "
            "Do not output markdown i.e. ```python```."
            "Do not include any steps that writes to, reads from or opens local files."
        )),
        UserMessage(content=prompt),
    ]

    llm = create_llm(model_provider, model, ollama_host, google_api_key, openai_api_key, openai_base_url)

    response = await llm.ainvoke(messages)

    return response.completion