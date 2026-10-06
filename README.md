# Patreon Download Helper

*Written in November 2024 to download German-learning materials from my own paid subscription.*\
*No longer maintained and may not work with Patreon's current page layout.*

**Overview**

This Python script uses Selenium WebDriver to automate repetitive downloads in a logged-in browser session. It opens a page, scrolls to load more content (for example on infinite-scroll pages) and then clicks every download link that matches specified keywords. It reuses an existing Chrome profile, so the browser stays signed in and no credentials are stored in the script.

Scrolling continues until the user presses Enter or a configurable time limit is reached. The script then starts the downloads. The browser can still be used while the script runs.

This tool is intended only for content you already have access to. Redistribution of copyrighted content is not supported.

**Requirements**

- Python 3.x
- Selenium WebDriver (for automating the browser)
- ChromeDriver (matching the version of Google Chrome installed on your system)
- Google Chrome browser installed with an existing user profile

**Usage**

1. Install Selenium: `pip install selenium`
2. In `patreon_download_helper.py`, adjust:
   - the Chrome binary and user-profile paths,
   - the path to `chromedriver.exe`,
   - the target URL,
   - the XPath keywords that identify the download links.
3. Run `python patreon_download_helper.py` and press Enter when enough content has loaded.

Large pages can use a lot of memory, so it is best to download content in smaller batches.

**Features**

- Chrome Browser Automation: Automates the Chrome browser using Selenium WebDriver.
- Custom User Profile: Utilizes an existing Chrome user profile to keep the session signed in.
- Background Key Press Listener: Lets the user stop scrolling early with the Enter key and start the downloads.
- Scroll Time Limit: Stops scrolling after a configurable duration to prevent memory overload and browser crashes.
- File Download: Identifies and clicks on download links that match specified keywords via XPath.
- Error Handling: Includes basic error handling so a failed link does not stop the remaining downloads.
