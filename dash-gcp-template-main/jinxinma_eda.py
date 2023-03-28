# import csv
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import pandas as pd

def run_eda_analysis():
    data = pd.read_csv('./unprocessed_dataset.zip',skipinitialspace = True) #,low_memory=False
    group = data.groupby('YYYY').mean()
    group = group.reset_index()
    own = data[data['HOMEOWN'] == 1]
    rent = data[data['HOMEOWN'] == 2]
    own_group = own.groupby('YYYY').mean()
    own_group = own_group.reset_index()
    rent_group = rent.groupby('YYYY').mean()
    rent_group = rent_group.reset_index()
    group1 = pd.DataFrame()
    group1['YYYY'] = own_group['YYYY']
    group1['Rent-Income'] = rent_group['INCOME']
    group1['Own-Income'] = own_group['INCOME']

    fig1 = px.line(group, x='YYYY', y='INCOME', title='Income Increasement with time')
    fig1.update_traces(mode='markers+lines')

    fig2 = px.line(group1, x='YYYY', y=['Rent-Income', 'Own-Income'], title='Relationship between house rent and own',
                  labels={'value': 'Value', 'variable': 'Lines'})
    fig2.update_traces(mode='markers+lines')
    fig2.update_layout(legend_title='Lines',
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

    df_diff = group1.iloc[:, 1:].diff()
    df_diff['YYYY'] = group1['YYYY']
    fig3 = px.bar(df_diff, x='YYYY', y=['Rent-Income', 'Own-Income'], barmode='group',
                 title='First Order difference of income')
    return list((fig1,fig2,fig3))
