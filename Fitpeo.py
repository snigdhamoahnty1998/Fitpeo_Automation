from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# browser_driver
driver = webdriver.Chrome()

# open_url
driver.get("https://www.fitpeo.com/revenue-calculator")
time.sleep(2)

# maximize_browser
driver.maximize_window()
time.sleep(5)

# navigate_calculator
driver.find_element(By.LINK_TEXT,"Revenue Calculator").click()
time.sleep(5)

# scroll_page
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(5)

slider_thumb = driver.find_element(By.CLASS_NAME, "MuiSlider-thumb")

# Create an ActionChains object to perform the drag operation
actions = ActionChains(driver)

# Click and hold on the slider thumb
actions.click_and_hold(slider_thumb)
actions.move_by_offset(93, 0)  # Here i give 93 but it goes up to 816, for 820 we should give 93.3 but it won't take any decimal offset.
actions.release().perform()
time.sleep(5)

text_box = driver.find_element(By.ID,":R57alklff9da:")
time.sleep(5)
text_box.click()
time.sleep(5)

# clear_value
input_field = driver.find_element(By.XPATH, "//input[@id=':R57alklff9da:']") 

# Use JavaScript to clear the value of the input field
driver.execute_script("arguments[0].value = '';", input_field)
time.sleep(5)
input_field.send_keys("560")
time.sleep(5)

# drag_sliders
driver.execute_script("window.scrollBy(500, 550);")
time.sleep(5)


# for check_boxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
max_checkboxes_to_select = 3
selected_count = 0

# Loop through all checkboxes
for checkbox in checkboxes:
    if selected_count >= max_checkboxes_to_select:  # Stop if 3 checkboxes have been selected
        break
    if not checkbox.is_selected():  # Check if the checkbox is unchecked
        checkbox.click()  # Click it to select
        selected_count += 1 

for checkbox in checkboxes:
    if checkbox.is_selected():
        print("Checkbox is selected.")
    else:
        print("Checkbox is not selected.")

time.sleep(5)





driver.close()



