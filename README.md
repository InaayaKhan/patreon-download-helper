# Patreon Scrape Bot

**Overview**

*Written in November 2024 to download German-learning materials from my own paid subscription.*\
*No longer maintained and may not work with Patreon's current page layout.*

This Python script uses Selenium WebDriver to automate the process of navigating a webpage, scrolling for content, and downloading files from specified links. It is designed to work with Google Chrome or any Chromium-based browser using an existing user profile to maintain sessions and avoid logins.

The script runs in the background and allows for user interaction. Once the user presses the Enter key, it will start the process of downloading files from the page. The script is designed to be used on a page like Patreon or similar sites where downloadable content is linked via specific keywords.

NOTE: This tool can only be used to download content that you have already paid for. I do not support the redistribution of copyrighted content.

**Requirements**

- Python 3.x
- Selenium WebDriver (for automating the browser)
- ChromeDriver (matching the version of Google Chrome installed on your system)
- Google Chrome browser installed with an existing user profile

**Features**

- Chrome Browser Automation: Automates the Chrome browser using Selenium WebDriver.
- Custom User Profile: Utilizes an existing Chrome user profile for seamless browsing.
- Background Key Press Listener: Waits for the user to press the Enter key before starting the downloading process.
- Scrolling Mechanism: Scrolls down a webpage to load more content (useful for infinite scroll pages).
- File Download: Identifies and clicks on downloadable links that match specified keywords.
- Error Handling: Includes basic error handling to deal with possible download failures.
