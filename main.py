from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4
# import pandas as pd
import csv
from selenium.webdriver import FirefoxOptions
import time


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def thai_number_to_int(value):
    if value != "":
        thai_numbers = {
            'ศูนย์': 0,
            'หนึ่ง': 1,
            'สอง': 2,
            'สาม': 3,
            'สี่': 4,
            'ห้า': 5,
            'หก': 6,
            'เจ็ด': 7,
            'แปด': 8,
            'เก้า': 9,
            'สิบ': 10,
            'ร้อย': 100,
            'พัน': 1000,
            'หมื่น': 10000,
            'แสน': 100000,
            'ล้าน': 1000000
        }
        int_value = 0
        # Split the input value into its components
        if value.find(".") > 0:
            intNum, point = value.split(".")
            value = "."+point
            if "พัน" in value:
                int_value = int(
                    intNum)*thai_numbers["พัน"] + float(value.replace("พัน", ""))*thai_numbers["พัน"]
            elif "หมื่น" in value:
                int_value = int(intNum)*thai_numbers["หมื่น"] + float(
                    value.replace("หมื่น", ""))*thai_numbers["หมื่น"]
            elif "แสน" in value:
                int_value = int(
                    intNum)*thai_numbers["แสน"] + float(value.replace("แสน", ""))*thai_numbers["แสน"]
            elif "ล้าน" in value:
                int_value = int(
                    intNum)*thai_numbers["ล้าน"] + float(value.replace("ล้าน", ""))*thai_numbers["ล้าน"]

        else:
            if "พัน" in value:
                int_value = int(value.replace("พัน", ""))*thai_numbers["พัน"]
            elif "หมื่น" in value:
                int_value = int(value.replace("หมื่น", "")) * \
                    thai_numbers["หมื่น"]
            elif "แสน" in value:
                int_value = int(value.replace("แสน", ""))*thai_numbers["แสน"]
            elif "ล้าน" in value:
                int_value = int(value.replace("ล้าน", ""))*thai_numbers["ล้าน"]
            else:
                int_value = value
        return int_value
    else:
        return 0


# driver = webdriver.Chrome(
#     executable_path=r'D:\Work Dev\makewebbkk\scraping shoppee\chromedriver_win32\chromedriver')


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    options=options, executable_path="path/to/executable")

# options = FirefoxOptions()
# options.add_argument("--headless")
# options.binary_location = r''
# # browser = webdriver.Firefox(options=options)

# driver = webdriver.Firefox(executable_path=r'/Users/tharintantayothin/Desktop/Nut/makeWebBkk/Shopee_repo/web-scraping-shopee/geckodriver.exe', options=options)


driver.get('https://shopee.co.th/nppbox')

delay = 3  # seconds
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, 'main')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
# เลือกภาษาไทย
# thai_button = driver.find_element(
#     '/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[3]/div[1]/button")


thai_button.click()
# ccc = driver.find_element(
#     By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[3]/button[7]")
# ccc.click()


product_name_list = []
product_price_list = []
product_sale_list = []

driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
driver.execute_script("document.body.style.zoom='10%'")
data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup
time.sleep(10)
total_pages_element = int(soup.find(
    'span', {'class': 'shopee-mini-page-controller__total'}).text)
print(total_pages_element)
# all_product = soup.find_all('div', {'class': 'Mz89A3 WZO+p+ uAxOVF'})
# all_product_price = soup.find_all('div', {'class': "KF1Uvz _3QBW9H"})
# all_product_sale = soup.find_all('div', {'class': 'rOgDNT lNPX0P'})
# print(len(all_product))
# print(len(all_product_price))
# print(len(all_product_sale))
# all_product = soup.find_all('div', {'class': 'VptMHK Odl6HA GO6iCi'})
# print(len(all_product))

# for product in all_product:
#     # print(product.text)
#     product_name_list.append(product.text)

# all_product_price = soup.find_all('div', {'class': "uwSW-2 qljqDx"})

# for product in all_product_price:
#     # print(product.text)
#     product_price_list.append(product.text)


# all_product_sale = soup.find_all('div', {'class': "ZjwhVB YpOBv3"})

# for product in all_product_sale:
#     # print(product.text)
#     product_sale_list.append(product.text)

# print(product_detail_list)
# driver.close()

check_btn_next = 0
while check_btn_next < total_pages_element:
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(
    #     options=options, executable_path="path/to/executable")
    page_url = f'https://shopee.co.th/nppbox?page={check_btn_next}'
    print(f'https://shopee.co.th/nppbox?page={check_btn_next}')
    driver.get(page_url)
    time.sleep(3)
    try:
        myElem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, 'main')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
    driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')
    driver.execute_script("document.body.style.zoom='5%'")
    time.sleep(3)
    data = driver.page_source  # ดึงข้อมูลจากหน้าเว็บ
    soup = bs4.BeautifulSoup(data)  # จัดในรูปแบบ BeautifulSoup

    all_product = soup.find_all('div', {'class': 'Mz89A3 WZO+p+ uAxOVF'})
    all_product_price = soup.find_all('div', {'class': "KF1Uvz _3QBW9H"})
    all_product_sale = soup.find_all('div', {'class': 'rOgDNT'})

    # print(all_product_sale)
    print(len(all_product))
    print(len(all_product_price))
    print(len(all_product_sale))

    for x in range(len(all_product)):
        if x > 5:
            product_name_list.append(all_product[x].text)

    for x in range(len(all_product_price)):
        if x > 5:
            product_price_list.append(all_product_price[x].text)
    for x in range(len(all_product_sale)):
        if x > 5:
            product_sale_list.append(all_product_sale[x].text)

    check_btn_next += 1

driver.close()

print(len(product_name_list))
print(len(product_price_list))
print(len(product_sale_list))
header = ['name', 'price', 'sale']
data_csv = []

with open('shopee.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(product_name_list)):
        data_csv = []
        data_csv.append(product_name_list[i])
        data_csv.append(product_price_list[i].replace("฿", ""))
        data_csv.append(thai_number_to_int((product_sale_list[i].replace(
            "ขายแล้ว ", "").replace(" ชิ้น", ""))))
        writer.writerow(data_csv)


# with open('shopee1.txt', 'w', encoding="utf-8") as f:
#     for i in range(len(product_name_list)):
#         f.write(product_name_list[i]+"," +
#                 product_price_list[i]+","+product_sale_list[i])
#         f.write('\n')
