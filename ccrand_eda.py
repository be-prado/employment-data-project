import csv
import pandas as pd
import numpy as np
import plotly.express as px

    # Data being studied: 
    # - Month of Birth vs Household income
    # - Month of Birth vs Market Value of Home
    # - Month of Birth vs Investment Value

def birthm_recode(BIRTHM):
    dic = {
        1:	"January",
        2:	"February",
        3:	"March",
        4:	"April",
        5:	"May",
        6:	"June",
        7:	"July",
        8:	"August",
        9:	"September",
        10:	"October",
        11:	"November",
        12:	"December",
    }
    return dic.get(BIRTHM)

def inc(fter):
    f_inc = fter.melt(id_vars = ['BIRTHM'],value_vars= ['INCOME'], var_name="variables", value_name='Income')
    f_inc['BIRTHM'] = pd.Categorical(f_inc['BIRTHM'], categories=['January','February','March','April','May','June','July','August','September','October','November','December'], ordered=True)
    fig_inc = px.density_heatmap(f_inc.sort_values('BIRTHM'), x = "BIRTHM", y = "Income", facet_col='variables',
                          labels={'BIRTHM': 'Birth Month', 'values':'Dollars ($)'})
    return fig_inc

def home(fter):
    f_home = fter.melt(id_vars = ['BIRTHM'],value_vars= ['HOMEAMT'], var_name="variables", value_name='Home_Value')
    f_home['BIRTHM'] = pd.Categorical(f_home['BIRTHM'], categories=['January','February','March','April','May','June','July','August','September','October','November','December'], ordered=True)
    fig_home = px.density_heatmap(f_home.sort_values('BIRTHM'), x = "BIRTHM", y = "Home_Value", facet_col='variables',
                            labels={'BIRTHM': 'Birth Month', 'values':'Dollars ($)'})

    fig_home.update_layout(yaxis=dict(range = [0,2e6]))
    return fig_home

def inv(fter):
    f_inv = fter.melt(id_vars = ['BIRTHM'],value_vars= ['INVAMT'], var_name="variables", value_name='Investment_Value')
    f_inv['BIRTHM'] = pd.Categorical(f_inv['BIRTHM'], categories=['January','February','March','April','May','June','July','August','September','October','November','December'], ordered=True)
    fig_inv = px.density_heatmap(f_inv.sort_values('BIRTHM'), x = "BIRTHM", y = "Investment_Value", facet_col='variables',
                            labels={'BIRTHM': 'Birth Month', 'values':'Dollars ($)'})
    fig_inv.update_layout(yaxis=dict(range = [0,2e6]))
    return fig_inv

def run_eda_analysis():
    data = pd.read_csv("./unprocessed_dataset.zip")
    test = data[['BIRTHM', 'INCOME', 'HOMEAMT', 'INVAMT']]
    fter = test[(test['BIRTHM'].str.isspace() == False) & (test['INCOME'].str.isspace() == False) & (test['HOMEAMT'] != 9999998) & (test['HOMEAMT'] != 9999999) & (test['INVAMT'] != 99999998) & (test['BIRTHM'] != "15")]
    fter = fter.apply(pd.to_numeric, axis=1)
    fter['BIRTHM'] = fter['BIRTHM'].apply(birthm_recode)

    fig_inc = inc(fter)
    fig_home = home(fter)
    fig_inv = inv(fter)

    return (fig_home, fig_inv, fig_inc)