# Instagram Profile Information Scraper

## Description
This repository contains an automation script written in Python to retrieve the follower count and following count of any Instagram profile(Instagram Profile Of GUVI is used). It utilizes the Selenium library for web automation.

## Automation Script
The automation script is named `guvi_insta.py`. It includes a class `InstagramPageInfo` with methods to initialize the WebDriver, navigate to the Instagram page, retrieve follower count, retrieve following count, and handle browser shutdown. The script also includes test cases using pytest for positive and negative scenarios.

## Test Script
The test script is named `test_guvi_insta.py`. It contains test cases for various scenarios such as retrieving follower count, retrieving following count, handling invalid URLs, and handling exceptions.

## Requirements
- Python 3.12.0
- Selenium library
- GeckoDriverManager (for managing GeckoDriver for Firefox)
- Firefox browser

## Setup

1. Install dependencies:
    ```
    pip install selenium webdriver-manager pytest
    ```
2. Make sure you have Firefox browser installed.

## Usage
1. Set the URL of the Instagram profile you want to scrape in the `guvi_insta.py` script.
2. Run the automation script using Python:
    ```
    python guvi_insta.py
    ```
3. To run the test script:
    ```
    pytest test_guvi_insta.py
    ```

