from pathlib import Path

# Application
BASE_URL = "https://www.saucedemo.com/"

# Browser
BROWSER = "chrome"
HEADLESS = False

# Timeout
TIMEOUT = 10

# Project Paths
ROOT = Path(__file__).resolve().parent.parent

REPORT_DIR = ROOT / "reports"
SCREENSHOT_DIR = ROOT / "screenshots"
LOG_DIR = ROOT / "logs"

# Create folders automatically
for folder in [REPORT_DIR, SCREENSHOT_DIR, LOG_DIR]:
    folder.mkdir(exist_ok=True)