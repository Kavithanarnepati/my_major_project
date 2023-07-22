from django.conf import settings
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def startEda():
    path = os.path.join(settings.MEDIA_ROOT, 'Punedata.csv')
    df = pd.read_csv(path)
    X_axis = df['LAC']
    Y_axis_2019 = df['Data_2019']
    Y_axis_2020 = df['Data_2020']
    Y_axis_2021 = df['Data_2021']
    data = df[['LAC', 'Data_2021']]
    groupedvalues = data.groupby('LAC').sum().reset_index()
    plt.xticks(rotation=90)
    ax = sns.barplot(x='LAC', y='Data_2021', data=groupedvalues, errwidth=0)
    ax.bar_label(ax.containers[0])
    plt.xlabel("LAC")
    plt.ylabel("Total Data in GB")
    plt.show()