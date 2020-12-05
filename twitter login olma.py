from selenium import webdriver
import time
import csv
import datetime
from datetime import date, timedelta
kull_adi_input= input("kullanıcı adınızı giriniz")
sifre_input = input("şifrenizi giriniz")

driver= webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://twitter.com/login")

kullanici_adi = driver.find_element_by_name("session[username_or_email]")
sifre = driver.find_element_by_name("session[password]")
twitler1=[]
kullanici_adi.send_keys(kull_adi_input)
sifre.send_keys(sifre_input)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div").click()

twitler=driver.find_elements_by_tag_name('p')
twitler1.append(twitler)
with open('twitler1.csv', 'a', newline='', encoding='utf-8') as f:
	w = csv.writer(f, delimiter='\n')
	w.writerow(twitler)
pass
driver.close()

