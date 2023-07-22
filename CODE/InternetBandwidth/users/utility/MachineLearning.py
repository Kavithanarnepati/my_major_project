from django.conf import settings
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score


def startProcess():
    path = os.path.join(settings.MEDIA_ROOT, 'Punedata.csv')
    df = pd.read_csv(path)
    # df = df[['LAC','Data_2019','Data_2020','Data_2021']]
    # print(df.head())
    df['usage'] = df[['Data_2019','Data_2020','Data_2021']].mean(axis=1)
    x_set = df['LAC'].values
    y_set = df['usage'].values
    x_set = x_set.reshape(-1,1)
    actual_val = df['Data_2019'].values
    x_test = actual_val.reshape(-1,1)
    dt = DecisionTreeRegressor()
    dt.fit(x_set,y_set)
    dt_pred = dt.predict(x_set)
    #print(dt_pred)
    #print(x_test)
    dt_acc = r2_score(x_test,dt_pred)

    # print(dt_acc)
    # fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    # ax.plot(x_test, color="red", label="Original")
    # ax.plot(dt_pred, color="green", label="Predections")
    # # ax.plot(x_set, color="green", label="Direct forecast")
    # ax.set_title(f"Original vs predection")
    # ax.legend()
    # plt.show()

    df_dt = pd.DataFrame(list(zip(x_set, x_test,dt_pred)),
                      columns=['LAC', 'Actual','Predicted'])
    df_dt = df_dt.to_html(index=False)

    rf = RandomForestRegressor()
    rf.fit(x_set, y_set)
    rf_pred = rf.predict(x_set)
    rf_acc = r2_score(x_test, rf_pred)
    rf_df = pd.DataFrame(list(zip(x_set, x_test, rf_pred)),
                         columns=['LAC', 'Actual', 'Predicted'])
    rf_df = rf_df.to_html(index=False)

    knn = KNeighborsRegressor()
    knn.fit(x_set, y_set)
    knn_pred = knn.predict(x_set)
    knn_acc = r2_score(x_test, knn_pred)
    knn_df = pd.DataFrame(list(zip(x_set, x_test, rf_pred)),
                         columns=['LAC', 'Actual', 'Predicted'])
    knn_df = knn_df.to_html(index=False)
    return df_dt, dt_acc, rf_df, rf_acc,knn_df,knn_acc

