# ppwdump/config.py

OLLAMA_MODEL = "msm"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"
#reduce to 16384 or 8192 if needed if low VRAM/RAM
OLLAMA_NUM_CTX = 32768
USE_VISION = False
ANONYMIZED_TELEMETRY = False
ENABLE_MEMORY = False #not implemented leave False
HEADLESS = False