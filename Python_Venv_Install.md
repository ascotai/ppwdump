To install this project using a Python virtual environment and clone the repository, follow these steps:

1. **Clone the Repository:**
   Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Then, run the following command:
   ```bash
   git clone https://github.com/ascotai/ppwdump.git
   cd ppwdump
   ```

2. **Create a Virtual Environment with uv:**
   Navigate to the root directory of the cloned project. Then, create a virtual environment using `uv` for Python 3.12.3 by running:
   ```bash
   uv venv -p python3.12.3 venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows, activate the virtual environment with:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux, activate the virtual environment with:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   With the virtual environment activated, install the required dependencies listed in `requirements.txt` by running:
   ```bash
   uv pip install -r requirements.txt
   ```

5. **Install Playwright:**
   Install Playwright and its necessary browser binaries by running:
   ```bash
   uv run playwright install
   ```

6. **Disable Telemetry:**
   To disable browser-use telemetry, export the `ANONYMIZED_TELEMETRY` environment variable to `"false"` in your shell:
   - On Windows, run:
     ```cmd
     set ANONYMIZED_TELEMETRY=false
     ```
   - On macOS and Linux, run:
     ```bash
     export ANONYMIZED_TELEMETRY="false"
     ```

7. **Run the Project:**
   You can now run the project using the following command:
   ```bash
   cd ../
   python -m ppwdump
   ```

This will execute the main script located in `__main__.py`, which in turn calls the `main` function from `main.py`.

If you encounter any issues or need further assistance, please refer to the `Readme.md` file for additional information or consider checking the project's documentation or contributing guidelines.
