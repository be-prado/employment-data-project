import pandas as pd

def run_ml_cleaning(df_in):

    df = df_in
    #recode to text
    def region_recode(reg):
        r_dic = {
        1:	"West",
        2:	"North Central",
        3:	"Northeast",
        4:	"South"
        }
        return r_dic.get(reg)

    df['REGION'] = df['REGION'].apply(region_recode)

    def sex_recode(sex):
        r_dic = {
        1:	"Male",
        2:	"Female",
        }
        return r_dic.get(sex)

    df['SEX'] = df['SEX'].apply(sex_recode)

    def marry_recode(m):
        r_dic = {
        1:	"Married/partner",
        2:	"Separated",
        3: "Divorced",
        4: "Widowed",
        5: "Never Married"
        }
        return r_dic.get(m)

    df['MARRY'] = df['MARRY'].apply(marry_recode)


    #text to cats.
    df["REGION"] = pd.Categorical(df.REGION)

    df["SEX"] = pd.Categorical(df.SEX)

    df["MARRY"] = pd.Categorical(df.MARRY)

    df_out = pd.get_dummies(df, columns = ['REGION', 'SEX', 'MARRY'], drop_first=True)

    return df_out