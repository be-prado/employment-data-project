import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

def figure(var1, var2, data):
    fig = plt.figure()
    plt.scatter(var1, var2, data=data)
    plt.xlabel(var1)
    plt.xlabel(var2)
    return fig

def run_eda_analysis():
    df = pd.read_csv("./unprocessed_dataset.zip")
    target = df[['ICS','ICE','VEHNUM']]
    target = target.dropna()
    df['VEHNUM'] = pd.to_numeric(df['VEHNUM'],errors='coerce')
    
    target.corr()
    
    
    #customer sentiment and customer expectation
    #Assumptions: these two should be postively correlated.
    #assumption is confirmed by the graph
    fig1 = figure('ICS','ICE', data=target)
    
    #customer sentiment and customer expectation
    #Assumptions: these two should be postively correlated.
    #graph shows no correlation
    fig2 = figure('ICS','VEHNUM', data=target)
    
    #number of car owned and customer expectation
    #Assumptions: these two should be postively correlated.
    #graph shows no correlation
    fig3 = figure('ICE','VEHNUM', data=target)
    
    return (fig1, fig2, fig3)

# list = run_eda_analysis()
# for fig in list:
#     fig.show()


