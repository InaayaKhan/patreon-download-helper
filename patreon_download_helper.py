import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Chrome options for Chrome with your existing profile
chrome_options = Options()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to Chrome browser. Might need to be changed
chrome_options.add_argument(r"user-data-dir=C:/Users/Public/ChromeUser")  # Path to Chrome user data. Might need to be changed
chrome_options.add_argument(r"profile-directory=Default")  # Profile directory

# Create a Service object for ChromeDriver
service = Service("chromedriver.exe")  # Ensure chromedriver.exe path is correct and matches Chrome version
driver = webdriver.Chrome(service=service, options=chrome_options)

# Variable to check if Enter key has been pressed
enter_pressed = False

# Function to wait for Enter keypress
def wait_for_enter():
    global enter_pressed
    input("Press Enter to start downloading files...")
    enter_pressed = True

# Start the Enter key listener thread
threading.Thread(target=wait_for_enter).start()

# This code was written to download content from the channel "Easy German"
# This part will need to be edited depending on what you wish to download

try:
    # Navigate to the desired page
    driver.get("https://patreon.com/your-target-url?view=expanded")  # Replace with your target URL
    time.sleep(10)  # Initial wait for the page to load. Adjust based on your needs.

    # NOTE: Although you could theoretically download everything at once, I do not recommend it because it maxxed out my RAM and crashed.
    # I suggest downloading content in bits if it is a lot.
    # You can interact with the browser while this script is at work.


    # Set the scroll duration limit
    scroll_duration = 300  # Total scroll time in seconds allowed for scrolling
    end_time = time.time() + scroll_duration  # Calculate the end time

    # Scroll down for the specified duration or until Enter is pressed
    while time.time() < end_time and not enter_pressed:
        driver.execute_script("window.scrollBy(0, 1000000);")  # Scroll down at insane speeds
        time.sleep(1)  # Wait briefly to allow content to load

    print("Scrolling completed or Enter key pressed.")

    # Find all download links that contain specific keywords and click each one
    # You will have to edit this based on what links you want to click to download the content
    download_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'HTML') or contains(text(), 'Textdatei') or contains(text(), 'Semikolon-Trennung')]")

    print(f"Found {len(download_links)} download links.")
    
    for link in download_links:
        try:
            link.click()
            time.sleep(0.01)  # Wait briefly to allow download to start. This is actually very fast already. 0.01s
        except Exception as e:
            print(f"Failed to click link: {e}")

finally:
    # Close the browser after operation
    driver.quit()
