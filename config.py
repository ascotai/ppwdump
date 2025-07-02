# ppwdump/config.py
#Ollama settings
USE_CHAT_OLLAMA = True # True for better Ollama performance, False to use an OpenAI compatible provider
OLLAMA_HOST = "127.0.0.1:11434"
#OpenAI settings (set USE_CHAT_OLLAMA = False)
API_KEY = "none"
OPENAI_BASE_URL = "http://127.0.0.1:11434/v1"
#Both
BROWSER_MODEL = "msm32"
CODE_MODEL = "msm32"
USE_VISION = False
ANONYMIZED_TELEMETRY = False
ENABLE_MEMORY = False #not implemented leave False
HEADLESS = False

