# ppwdump

## Description

`ppwdump` turns a prompt into runnable python playwright code and pytest playwright code. It uses Playwright, and Browser-use. This project leverages the power of these libraries to interact with web browsers and generate code for various purposes.

https://github.com/user-attachments/assets/566c2711-c3b7-4a5c-8bdc-92557c6b57a9

## Important Note

This project works best with version 0.8.0 of Ollama. Using later versions may cause issues at this time.

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
   - `BASE_URL`: The base URL for the language model.
   - `BROWSER_NUM_CTX`: The number of context tokens for browser interactions.
   - `CODE_NUM_CTX`: The number of context tokens for code generation.
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
    my_model = "msm"
    my_url  = "http://127.0.0.1:11434"
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
