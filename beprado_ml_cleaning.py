import pandas as pd
import numpy as np
import cpi

def run_ml_cleaning(df):
    # replace NA responses with np.nan
    df = df.replace({"HOMEAMT" : {9999998: np.nan, 9999999: np.nan}, "INVAMT": {99999998: np.nan}})
    
    # inflate money with respect to year 
    df = df[df["YYYY"] != 2023] # can't inflate 2023 with cpi
    df["INFL_HOMEAMT"] = df.apply(lambda x: cpi.inflate(x["HOMEAMT"], int(x["YYYY"]), 2020), axis=1)
    df["INFL_INVAMT"] = df.apply(lambda x: cpi.inflate(x["INVAMT"], int(x["YYYY"]), 2020), axis=1)
    # drop uninflated columns
    df = df.drop(["HOMEAMT", "INVAMT"], axis=1)
    # replace nan values with mean
    home_mean = df[df["INFL_HOMEAMT"].notnull()]["INFL_HOMEAMT"].mean()
    inv_mean = df[df["INFL_INVAMT"].notnull()]["INFL_INVAMT"].mean()
    df = df.replace({"INFL_HOMEAMT": {np.nan: home_mean}, "INFL_INVAMT": {np.nan: inv_mean}})

    # remove unavailable homeownership data
    df = df[df["HOMEOWN"] != 99]
    return df