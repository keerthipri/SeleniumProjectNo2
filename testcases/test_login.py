import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="D:/programming files/chromedriver_win32/chromedriver.exe")
    driver.implicitly_wait(10)
    yield
    driver.quit()


def test_Login_01(test_setup):
   driver.get("http://opensource-demo.orangehrmlive.com/")
   driver.find_element(By.NAME,value="username").send_keys("Admin")
   driver.find_element(By.NAME,value="password").send_keys("admin123")
   driver.find_element(By.XPATH,value="//button[@type='submit']").click()
   assert "pim" in driver.current_url;
   print("successfully logined")



def test_Login_02(test_setup):
    driver.get("http://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME,value="username").send_keys("Admin")
    driver.find_element(By.NAME,value="password").send_keys("invalidpassword")
    driver.find_element(By.XPATH,value="//button[@type='submit']").click()
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
    currenturl = driver.current_url
    if (currenturl == url):
        print("succeccfully logined")
    else:
        print("invalid credentials,check username and password")


def test_PIM_01(test_setup):
    driver.get("http://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, value="username").send_keys("Admin")
    driver.find_element(By.NAME, value="password").send_keys("admin123")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("keerthi")
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("priya")
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.CONTROL + "a")
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.DELETE)

    time.sleep(5)
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys("97531")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, value="//label[text()='Nationality']/../../div[2]/div/div/div").click()
    driver.find_element(By.XPATH, value="//*[text()='Indian']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//label[text()='Marital Status']/../../div[2]/div/div/div").click()
    driver.find_element(By.XPATH, value="//*[text()='Married']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span").click()
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//label[text()='Blood Type']/../../div[2]/div/div/div").click()
    driver.find_element(By.XPATH, value="//*[text()='A-']").click()
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(2)


def test_PIM_02(test_setup):
    driver.get("http://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, value="username").send_keys("Admin")
    driver.find_element(By.NAME, value="password").send_keys("admin123")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("97531")
    time.sleep(5)
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, value="//label[text()='Nationality']/../../div[2]/div/div/div").click()
    driver.find_element(By.XPATH, value="//*[text()='Albanian']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//label[text()='Marital Status']/../../div[2]/div/div/div").click()
    driver.find_element(By.XPATH, value="//*[text()='Single']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(10)

def test_PIM_03(test_setup):
    driver.get("http://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.find_element(By.NAME, value="username").send_keys("Admin")
    driver.find_element(By.NAME, value="password").send_keys("admin123")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
    driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("97531")
    driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,value="//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)


