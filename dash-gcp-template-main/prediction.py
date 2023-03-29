def predict_xgboost(input_value):

    import pickle
    filehandler2=open("./model_xgboost.pkl",'rb')
    model_xgboost2=pickle.load(filehandler2)
    # prediction
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.model_selection import GridSearchCV
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import LabelEncoder
    df=pd.read_csv('./dataset_for_ml_models.zip',skipinitialspace = True)

    # calculate mean and std
    scaler = StandardScaler()
    scaler.fit(df[['AGE', 'INFL_HOMEAMT', 'INFL_INVAMT']])
    # year
    years = df['YYYY']
    le = LabelEncoder()  # add a default value for unseen categories
    le.fit(years)
    # Income
    scaler_y = StandardScaler()
    y_scaled=scaler_y.fit_transform(np.array(df['INCOME']).reshape(-1, 1))


    # new data
    new_df = pd.DataFrame(df.drop(['INCOME','YYYYMM', 'INFL_HOMEAMT'], axis=1).mean()).T
    new_df['INFL_HOMEAMT']=input_value

    new_data_scaled = scaler.transform(new_df[['AGE', 'INFL_HOMEAMT', 'INFL_INVAMT']])
    new_df[['AGE', 'INFL_HOMEAMT', 'INFL_INVAMT']] = new_data_scaled
    new_year = new_df['YYYY']
    def transform_new_year(new_year):
            try:
                encoded_year = le.transform(new_year)[0]
            except ValueError:
                encoded_year = years.mean()-min(years)
                print(f"Note: {new_year} is not in the training data, result maybe inaccurate.")
            return encoded_year
    new_df['YYYY'] = transform_new_year(new_year)

    X=new_df.reindex(columns=model_xgboost2.feature_names_in_)

    # 
    income_pred = model_xgboost2.predict(X)

    # inverse transform
    income_pred_unscaled = scaler_y.inverse_transform(income_pred.reshape(-1, 1)).item()

    return income_pred_unscaled