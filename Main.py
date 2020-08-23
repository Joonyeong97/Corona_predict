# Installing collected packages: pystan, ephem, LunarCalendar, pymeeus, convertdate, holidays, setuptools-git, fbprophet
# conda install -c conda-forge fbprophet
# pip install plotly
# pip install ipython

import time
import Corona_naver
import Corona
PATH = 'C:/Users/82105/Desktop/Data_Analysis/Python/Study/Python_study/Python/pycharm/Testing/result_img/'
# 낮으면 타이트하게, 높으면 유연하게
scale = 0.2

# 자동업데이트
if __name__ == '__main__':
    start = str(input("당일자로 Corona 감염자 예측을 진행 하시겠습니까? y or n : "))
    if start == 'y':
        Corona_naver.naver_corona()
        time.sleep(1)
        Corona.corona_prdict()
    elif start == 'n':
        Corona.corona_prdict()
    else:
        pass