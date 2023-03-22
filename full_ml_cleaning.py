import csv
import pandas as pd
import numpy as np
# individual data cleaning modules
import beprado_ml_cleaning
import jpitti_ml_cleaning


def run_full_ml_cleaning():
    # do general data cleaning
    df = pd.read_csv("./unprocessed_dataset.zip")
    ml_vars = df[['YYYY', 'YYYYMM', 'INCOME', 'HOMEAMT', 'HOMEOWN', 'INVAMT', 'AGE', 'REGION', 'SEX', 'MARRY', 'EGRADE', 'EHSGRD', 'ECLGRD', 'POLAFF']]
    df = ml_vars.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna()
    df = df.apply(pd.to_numeric, axis=1)
    # do variable specific data cleaning
    print("\nRunning beprado_ml_cleaning...")
    df = beprado_ml_cleaning.run_ml_cleaning(df)
    print("Done with beprado_ml_cleaning!\n")
    print("\nRunning jpitti_ml_cleaning...")
    df = jpitti_ml_cleaning.run_ml_cleaning(df)
    print("Done with jpitti_ml_cleaning!\n")

    return df