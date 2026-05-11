from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Launch browser

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Open website

driver.get("https://adnabu-store-assignment1.myshopify.com/password")

# Enter password

password_box = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)

password_box.send_keys("AdNabuQA")

# Click Enter button

enter_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)

enter_button.click()

# Click search icon

search_icon = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "summary[aria-label='Search']"))
)

search_icon.click()

# Search product

search_box = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='search']"))
)

search_box.send_keys("The Collection Snowboard: Liquid")
search_box.send_keys(Keys.ENTER)

# Open product

first_product = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "The Collection Snowboard"))
)

first_product.click()

# Add to cart

# Add to cart

add_to_cart = wait.until(
    EC.element_to_be_clickable((By.ID, "ProductSubmitButton-template--19850788667482__main"))
)

driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)

driver.execute_script("arguments[0].click();", add_to_cart)

print("Product added to cart successfully")

driver.quit()