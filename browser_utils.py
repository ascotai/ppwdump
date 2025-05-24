# ppwdump/browser_utils.py

import os
from .config import ANONYMIZED_TELEMETRY

# Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = ANONYMIZED_TELEMETRY

from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.agent.views import AgentHistoryList
from langchain_ollama import ChatOllama





async def run_initial_task(task, llm, use_vision, enable_memory) -> AgentHistoryList:
    
    browser = Browser(
    config=BrowserConfig(
        #chrome_instance_path='/usr/bin/google-chrome',
    )
)
    agent = Agent(
        browser=browser,
        task=task,
        llm=llm,
        use_vision=use_vision,
        enable_memory=enable_memory

    )

    result = await agent.run()  # Ensure this is awaited
    await browser.close()

    return result