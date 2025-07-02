# ppwdump

## Description

`ppwdump` turns a prompt into runnable python playwright code and pytest playwright code. It uses Playwright, and Browser-use. This project leverages the power of these libraries to interact with web browsers and generate code for various purposes. `ppwdump` should now work with OpenAI compatible providers, not just Ollama.

https://github.com/user-attachments/assets/566c2711-c3b7-4a5c-8bdc-92557c6b57a9

## Installation Using Virtual Environment

For a more isolated environment, we recommend using a Python virtual environment. If you are on macOS, follow the instructions in the [Python_Venv_Install.md](Python_Venv_Install.md) file to create and activate a virtual environment using `uv` and then install the dependencies.

## Requirements

To run this project, you need to have the following dependencies installed:

```plaintext
browser-use
```

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

Additionally, you need to install Playwright's browser binaries by running:

```bash
playwright install
```

## Usage

1. **Run the Main Script**

   The main entry point of the project is `__main__.py`. You can run it directly using Python:

   ```bash
   cd ../
   python -m ppwdump
   ```

2. **Customize Configuration**

   The configuration for the project is located in `config.py`. You can modify the following settings:

   - `ANONYMIZED_TELEMETRY`: Whether to enable anonymized telemetry.
   - `BROWSER_MODEL`: The language model to use for browser interactions.
   - `CODE_MODEL`: The language model to use for code generation.
   - `USE_CHAT_OLLAMA`: Use ChatOllama for better performance with Ollama when True, or set to False to use an OpenAI compatible provider.
   - `OLLAMA_HOST`: Host address and port for the Ollama service.
   - `API_KEY`: API key for the OpenAI compatible provider (set `USE_CHAT_OLLAMA` to False).
   - `OPENAI_BASE_URL`: Base URL for the OpenAI compatible provider (set `USE_CHAT_OLLAMA` to False).
   - `USE_VISION`: Enable or disable vision feature.
   - `HEADLESS`: Run the browser in headless mode.

3. **Command Line Options**

   ```bash
   python -m ppwdump [-h] [--no-out] [--pytest] [--history] [--all] [--headless]
   ```

   Run the main task with optional outputs. Default behavior: output python code

   options:
   - `-h, --help`: show this help message and exit
   - `--no-out`: Output nothing
   - `--pytest`: Output only pytest code
   - `--history`: Output only history list
   - `--all`: Output history list, python code and pytest code
   - `--headless`: Run the browser in headless mode

## Using ppwdump as a Library

You can use the `ppwdump` library directly in your own projects. Here's an example of how to do this:

```python
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
```

## Disable Telemetry

   To disable browser-use telemetry, export the `ANONYMIZED_TELEMETRY` environment variable to `"false"` in your shell:
   - On Windows, run:
     ```cmd
     set ANONYMIZED_TELEMETRY=false
     ```
   - On macOS and Linux, run:
     ```bash
     export ANONYMIZED_TELEMETRY="false"
     ```

## Contributing

Contributions to this project are welcome. Please fork the repository and submit pull requests with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](License) file for details.