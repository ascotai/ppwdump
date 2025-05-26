# ppwdump/browser_utils.py

import os
from .config import ANONYMIZED_TELEMETRY

# Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = ANONYMIZED_TELEMETRY

from browser_use import Agent, BrowserProfile, BrowserSession


async def run_initial_task(task, llm, use_vision, enable_memory):
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

    

    agent = Agent(
        task=task,
        llm=llm,
        use_vision=use_vision,
        enable_memory=enable_memory,
        browser_session=browser_session  # Use the session instead of browser
    )

    result = await agent.run()  # Ensure this is awaited
    await browser_session.close()

    return result