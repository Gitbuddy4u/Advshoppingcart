import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select  # <--- add this import for drop down lists

s = Service(executable_path ='.//chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'-------------------------~*~--------------------------')
    print(f'Test start at:{datetime.datetime.now()}')
    # make browswer full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    driver.get(locators.adv_shop_cart_url)

    if driver.current_url == locators.adv_shop_cart_url and driver.title == '\xa0Advantage Shopping':
        print(f'Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.5)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'-------------------------~*~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def signup():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]').click()
    sleep(2)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
    sleep(0.5)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
    sleep(0.5)
    driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
    sleep(0.5)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(0.5)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(0.5)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(0.5)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(2)
    print(f'--------New Account Created----------------')

def check_full_name():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate = "My_account"]').click()
    sleep(2)

    if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed():
        print(f'----The full name of the user:{locators.full_name}--------')
    else:
        print(f'----something went wrong please check the open account page script----')
    sleep(1)

def check_orders():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    sleep(3.0)
    assert driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    sleep(0.5)
    no_orders = driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    if no_orders == True:
        print(f'------------Their is no order---------------')
    else:
        print(f'-------------something is wrong ---check the script----')


def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="Sign_out"]').click()
    sleep(2)


def log_in():
    if driver.current_url == locators.adv_shop_cart_url:
        print( f'----home page is displayed----')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(2)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)
        print( f'----login is successful with new account----------')
    else:
        print(f'-------please check the script to fix the error--------')


def delete_test_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(10)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate="My_account"]').click()
    # driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(10)
    driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').click()
    sleep(10)
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    sleep(10)

def verify_account_deleted():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    sleep(0.5)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)

    if driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]'
                                     '[contains(., "Incorrect user name or password")]').is_displayed():
        sleep(5)
        print(f'------Account has been successfully deleted---Account {locators.username}--------')
    else:
        print(f'-----please check the script for error----------------')


def check_home_page():
    driver.get(locators.adv_shop_cart_url)
    list_opts1 = [ 'SPEAKERS', 'TABLETS', 'HEADPHONES', 'LAPTOPS', 'MICE']
    for e in list_opts1:
        if driver.find_element(By.XPATH, f"//span[contains(., '{e}')]").is_displayed():
            sleep(0.5)
            print(f"we can see '{e}' link on homepage")
        else:
            print("'{element}' link is nit displayed on the homepage!")

    list_opts2 = ['SPECIAL OFFER', 'POPULAR ITEMS', 'CONTACT US']
    for l in list_opts2:
        if driver.find_element(By.XPATH, f'//a[contains(., "{l}")]').is_displayed():
            sleep(0.5)
            driver.find_element(By.XPATH, f'//a[contains(., "{l}")]').click()
            sleep(1)
            if driver.find_element(By.XPATH, f"//*[self::h1 or self::h3][contains(., '{l}')]").is_displayed():
                sleep(0.5)
                print(f'-------{l}-----is displayed.------')
        else:
            print(f'-----the logo is not displayed-----')

    if driver.find_element(By.XPATH, f'//span[contains(., "dvantage")]').is_displayed()\
            and driver.find_element(By.XPATH, f'//span[contains(., "DEMO")]').is_displayed():
        sleep(2)
        print(f'-----logo is displayed---------')
    else:
        print(f'------The logo is not displayed------')

    driver.find_element(By.XPATH, f'//a[contains(., "CONTACT US")]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, f'//h1[contains(., "CONTACT US")]').is_displayed()
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Headphones')
    sleep(0.5)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text("Bose SoundLink Around-ear Wireless Headphones II")
    sleep(0.5)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/a').is_displayed():
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/a').click()
        print('------continue shopping button is displayed.------')
    else:
        print('---------something went wrong, please check the code for continue shopping button-------')







# setUp()
# signup()
# check_full_name()
# check_orders()
# log_in()
# log_out()
# log_in()
# log_out()
# log_in()
# log_out()
# delete_test_account()
# verify_account_deleted()
# check_home_page()
# tearDown()