# ppwdump

## Description

`ppwdump` turns an ollama prompt into runnable python playwright code and pytest playwright code. It uses Playwright, Langchain-ollama, and Browser-use. This project leverages the power of these libraries to interact with web browsers and generate code for various purposes.


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
   - `OLLAMA_MODEL`: The language model to use.
   - `OLLAMA_BASE_URL`: The base URL for the language model.
   - `OLLAMA_NUM_CTX`: The number of context tokens.

3. **Browser Configuration**

   The browser configuration is handled in `__main__.py`. You can customize the browser settings by modifying the `BrowserProfile` object. The browser settings docs are found [here](https://docs.browser-use.com/customize/browser-settings)

4. **Command Line Options**

   ```bash
   python -m ppwdump [-h] [--no-out] [--pytest] [--history] [--all]
   ```

   Run the main task with optional outputs. Default behavior: output python code

   options:
   - `-h, --help`: show this help message and exit
   - `--no-out`: Output nothing
   - `--pytest`: Output only pytest code
   - `--history`: Output only history list
   - `--all`: Output history list, python code and pytest code

## Code Generation

The project includes functions for code generation:

- `generate_playwright_code(history_list)`: Generates Python Playwright code based on a history list.
- `generate_pytest_playwright_code(playwright_code)`: Generates PyTest code from Python Playwright scripts.

These functions are located in `code_generation.py`.

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

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.