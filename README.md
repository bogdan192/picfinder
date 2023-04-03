# Smoke tests for picfinder.ai

Tests to open the page, check landing page elements and do a simple search

- Runs only on chromium
- Support for **headless and headed** execution (run with --hedless for speed).
 

## How to install

- Install python 3 [Download Page](https://www.python.org/downloads/)
- Install playwright for Python (both module and browsers) see [Installation guide](https://playwright.dev/python/docs/intro)
- Install the requirements in requirements.txt

python3 -m pip install -r requirements.txt

## How to run
- For headed execution (see the browser) 

python3 -m pytest --html=report.html --self-contained-html --headed tests.py

- For headless remove the  --headed parameter

## Documentation

See on [playwright.dev](https://playwright.dev/python/docs/test-runners) for examples and more detailed information.