from django.conf import settings
import pandas as pd
import os

from sklearn.tree import DecisionTreeRegressor


def get_user_input(lac):
    path = os.path.join(settings.MEDIA_ROOT, 'Punedata.csv')
    df = pd.read_csv(path)
    df['usage'] = df[['Data_2019','Data_2020','Data_2021']].mean(axis=1)
    x_set = df['LAC'].values
    y_set = df['usage'].values
    x_set = x_set.reshape(-1,1)

    dt = DecisionTreeRegressor()
    dt.fit(x_set,y_set)
    rslt = dt.predict([[lac]])
    print('====>',rslt)
    return rslt[0]


