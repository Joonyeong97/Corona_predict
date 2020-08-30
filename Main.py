# Installing collected packages: pystan, ephem, LunarCalendar, pymeeus, convertdate, holidays, setuptools-git, fbprophet
# conda install -c conda-forge fbprophet
# pip install plotly
# pip install ipython

import time
import Corona_naver
import Corona
PATH = 'C:/Users/82105/Desktop/Data_Analysis/Python/Develop_Code/Corona_predict/result_img/'
# 낮으면 타이트하게, 높으면 유연하게
scale = 0.2

# 자동업데이트
if __name__ == '__main__':
    start = str(input("1 = 업데이트, 2 = 예측, 3 = 둘다  "))
    if start == '1':
        Corona_naver.naver_corona()
    elif start == '2':
        Corona.corona_prdict()
    elif start == '3':
        Corona_naver.naver_corona()
        time.sleep(1)
        Corona.corona_prdict()
    else:
        pass