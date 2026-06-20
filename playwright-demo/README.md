# python -m venv venv
venv\Scripts\activate

# pip install playwright pytest pytest-playwright


# playwright install

# playwright install chromium

# for playwright stealthy 
npm install playwright playwright-extra

# CI setup checklist:
# Make sure your CI has these commands:

bash
# 1. Install dependencies
pip install pytest playwright pytest-playwright

# 2. Install browsers
playwright install chromium

# 3. Optionally install deps
playwright install-deps chromium  # installs system deps