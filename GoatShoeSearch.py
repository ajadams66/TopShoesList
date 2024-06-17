import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import date

today = date.today()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
Likes_available = True

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.goat.com/collections/just-dropped')
time.sleep(5)

# Shoe1
Shoe1 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/a/div[1]/div[1]/div[1]')
Shoe1_name = Shoe1.text
Shoe1_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/a/div[1]/div[2]/div/div')
Shoe1_price = Shoe1_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/a/div[1]/div[1]/div[2]')
date1 = date.text
Shoe1 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/a')
Shoe1_src = Shoe1.get_attribute('href')
# Shoe2
Shoe2 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[2]/a/div[1]/div[1]/div[1]')
Shoe2_name = Shoe2.text
Shoe2_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[2]/a/div[1]/div[2]/div/div/span')
Shoe2_price = Shoe2_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[2]/a/div[1]/div[1]/div[2]')
date2 = date.text
Shoe2 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[2]/a')
Shoe2_src = Shoe1.get_attribute('href')
# Shoe3
Shoe3 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[3]/a/div[1]/div[1]/div[1]')
Shoe3_name = Shoe3.text
Shoe3_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[3]/a/div[1]/div[2]/div/div')
Shoe3_price = Shoe3_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[3]/a/div[1]/div[1]/div[2]')
date3 = date.text
Shoe3 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[3]/a')
Shoe3_src = Shoe1.get_attribute('href')
# Shoe4
Shoe4 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[4]/a/div[1]/div[1]/div[1]')
Shoe4_name = Shoe4.text
Shoe4_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[4]/a/div[1]/div[2]/div/div[1]/span')
Shoe4_price = Shoe4_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[4]/a/div[1]/div[1]/div[2]')
date4 = date.text
Shoe4 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[4]/a')
Shoe4_src = Shoe1.get_attribute('href')
# Shoe5
Shoe5 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[5]/a/div[1]/div[1]/div[2]')
Shoe5_name = Shoe5.text
Shoe5_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[5]/a/div[1]/div[1]/div[1]')
Shoe5_price = Shoe5_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[5]/a/div[1]/div[2]/div/div[1]/span')
date5 = date.text
Shoe5 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[5]/a')
Shoe5_src = Shoe1.get_attribute('href')
# Shoe6
Shoe6 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[6]/a/div[1]/div[1]/div[1]')
Shoe6_name = Shoe6.text
Shoe6_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[6]/a/div[1]/div[2]/div/div/span')
Shoe6_price = Shoe6_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[6]/a/div[1]/div[1]/div[2]')
date6 = date.text
Shoe6 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[6]/a')
Shoe6_src = Shoe1.get_attribute('href')
# Shoe7
Shoe7 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[7]/a/div[1]/div[2]/div/div[1]/span')
Shoe7_name = Shoe7.text
Shoe7_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[7]/a/div[1]/div[1]/div[1]')
Shoe7_price = Shoe7_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[7]/a/div[1]/div[1]/div[2]')
date7 = date.text
Shoe7 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[7]/a')
Shoe7_src = Shoe1.get_attribute('href')
# Shoe8
Shoe8 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[8]/a/div[1]/div[2]/div/div/span')
Shoe8_name = Shoe8.text
Shoe8_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[8]/a/div[1]/div[1]/div[1]')
Shoe8_price = Shoe8_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[8]/a/div[1]/div[1]/div[2]')
date8 = date.text
Shoe8 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[8]/a')
Shoe8_src = Shoe1.get_attribute('href')
# Shoe9
Shoe9 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[9]/a/div[1]/div[2]/div/div[1]/span')
Shoe9_name = Shoe9.text
Shoe9_p = driver.find_element(By.XPATH,
                              value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[9]/a/div[1]/div[1]/div[1]')
Shoe9_price = Shoe9_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[9]/a/div[1]/div[1]/div[2]')
date9 = date.text
Shoe9 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[9]/a')
Shoe9_src = Shoe1.get_attribute('href')
# Shoe10
Shoe10 = driver.find_element(By.XPATH,
                             value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[10]/a/div[1]/div[2]/div/div/span')
Shoe10_name = Shoe10.text
Shoe10_p = driver.find_element(By.XPATH,
                               value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[10]/a/div[1]/div[1]/div[1]')
Shoe10_price = Shoe10_p.text
date = driver.find_element(By.XPATH,
                           value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[10]/a/div[1]/div[1]/div[2]')
date10 = date.text
Shoe10 = driver.find_element(By.XPATH,
                            value='/html/body/div[1]/div/main/div[1]/div/div[2]/div/div[1]/div[14]/a')
Shoe10_src = Shoe1.get_attribute('href')
Shoe_list = {
    'Shoe Name': [Shoe1_name, Shoe2_name, Shoe3_name, Shoe4_name, Shoe5_name, Shoe6_name, Shoe7_name, Shoe8_name,
                  Shoe9_name, Shoe10_name],
    'price': [Shoe1_price, Shoe2_price, Shoe3_price, Shoe4_price, Shoe5_price, Shoe6_price, Shoe7_price, Shoe8_price,
              Shoe9_price, Shoe10_price],
    'release date': [date1, date2, date3, date4, date5, date6, date7, date8, date9, date10],
    'LInk to shoe': [Shoe1_src, Shoe2_src, Shoe3_src, Shoe4_src, Shoe5_src, Shoe6_src, Shoe7_src, Shoe8_src, Shoe9_src, Shoe10_src]
}
movie_list = pd.DataFrame.from_dict(Shoe_list)
movie_list.to_csv(f'NewShoes-{today}.csv', index=False)