from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import pandas as pd


import re

def cleanText(readData):
    # 텍스트에 포함되어 있는 특수 문자 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text


def naver_corona():
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    date2 = time.strftime('%Y%m%d', time.localtime(time.time()))
    # 코로나 바이러스
    keyword = "코로나"
    result = {}

    # 웹접속 - 네이버 이미지 접속
    # 84.0.4147.30 / chrome version
    print("접속중")
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.implicitly_wait(30)

    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}'.format(keyword)
    driver.get(url)

    hwak = driver.find_elements_by_css_selector(
        '#_cs_production_type > div:nth-child(6) > div.status_info > ul > li.info_01 > p')
    scan = driver.find_elements_by_css_selector(
        '#_cs_production_type > div:nth-child(6) > div.status_info > ul > li.info_02 > p')
    reco = driver.find_elements_by_css_selector(
        '#_cs_production_type > div:nth-child(6) > div.status_info > ul > li.info_03 > p')
    dead = driver.find_elements_by_css_selector(
        '#_cs_production_type > div:nth-child(6) > div.status_info > ul > li.info_04 > p')

    result['date'] = str(today)
    result['patient'] = cleanText(hwak[0].text)
    result['check_corona'] = cleanText(scan[0].text)
    result['recovery'] = cleanText(reco[0].text)
    result['dead'] = cleanText(dead[0].text)

    # text3 = driver.find_elements_by_css_selector('strong.num')
    driver.close()

    output_file = pd.DataFrame(result, index=[0])

    df_korea = pd.read_csv('corona.csv')

    if df_korea.loc[-1:, 'date'].item() == today:
        df_korea = df_korea.drop(df_korea.iloc[-1:].index, axis=0)
        df_korea = df_korea.append(output_file)
        df_korea.to_csv('corona.csv', index=False)
    else:
        df_korea = df_korea.append(output_file)
        df_korea.to_csv('corona.csv', index=False)