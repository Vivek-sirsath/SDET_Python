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

chkBoxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

# Click action on each checkbox
for chkBox in chkBoxes:
    chkBox.click()

print("All 3 check boxes selected")

# Click on submit button
driver.find_element(By.ID, "submit-id-submit").click()
print("clicked on submit button")
time.sleep(3)

# Verify selected checkboxes
resultTxt = driver.find_element(By.XPATH, "//p[@id='result-text']").text
if resultTxt.__contains__("one, two, three"):
    print("Checkboxes selected properly")
else:
    print("Checkboxes not selected properly")





