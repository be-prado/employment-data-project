# import csv
# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import scale
from sklearn.linear_model import Lasso
from sklearn.linear_model import LassoCV
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


def run_eda_analysis():
    data = pd.read_csv('./unprocessed_dataset.zip', skipinitialspace=True)  # ,low_memory=False
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

    data1 = pd.read_csv('dataset_for_ml_models.zip')
    data1['AGE'] = scale(data1['AGE'])
    data1['INFL_HOMEAMT'] = scale(data1['INFL_HOMEAMT'])
    data1['INFL_INVAMT'] = scale(data1['INFL_INVAMT'])
    data1['INCOME'] = scale(data1['INCOME'])
    data1['YYYY'] = LabelEncoder().fit_transform(data1['YYYY'])
    train, test = train_test_split(data1, test_size=0.3, random_state=1)
    x_train = train.drop(['INCOME', 'YYYYMM'], axis=1)
    y_train = train['INCOME']
    x_test = test.drop(['INCOME', 'YYYYMM'], axis=1)
    y_test = test['INCOME']

    X = x_train
    y = y_train

    lasso_reg = linear_model.Lasso(alpha=1e-2)

    lasso_reg.fit(X, y)

    y_pred = lasso_reg.predict(X)

    fig4 = px.scatter(x=y, y=y_pred)
    fig4.update_layout(
        title="Lasso Regression Fit",
        xaxis_title="True Values",
        yaxis_title="Predicted Values"
    ).update_traces(line_color="red")

    # fig4.show()

    coef_abs = lasso_reg.coef_
    fig5 = px.bar(x=coef_abs, y=x_train.columns)
    fig5.update_layout(
        title="Lasso Regression Feature Importance",
        xaxis_title="Features",
        yaxis_title="Absolute Coefficients"
    )
    # fig5.show()

    rmse = mean_squared_error(y, y_pred, squared=False)
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    print("RMSE of Lasso:", rmse)
    print("R2 score of Lasso:", r2)
    print("MSE of Lasso:", mse)

    rf_reg = RandomForestRegressor(n_estimators=100, max_depth=5)
    rf_reg.fit(X, y)
    y_pred = rf_reg.predict(X)

    fig6 = px.scatter(x=y, y=y_pred)
    fig6.update_layout(
        title="Random Forest Regression Fit",
        xaxis_title="True Values",
        yaxis_title="Predicted Values"
    ).update_traces(line_color="red")

    importances = rf_reg.feature_importances_
    fig7 = px.bar(x=importances, y=x_train.columns)
    fig7.update_layout(
        title="Random Forest Feature Importance",
        xaxis_title="Features",
        yaxis_title="Absolute Coefficients"
    )

    # fig6.show()
    # fig7.show()

    rmse1 = mean_squared_error(y, y_pred, squared=False)
    r21 = r2_score(y, y_pred)
    mse1 = mean_squared_error(y, y_pred)
    print("RMSE of Random Forest:", rmse1)
    print("R2 score of Random Forest:", r21)
    print("MSE of Random Forest:", mse1)
    return list((fig1, fig2, fig3, fig4, fig5, fig6, fig7))
