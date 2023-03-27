import pandas as pd
import numpy as np
import plotly.express as px

def run_eda_analysis():
    survey_df = pd.read_csv('./unprocessed_dataset.zip',skipinitialspace = True) #,low_memory=False
    # 
    ## Compare income and interest rates for borrowing money
    df1 = survey_df[['RATEX', 'INCOME']]
    def rate_groups(series):
        rate={
            1:'Go up',
            3:'Stay the same',
            5:'Go down',
            8:'DK',
            9:'NA'
            }
        return rate.get(series)

    df1['rate'] = df1['RATEX'].apply(rate_groups)
    df1['RATEX1']= df1['RATEX'].astype({'RATEX':'category'}).replace([8,9], np.nan)
    df1_full=df1.dropna()

    fig1 = px.box(df1_full, x="rate", y="INCOME",width=600, height=600,
                category_orders={"rate":["Go up","Stay the same","Go down"]})
    fig1.update_layout(title_text='Income and Interest Rates for Borrowing Money')

    #
    ## political affiliation by education level

    df2=survey_df[['POLAFF','EDUC']]
    def politic_groups(series):
        rate={
            1:'Republican',
            2:'Democrat',
            3:'Independent, No Preference',
            8:'DK',
            9:'NA'
            }
        return rate.get(series)

    df2['political'] = df2['POLAFF'].apply(politic_groups)

    def educ_groups(series):
        rate={
            1:'Grade 0-8 no hs diploma',
            2:'Grade 9-12 no hs diploma',
            3:'Grade 0-12 w/ hs diploma',
            4:'Grade 13-17 no col degree',
            5:'Grade 13-16 w/ col degree',
            6:'Grade 17 W/ col degree'
            }
        return rate.get(series)

    df2['education'] = df2['EDUC'].apply(educ_groups)

    df2_nan= df2.replace([8,9,None], np.nan)
    # df2=pd.concat([df2[['EDUC']], dfPOLAFF], axis=1)
    df2_full=df2_nan.dropna()

    df2_value_counts=df2_full.value_counts().to_frame().reset_index()
    df2_value_counts.columns = ['EDUC','POLAFF','education level', 'political affiliation','count'] # change column names

    fig2 = px.bar(df2_value_counts, x='political affiliation', y="count", color='EDUC', text='education level',
                category_orders={"political affiliation":['Republican','Democrat','Independent, No Preference'],
                                "education level":['Grade 0-8 no hs diploma','Grade 9-12 no hs diploma','Grade 0-12 w/ hs diploma','Grade 13-17 no col degree','Grade 13-16 w/ col degree','Grade 17 W/ col degree']})
    fig2.update_layout(title_text='Political Affiliation by Education Level') #, xaxis_tickangle=-45

    #
    ## political affiliation by age
    df3=survey_df[['POLAFF','AGE']]

    df3['political'] = df3['POLAFF'].apply(politic_groups)
    df3_nan= df3.replace([8,9,None], np.nan)
    df3_full=df3_nan.dropna()

    fig3 = px.histogram(df3_full, x='AGE', color='political',text_auto=True)
    fig3.update_layout(title_text='Political Affiliation by Education Level') #, xaxis_tickangle=-45

    return list(fig1,fig2,fig3)

