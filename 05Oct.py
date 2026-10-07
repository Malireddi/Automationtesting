# 1. Program that automatically login with username and password in saucedemo website

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username=driver.find_element(By.ID, "user-name")
password=driver.find_element(By.ID, "password")
login=driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

print(username.get_attribute("placeholder"))
print(login.is_enabled())
print(username.is_displayed())


login.click()
driver.quit()


# 2. Program that automatically opens google and search actor chiyan vikram

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/search?q=Pawan+kalyan")

print("Chrome opened.")
print("Searching for: Pawan kalyan")
print("If CAPTCHA appears, the browser will remain open.")
print("Press ENTER in this terminal when you want to close the browser.")

input()

print("ENTER pressed. Closing browser...")
driver.quit()


# 3. Program that automatically login and shows the products as list of names

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

login.click()

products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

product_names = [product.text for product in products]

driver.execute_script("""
    document.body.innerHTML = `
        <h1>Product List</h1>
        <ol id="product-list"></ol>
    `;
""")

for product in product_names:
    driver.execute_script("""
        let li = document.createElement("li");
        li.textContent = arguments[0];
        document.getElementById("product-list").appendChild(li);
    """, product)

input("Press ENTER to close the browser...")

driver.quit()
