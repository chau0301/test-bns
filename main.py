from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

webTarget = 'https://app2.benefitsolutions.com.sg/devAmplify/v.2/#/login'

chrome_driver_path = "/chrome-driver/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get(webTarget)

# test case 1: Check forgot
try:
    # wait for 2 seconds
    time.sleep(2)
    forgotPasswordButton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#__layout > div > div > div > div.main_content.d-flex.justify-content-center > div.d-flex.flex-column.align-items-center > div.login-container.d-flex.flex-column.justify-content-center.align-items-center > div > div.form__info > div.forget-password.mt--15 > a")))
    forgotPasswordButton.click()

    h2_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#__layout > div > div > div > div.main_content.d-flex.justify-content-center > div.d-flex.flex-column.align-items-center > div > div > div > div.credentials.mt--30 > h2"))
    )
    print("Test case 1:", "Forgot Credentials?" == h2_element.text)
    signin_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "#__layout > div > div > div > div.main_content.d-flex.justify-content-center > div.d-flex.flex-column.align-items-center > div > div > div > div.askAccount.line-height-12.text-black.font-400.mt--30.font__regular.text-16 > a"))
    )
    signin_element.click()
except NameError:
    print("Test case 1: False")
finally:
    pass

# test case 2
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    # username_field.send_keys(testDict["username"])

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.send_keys(testDict["password"])
    password_field.send_keys(Keys.RETURN)

    username_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-group-1 > div > div:nth-child(3) > em")))
    print("Test case 2:",  username_label.text == "Your username does not match our records")
except:
    print("Test case 2: false")
finally:
    pass

# test case 3
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    username_field.send_keys("anh_hr")

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.clear()
    password_field.send_keys(Keys.RETURN)

    password_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-group-2 > div > div:nth-child(4) > em")))
    print("Test case 3:",  password_label.text == "Your password is blank")
except:
    print("Test case 3: false")
finally:
    pass

# test case 4
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    username_field.clear()
    username_field.send_keys("phuonganh")

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.clear()
    password_field.send_keys("P@ssw0rd")
    password_field.send_keys(Keys.RETURN)

    above_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#__layout > div > div > div > div.main_content.d-flex.justify-content-center > div.d-flex.flex-column.align-items-center > div.alert_login.text-white.text-center.text-14 > div")))
    print("Test case 4:", above_label.text == "Sorry, your account is not registered.")
except:
    print("Test case 4: false")
finally:
    pass

# test case 5
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    username_field.clear()
    username_field.send_keys("anh_hr")

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.clear()
    password_field.send_keys("Test@123")
    password_field.send_keys(Keys.RETURN)

    above_label = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#__layout > div > div > div > div.main_content.d-flex.justify-content-center > div.d-flex.flex-column.align-items-center > div.alert_login.text-white.text-center.text-14 > div")))
    print("Test case 5:", above_label.text == "Oops, it seems like your userid or password is not valid. Please re-enter. Do watch out for your Capslock.")
except:
    print("Test case 5: false")
finally:
    pass

# test case 6
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    username_field.clear()
    username_field.send_keys("anh_hr")

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.clear()
    password_field.send_keys("P@ssw0rd")
    password_field.send_keys(Keys.RETURN)

    logo_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#__layout > div > div.d-flex.flex-column.mb-header > nav > div.navbar-brand.m-0.cursor_pointer > img")))
    logo_src = logo_header.get_attribute("src")
    print("Test case 6:", logo_src == "https://app2.benefitsolutions.com.sg/devAmplify/v.2/_nuxt/img/logo.6754364.png")
except:
    print("Test case 6: false")
finally:
    pass

# test case 7
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    username_field.clear()
    username_field.send_keys("anh_hr")

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.clear()
    password_field.send_keys("abcdef")
    password_field.send_keys(Keys.RETURN)
    password_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-group-2 > div > div:nth-child(4) > em")))
    print("Test case 7:",  password_label.text == "Password must include 8 characters, 1 special character and 1 uppercase letter and 1 number")
except:
    print("Test case 7: false")
finally:
    pass

# test case 8
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    username_field.clear()
    username_field.send_keys("anh_hr")

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.clear()
    password_field.send_keys("abcdefg1")
    password_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-group-2 > div > div:nth-child(4) > em")))
    print("Test case 8:",  password_label.text == "Password must include 8 characters, 1 special character and 1 uppercase letter and 1 number")
except:
    print("Test case 8: false")
finally:
    pass

# test case 9
try:
    # wait for 2 seconds
    time.sleep(2)
    # find the username input field and enter the username
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-username")))
    username_field.clear()
    username_field.send_keys("anh_hr")

    # find the password input field and enter the password
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-field-password")))
    password_field.clear()
    password_field.send_keys("Abcdefg1@")
    password_field.send_keys(Keys.RETURN)
    password_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-group-2 > div > div:nth-child(4) > em")))
    print("Test case 9:",  password_label.text == "Password must include 8 characters, 1 special character and 1 uppercase letter and 1 number")
except:
    print("Test case 9: false")
finally:
    pass

driver.close()