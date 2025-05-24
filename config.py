# ppwdump/config.py

ANONYMIZED_TELEMETRY = "false"

# LLM Configuration
OLLAMA_MODEL = "msm" 
OLLAMA_BASE_URL = "http://192.168.105.3:11434"
#reduce to 16384 or 8192 if needed if low VRAM/RAM
OLLAMA_NUM_CTX = 32768
USE_VISION = False
ENABLE_MEMORY = False
