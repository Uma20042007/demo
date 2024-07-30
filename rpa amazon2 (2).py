import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

# Replace with your Amazon credentials
username = "your_amazon_username"
password = "your_amazon_password"

# Replace with the specific order number you want to track
order_number = "123-4567890-1234567"

# Initialize the browser (adjust browser path if needed)
driver = webdriver.Chrome()  # Path to your ChromeDriver

# Navigate to Amazon login page
driver.get("https://www.amazon.com/")

# Log in to Amazon
username_field = driver.find_element(By.ID, "ap_email")
password_field = driver.find_element(By.ID, "ap_password")
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
time.sleep(3)  # Wait for page to load

# Navigate to order history
driver.find_element(By.LINK_TEXT, "Returns & Orders").click()
time.sleep(2)

# Find the relevant order
order_link = driver.find_element(By.XPATH, f"//a[contains(@href, 'orderId={order_number}')]")
order_link.click()
time.sleep(2)

# Extract tracking details
tracking_info = driver.find_element(By.ID, "order-details-table").text
tracking_status = tracking_info.splitlines()[4]  # Assuming status is on line 4

# Print or use tracking information
print("Your product is", tracking_status)

# Close the browser
driver.quit()
