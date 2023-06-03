from selenium import webdriver
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\\Users\\Admin\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

url_video=input("enter url video : ")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()

driver.get('https://zefoy.com/')
screen='screenshot.png'
driver.save_screenshot(screen)
img = Image.open(screen)
text = tess.image_to_string(img)
text1=text
def read_last_line(text1):
	lines = text1.strip().split('\n')
	if lines:
		last_line = lines[-1].strip()
		return last_line
	else:
		return None

last_line = read_last_line(text1)
if last_line:
	print(last_line)
else:
	print("error")
sleep(1)
#this for input check capotch
input_captch = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/form/div/div/div/input")
input_captch.send_keys(last_line)

sleep(1)
click_check = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/form/div/div/div/div/button")
click_check.click()
#/////////////////////////////
sleep(5)
try:
	click_viwes = driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div[5]/div/button")
	click_viwes.click()
	sleep(10)
except Exception as e:
	os.remove(screen)
	os.system('py tiktok_views.py')





input_views = driver.find_element(By.XPATH,"/html/body/div[10]/div/form/div/input")
input_views.send_keys(url_video)
sleep(3)

click_search = driver.find_element(By.XPATH,"/html/body/div[10]/div/form/div/div/button")
click_search.click()
sleep(120)
click_search_2 = driver.find_element(By.XPATH,"/html/body/div[10]/div/form/div/div/button")
click_search_2.click()
sleep(3)
while True:
	click_viwes = driver.find_element(By.XPATH,'//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button')
	click_viwes.click()
	sleep(180)
	click_search_2 = driver.find_element(By.XPATH,"/html/body/div[10]/div/form/div/div/button")
	click_search_2.click()
	sleep(3)




