import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.offline as py
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import ParameterGrid
from tqdm import tqdm
import time
import Main

def corona_prdict():
    df_korea = pd.read_csv('corona.csv')
    df_prophet = df_korea[['date','patient']]
    # df_prophet = df_korea.rename(columns={
    #     'date': 'ds',
    #     'confirmed': 'y'
    # })
    df_prophet.columns = ['ds','y']

    # a = np.arange(0.8, 1.01, 0.1)
    # b = np.arange(0.1, 0.3, 0.1)
    #
    # params_grid = {'changepoint_range': a,
    #                'changepoint_prior_scale': b}
    # grid = ParameterGrid(params_grid)
    # for p in tqdm(grid):
    #     m = Prophet(**p,
    #                 yearly_seasonality=False,
    #                 weekly_seasonality=False,
    #                 daily_seasonality=True,
    #                 seasonality_mode='additive')
    #     m.fit(df_prophet)
    # print('optimum parameter loaded !!')
    
    m = Prophet(
        changepoint_prior_scale=Main.scale,  # 증가시 유연
        changepoint_range=0.90,  # 시계열의 첫 90%에 잠재적 변화점을 두다.
        yearly_seasonality=False,
        weekly_seasonality=False,
        daily_seasonality=True,
        seasonality_mode='additive'
    )

    m.fit(df_prophet)

    future = m.make_future_dataframe(periods=7) # 7일만 예상하겠다.
    forecast = m.predict(future)

    import matplotlib.font_manager as fm

    path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = fm.FontProperties(fname=path, size=50).get_name()
    plt.rc('font', family=font_name)

    fig = m.plot(forecast,figsize=(6,4), xlabel='날 짜', ylabel='감염자수(예상)')
    a = add_changepoints_to_plot(fig.gca(), m, forecast)
#    fig2 = plot_plotly(m, forecast, xlabel='날 짜', ylabel='감염자수(예상)')
    # py.iplot(fig2, filename='corona19.html')
    date = time.strftime('%Y%m%d', time.localtime(time.time()))
#    plotly.offline.plot(fig2, filename='corona_predict/corona19_{}.html'.format(date))
#     plt.imshow(a)
    plt.savefig(Main.PATH + "{}.png".format(date))