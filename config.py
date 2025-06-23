# ppwdump/config.py

BROWSER_MODEL = "q25c"
CODE_MODEL = "msm"
BASE_URL = "http://127.0.0.1:11434/v1"
#reduce to 16384 if needed if low VRAM/RAM
BROWSER_NUM_CTX = 22528
CODE_NUM_CTX = 32768
USE_VISION = False
ANONYMIZED_TELEMETRY = False
ENABLE_MEMORY = False #not implemented leave False
HEADLESS = False
# API Key for ChatOpenAI
API_KEY = "key_if_needed"
