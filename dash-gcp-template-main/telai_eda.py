import pandas as pd
import numpy as np
import plotly as py
import plotly.express as px


def run_eda_analysis():
    file= pd.read_csv("./unprocessed_dataset.zip")
    
    df = file.sort_values('INCOME')
    df = df[df['INCOME'].str.strip() != '']
    df = df[df['SEX'].str.strip() != '']
    df['INCOME'] = df['INCOME'].astype(int)
    df['SEX'] = df['SEX'].astype(int)

    accumulated_rates = []

    for gender in df['SEX'].unique():
        gender_df = df[df['SEX'] == gender]
        total_income = 0
        gender_accumulated_rates = []
        for income in gender_df['INCOME']:
            total_income += income
            gender_accumulated_rates.append(total_income / gender_df['INCOME'].sum())
        accumulated_rates += gender_accumulated_rates

    df['accumulated_rates'] = df.groupby('SEX')['INCOME'].cumsum() / df.groupby('SEX')['INCOME'].transform('sum')
    df1=df
    df1['SEX'] = df1['SEX'].replace({1: 'female', 2: 'male'})
    df1.drop_duplicates(subset=['SEX', 'accumulated_rates'], inplace=True)

    fig1 = py.express.line(df1, x='INCOME', y='accumulated_rates', color='SEX')


    df = file.sort_values('INCOME')
    df = df[df['INCOME'].str.strip() != '']
    df = df[df['SEX'].str.strip() != '']
    df['INCOME'] = df['INCOME'].astype(int)
    df['SEX'] = df['SEX'].astype(int)
    df = df[df['EDUC'].str.strip() != '']
    df['EDUC'] = df['EDUC'].astype(int)
    avg_wage_by_edu_sex = df.groupby(['EDUC', 'SEX']).mean()["INCOME"]
    df = pd.merge(df, avg_wage_by_edu_sex, on=["EDUC","SEX"])
    df_male = df[df["SEX"] == 1]
    df_female = df[df["SEX"] == 2]
    df = df.sort_values(["EDUC"])
    df['EDUC'] = df['EDUC'].astype(int)

    fig2 = px.line(df, x='EDUC', y='INCOME_y', color='SEX', line_group='SEX', labels={'EDUC':'EDUCATION LEVEL', 'INCOME_y':'WAGE'}, title='Average WAGE by EDUCATION LEVEL and SEX')

    df = file.sort_values('INCOME')
    df = df[df['INCOME'].str.strip() != '']
    df = df[df['SEX'].str.strip() != '']
    df['INCOME'] = df['INCOME'].astype(int)
    df['SEX'] = df['SEX'].astype(int)

    df = df[df['MARRY'].str.strip() != '']
    df['MARRY'] = df['MARRY'].astype(int)
    avg_wage_by_edu = df.groupby("MARRY").mean()["INCOME"]
    df = pd.merge(df, avg_wage_by_edu, on="MARRY")
    df1=df.drop_duplicates(subset=['MARRY'])
    df1 = df.sort_values(["MARRY"])

    fig3 = px.line(df1, x='MARRY', y='INCOME_y', title='INCOME DISTRIBUTION')
    fig3.update_layout(xaxis_title='MARRY (1 Married, 2 Separated, 3 Divorced, 4 Widowed, 5 No Married)',
                    yaxis_title='INCOME',
                    xaxis=dict(tickmode='linear', tick0=1, dtick=1))

    return (fig1, fig2, fig3)