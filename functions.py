from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import NoSuchElementException ,ElementClickInterceptedException 
from selenium.webdriver.support.ui import Select
import re
import time
import sys
import csv
import random

def slowsctipt():
    time.sleep(random.randint(5,15))

def find_single_element_with_retries(driver, locator, timeout=10, retries=3):
    for attempt in range(retries):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            print(f"Element found: {locator}")
            return element
        except Exception as e:
            if attempt < retries - 1:
                print(f"Retrying to find element: {locator}, Attempt {attempt + 1}")
                time.sleep(2)
            else:
                print(f"Error finding element {locator}: {e}")
                raise

def find_multiple_element_with_retries(driver, locator, timeout=10, retries=3):
    
    for attempt in range(retries):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return element
        except Exception as e:
            if attempt < retries - 1:
                print(f"Retrying to find element: {locator}, Attempt {attempt + 1}")
                time.sleep(2)
            else:
                print(f"Error finding element {locator}: {e}")
                raise
            
def login(driver,psw="mvs12345",email="abhotline@gmail.com"):
    driver.get("https://drm.donary.com/")
    time.sleep(20)

    emailelemnt=find_single_element_with_retries(driver,locator=(By.XPATH, "//input[@name='email' and @placeholder='User name']"))

    emailelemnt.send_keys(email)

    passwordelemnt=find_single_element_with_retries(driver,locator=(By.XPATH,"//input[@name='password' and @placeholder='Password' and @id='passwordId']"))

    passwordelemnt.send_keys(psw)
    
    loginbutton=find_single_element_with_retries(driver,locator=(By.XPATH,"//button[contains(@class, 'btnsignin')]"))


    loginbutton.click()
    time.sleep(15)
    driver.get("https://drm.donary.com/transaction")
    time.sleep(15)
    
def togglemenu(driver):
    closemenu_element=find_single_element_with_retries(driver,locator=(By.XPATH,"//a[@data-widget='pushmenu']"))

    closemenu_element.click()
    
def filters(driver):
    filterbutton=find_single_element_with_retries(driver,locator=(By.CLASS_NAME,"filter_text"))
    filterbutton.click()
    slowsctipt()
    productfilter=find_single_element_with_retries(driver,locator=(By.XPATH,"//span[text()='Select Payment Type']"))

    actions = ActionChains(driver)
    
    actions.move_to_element(productfilter).click().perform()
    slowsctipt()
    
    item_payment_search_element=find_single_element_with_retries(driver,locator=(By.XPATH,"//input[@placeholder='Search Payment Type']"))
    item_payment_search_element.click()

    titles=["Pledger","Credit Card","OJC","Matbia"]
    for i in titles:
        item_payment_search_element.send_keys(i)
        
        dropitem=find_single_element_with_retries(driver,locator=(By.XPATH,f"//label[text()='{i}']"))
        dropitem.click()
        item_payment_search_element.clear()
        slowsctipt()
    
    telement=find_single_element_with_retries(driver,locator=(By.XPATH,"//span[text()='Select Collector']"))

    driver.execute_script("arguments[0].scrollIntoView();", telement)
    cancelbutton=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="ddlPaymentStatus"]/div/div[1]/div/span[2]'))
    slowsctipt()

    cancelbutton.click()
    productfilter=find_single_element_with_retries(driver,locator=(By.XPATH,"//span[text()='Select Payment Status']"))

    productfilter.click()
    payment_Type=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="ddlPaymentStatus"]/div/div[2]/div[3]/div[1]/label'))

    actions = ActionChains(driver)

    # Move to the element and click it with the mouse
    actions.move_to_element(payment_Type).click().perform()
    searchbuton_element=find_single_element_with_retries(driver,locator=(By.XPATH,"//button[text()=' Search' and contains(@class, 'btn-primary')]"))
    searchbuton_element.click()
    slowsctipt()
    
    


def calender(driver):
    datefilter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="paymentTransactionsCalender"]/div[1]/span/i'))
    slowsctipt()

    datefilter_element.click()
    tdayfilter_element=find_single_element_with_retries(driver,locator=(By.XPATH,"//button[@id='id_today']"))

    tdayfilter_element.click()

    driver.execute_script("window.scrollBy(0, 1000);")
    applyfilter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="ngb-popover-0"]/div[2]/app-common-hebrew-english-calendar/div[3]/button[2]'))

    actions = ActionChains(driver)

# Move to the element and click it with the mouse
    actions.move_to_element(applyfilter_element).click().perform()
    slowsctipt()
    
