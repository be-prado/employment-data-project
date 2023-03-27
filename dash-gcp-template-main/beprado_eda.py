import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run_eda_analysis():
    df = pd.read_csv("./unprocessed_dataset.zip")
    return (income_analysis(df), home_buying_analysis(df), economy_analysis(df))

def select_df_with_labels(df, labels):
    # remove missing entries
    sub_df = df[labels].replace(" ", "")
    for label in labels:
        sub_df = sub_df[sub_df[label] != '']
    return sub_df.astype(int)


def income_analysis(df):
    income_labels = ["PAGO", "PEXP", "BAGO", "INEXQ1"]
    income_df = select_df_with_labels(df, income_labels)
    corrM = income_df.corr()
    #hmap = sns.heatmap(corrM, vmin=-1, vmax=1, center=0,
    #                  cmap=sns.diverging_palette(200, 20, n=100))
    #hmap.set(title="Correlation Matrix")

    fig = px.imshow(corrM)
    return fig

def home_buying_analysis(df):
    # car buying attitudes by region
    home_buying_labels = ["HOM", "CAR", "REGION"]
    buying_df = select_df_with_labels(df, home_buying_labels).groupby("REGION").mean().reset_index()
    buying_df = pd.melt(buying_df, id_vars=["REGION"], value_vars=["HOM", "CAR"])
    buying_df = buying_df.rename(columns={"REGION": "Region", "value": "Buying Attitude", "variable": "Item"})
    #print(buying_df.columns)
    #buying_plot = sns.barplot(x=buying_df.columns[0], y=buying_df.columns[2], hue=buying_df.columns[1], data=buying_df)
    fig = px.bar(buying_df, x=buying_df.columns[0], y=buying_df.columns[2],
                color=buying_df.columns[1], barmode='group',
                height=400)
    return fig

def economy_analysis(df):
    # [income quintile, home quintile, stock investment quintile, political affiliation,  economy in 5 years, gov economic policy]
    economy_dem = ["YTL5", "HTL5", "STL5", "POLAFF", "BUS5", "GOVT"]
    economy_df = select_df_with_labels(df, economy_dem)
    economy_df = economy_df[(economy_df["POLAFF"] < 8) & (economy_df["BUS5"] < 98) & (economy_df["GOVT"] < 8)]
    economy_df.head()
    economy_corr = economy_df.corr()
    #hmap = sns.heatmap(economy_corr, vmin=-1, vmax=1, center=0,
    #                  cmap=sns.diverging_palette(200, 20, n=100))
    #hmap.set(title="Correlation Matrix")

    fig = px.imshow(economy_corr)
    return fig



