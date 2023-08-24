from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

# Set the path to your ChromeDriver executable
chrome_driver_path = 'path/to/chromedriver.exe'

# Create a new Chrome browser instance
chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Open the website
website_url = 'https://example.com'  # Replace with the actual URL
driver.get(website_url)

try:
    # Locate and click the bullet button
    bullet_button = driver.find_element(By.ID, 'bullet_button_id')  # Replace with the actual ID
    bullet_button.click()

    # Wait for a brief moment (you might need to adjust the time depending on page load)
    driver.implicitly_wait(5)  # 5 seconds

    # Locate and click the vote button
    vote_button = driver.find_element(By.ID, 'vote_button_id')  # Replace with the actual ID
    vote_button.click()

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser window
    driver.quit()