def exportfilters(driver):
    export_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="dLabel"]'))



    export_filter_element.click()
    time.sleep(15)
    

    created_datefilter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[4]/div/span/label'))

    actions = ActionChains(driver)

    actions.move_to_element(created_datefilter_element).click().perform()

    scroll_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[6]/div/span'))
    

    driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
    slowsctipt()
    hebrewdatefilter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[7]/div/span/label'))

    actions = ActionChains(driver)
    

    actions.move_to_element(hebrewdatefilter_element).click().perform()

    ref_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[9]/div/span/label'))

    actions = ActionChains(driver)
    actions.move_to_element(ref_element).click().perform()
    approval_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[8]/div/span/label'))

    actions = ActionChains(driver)
    actions.move_to_element(approval_filter_element).click().perform()
    

    schedule_info_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[9]/div/span/label'))

    actions = ActionChains(driver)
    actions.move_to_element(schedule_info_element).click().perform()
    next_scroll_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[11]/div/span'))
    
    driver.execute_script("arguments[0].scrollIntoView();", next_scroll_element)
    slowsctipt()
    
    sc_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[12]/div/span/label'))

    actions = ActionChains(driver)
    actions.move_to_element(sc_filter_element).click().perform()


    note_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[14]/div/span/label'))
    
    actions = ActionChains(driver)
    actions.move_to_element(note_filter_element).click().perform()
    campaign_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[15]/div/span/label'))

    actions = ActionChains(driver)
    actions.move_to_element(campaign_filter_element).click().perform()

    reason_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[16]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(reason_filter_element).click().perform()





    another_scroll_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[15]/div/span'))

    driver.execute_script("arguments[0].scrollIntoView();", another_scroll_element)
    slowsctipt()
    reson_sp_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[17]/div/span/label'))
    actions = ActionChains(driver)
    
    actions.move_to_element(reson_sp_element).click().perform()
    yet_another_scroll_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[20]/div/span'))

    driver.execute_script("arguments[0].scrollIntoView();", yet_another_scroll_element)
    slowsctipt()
    account_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[21]/div/span/label'))

    actions = ActionChains(driver)
    actions.move_to_element(account_filter_element).click().perform()
    donor_english_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[22]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(donor_english_filter_element).click().perform()
    address_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[23]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(address_filter_element).click().perform()
    city_state_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[24]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(city_state_filter_element).click().perform()
    phonenumber_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[25]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(phonenumber_filter_element).click().perform()

    continue_scroll_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[25]/div/span'))

    driver.execute_script("arguments[0].scrollIntoView();", continue_scroll_element)
    slowsctipt()
    email_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[26]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(email_filter_element).click().perform()
    batch_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[27]/div/span/label'))

    actions = ActionChains(driver)
    actions.move_to_element(batch_filter_element).click().perform()
    group_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[28]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(group_filter_element).click().perform()
    class_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[29]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(class_filter_element).click().perform()
    father_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[30]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(father_filter_element).click().perform()
    scroll_elemment1=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[30]/div/span'))

    driver.execute_script("arguments[0].scrollIntoView();", scroll_elemment1)
    slowsctipt()
    fatherinlaw_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[31]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(fatherinlaw_filter_element).click().perform()
    englishtitle_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[32]/div/span/label'))
    actions = ActionChains(driver)
    time.sleep(5)
    actions.move_to_element(englishtitle_filter_element).click().perform()
    english_firstname_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[33]/div/span/label'))
    actions = ActionChains(driver)
    time.sleep(5)
    actions.move_to_element(english_firstname_filter_element).click().perform()
    english_secondname_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[34]/div/span/label'))
    actions = ActionChains(driver)
    time.sleep(5)
    actions.move_to_element(english_secondname_filter_element).click().perform()
    yiddish_title_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[35]/div/span/label'))
    actions = ActionChains(driver)
    time.sleep(5)
    actions.move_to_element(yiddish_title_filter_element).click().perform()
    scroll_elemment2=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[35]/div/span'))

    driver.execute_script("arguments[0].scrollIntoView();", scroll_elemment2)
    slowsctipt()

    time.sleep(5)
    yiddish_firstname_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[36]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(yiddish_firstname_filter_element).click().perform()
    time.sleep(5)
    yiddish_secondname_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[37]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(yiddish_secondname_filter_element).click().perform()
    time.sleep(5)
    yiddish_lasttitle_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[38]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(yiddish_lasttitle_filter_element).click().perform()
    ammountapplied_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[39]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(ammountapplied_filter_element).click().perform()
    currency_ammount_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[40]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(currency_ammount_filter_element).click().perform()
    scroll_elemment3=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[40]/div/span'))

    driver.execute_script("arguments[0].scrollIntoView();", scroll_elemment3)
    slowsctipt()
    currency_type_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[41]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(currency_type_filter_element).click().perform()
    tags_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[42]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(tags_filter_element).click().perform()
    gateway_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="cdk-drop-list-0"]/div[43]/div/span/label'))
    actions = ActionChains(driver)
    actions.move_to_element(gateway_filter_element).click().perform()
    driver.execute_script("window.scrollBy(0, -1000);")
    time.sleep(5)
    export_filter_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="dLabel"]'))

    slowsctipt()

    export_filter_element.click()
    
def exportfile(driver):
    real_exportbtn_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="ngb-nav-0-panel"]/app-payment-transaction/div[1]/div/div[1]/div[1]/div[3]/div[2]/button'))
    slowsctipt()
    real_exportbtn_element.click()
    importbtn_element=find_single_element_with_retries(driver,locator=(By.XPATH,'//*[@id="ngb-nav-0-panel"]/app-payment-transaction/div[1]/div/div[1]/div[1]/div[3]/div[2]/ul/li[2]/a'))
    time.sleep(10)
    importbtn_element.click()


    

