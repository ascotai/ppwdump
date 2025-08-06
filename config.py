# ppwdump/config.py

#Browser model
BROWSER_MODEL_PROVIDER="ollama" #Can be ollama, google, or openai 
BROWSER_MODEL = "uq3c5"
USE_VISION = False #Currently msmnew needs vision!
HEADLESS = False
#Code model
CODE_MODEL_PROVIDER="ollama" #Can be ollama, google, or openai
CODE_MODEL = "uq3c5"
#Ollama settings
OLLAMA_HOST = "127.0.0.1:11434"
#Google settings
GOOGLE_API_KEY="google_gemini_api_key"
#OpenAI settings
OPENAI_API_KEY = "open_api_key"
OPENAI_BASE_URL = "http://127.0.0.1:11434/v1"
#General
ANONYMIZED_TELEMETRY = False


