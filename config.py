# ppwdump/config.py

#BROWSER Model
BROWSER_MODEL_PROVIDER="ollama" #Can be ollama, google, or openai 
BROWSER_MODEL = "msm32"
USE_VISION = False
HEADLESS = False
#CODE_MODEL
CODE_MODEL_PROVIDER="ollama" #Can be ollama, google, or openai
CODE_MODEL = "msm32"
#Ollama settings
OLLAMA_HOST = "192.168.105.3:11434"
#Google settings
GOOGLE_API_KEY="none"
#OpenAI settings (set USE_CHAT_OLLAMA = False)
OPENAI_API_KEY = "none"
OPENAI_BASE_URL = "http://192.168.105.3:11434/v1"
#GENERAL
ANONYMIZED_TELEMETRY = False


