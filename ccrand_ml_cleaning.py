import pandas as pd

# Cleaning: EGRADE, EHSGRD, ECLGRD, POLAFF

def run_ml_cleaning(df):

    #recode to text
    def egrade_recode(egrade):
        dic = {num: str(num) for num in range(98)}
        dic[98] = "DK"
        dic[99] = "NA"
        return dic.get(egrade)

    df['EGRADE'] = df['EGRADE'].apply(egrade_recode)

    def ehsgrd_recode(ehsgrd):
        dic = {
            1: "Yes",
            5: "No",
            8: "DK",
            9: "NA",
        }
        return dic.get(ehsgrd)

    df['EHSGRD'] = df['EHSGRD'].apply(ehsgrd_recode)

    def eclgrd_recode(eclgrd):
        dic = {
            1: "Yes",
            5: "No",
            8: "DK",
            9: "NA",
        }
        return dic.get(eclgrd)

    df['ECLGRD'] = df['ECLGRD'].apply(eclgrd_recode)

    def polaff_recode(polaff):
        dic = {
            1: "Republican",
            2: "Democrat",
            3: "Independent, No Preference",
            8: "DK",
            9: "NA",
        }
        return dic.get(polaff)

    df['POLAFF'] = df['POLAFF'].apply(polaff_recode)

    # Text to Pandas Categories.
    df["EGRADE"] = pd.Categorical(df.EGRADE)

    df["EHSGRD"] = pd.Categorical(df.EHSGRD)

    df["ECLGRD"] = pd.Categorical(df.ECLGRD)

    df["POLAFF"] = pd.Categorical(df.POLAFF)

    df_out = pd.get_dummies(df, columns = ['EGRADE', 'EHSGRD', 'ECLGRD', 'POLAFF'], drop_first=True)

    return df_out