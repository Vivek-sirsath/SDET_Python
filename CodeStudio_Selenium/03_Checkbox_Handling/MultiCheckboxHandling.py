import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
time.sleep(30)
print("url opened")

Second_ChkBox = driver.find_element(By.ID, "id_checkboxes_1")
Second_ChkBox.click()
print("2nd check box selected")

Third_ChkBox = driver.find_element(By.ID, "id_checkboxes_2")
Third_ChkBox.click()
print("3rd checkbox selected")

driver.find_element(By.ID, "submit-id-submit").click()
print("clicked on submit button")
time.sleep(3)

# Verify selected checkboxes
resultTxt = driver.find_element(By.XPATH, "//p[@id='result-text']")
result = resultTxt.text
if result.__contains__("two, three"):
    print("Checkboxes selected properly")
else:
    print("Checkboxes not selected properly")

