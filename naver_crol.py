from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm


# 키워드 입력
keyword = "골든 리트리버 성견"
key = "gold_dog"

# 웹접속 - 네이버 이미지 접속
# 79.0.3945.36 / chrome version
print("접속중")
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.implicitly_wait(30)

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)
driver.get(url)
# 페이지 스크롤 다운
# body = driver.find_element_by_css_selector('body')
# for i in range(150):
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

# 이미지 링크 수집
imgs = driver.find_elements_by_css_selector('img._img')
result = []
for img in tqdm(imgs):
    if 'http' in img.get_attribute('src'):
        result.append(img.get_attribute('src'))
print(result)

# driver.close()
# print('수집완료')
#
# # 파일 저장
# import os
# if not os.path.isdir('./{}'.format(key)):
#     print('폴더생성')
#     os.mkdir('./{}'.format(key))
#
# # 다운로드
# from urllib.request import urlretrieve
#
# print("다운로드중")
# for index, link in tqdm(enumerate(result)):
#     start = link.rfind('.')
#     end = link.rfind('&')
#     # print(link[start:end])
#     filetype = link[start:end]
#     if filetype == '.jpg':  # jpg 만 다운
#         urlretrieve(link, './{}/{}{}{}'.format(key, key, index, filetype))
#         time.sleep(1)
# print("다운로드 완료")
#
# # import zipfile
# # zip_file = zipfile.Zipfile('./{}.zip'.format(keyword),'w')
# # # 이 폴더안에 파일 가져오는거
# # for image in tqdm(os.listdir('./{}'.format(keyword))):
# #     zip_file.write('./{}/{}'.format(keyword,image), compress_type=zip_file.ZIP_DEFLATED)
# # zip_file.close()
# # print("압축완료")
