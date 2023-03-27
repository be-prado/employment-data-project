

import dash
from dash import html, Dash, dcc, Input, Output
import jpitti_eda
import anranyao_eda

#calls to bring in graphs
jpitti_figs = jpitti_eda.jp_figs()
anranyao_figs = anranyao_eda.run_eda_analysis()
#initializing dashboard
app = dash.Dash(__name__)
server = app.server

#starting layout

app.layout = html.Div([
    html.H1("Predicting Income Based on Variables from the UM Consumer Survey"),

    html.H2("Exploratory Data Analysis"),

    html.P('''Our group began our project by exploring the relationships between the survey variables.'''),

    html.H4("How does political affiliation influence peoples' 1- and 5-year outlook on gas prices?"),

    html.P('''Given the politicization of fossil fuel use, I was curious to see if there was a relationship between these variables,
    and if there were differences between the 1- and 5- year outlooks.'''),

    dcc.Graph(
        id = 'jpitti_fig1',
        figure = jpitti_figs[0]
    ),

    html.P('''Based on the graphs, we can see that all people across all political affiliations expect gas prices to go up in 1- and 5-year outlooks.
    In both outlooks, it appears that Republicans are slightly more divided expected gas prices than Democrats. Interestingly, people from all parties appear to be more pessimistic on
    the 5-year outlook compared to the 1-year outlook.'''),

    html.H4("How do vehicle buying attitudes correspond with 1- and 5-year outlook on gas prices?"),

    html.P('''Based on the prior analysis of political affiliation and gas price outlook, I was curious to see if survey respondents had consistent opinions on vehicle buying
    and gas price outlook, and if their outlook stayed consistent across 1- and 5-year outlooks. My hypothesis was that people who think it's a good time to buy a car also expect to see gas prices rise, 
    since newer cars are more efficient to drive.'''),

    dcc.Graph(
        id = 'jpitti_fig2',
        figure = jpitti_figs[2]
    ),

    html.P('''Most respondents who believe it is a good time to buy a car also believe gas prices will rise in the near and far future.
    There were also a fair number of respondents who thought it was a bad time to buy a car and that gas prices will rise,
    which shows that people may not want to spend money on cars when they expect gas prices to rise.'''),

    html.H4("How does investment amount relate to opinion on government economic policy?"),

    html.P('''I wanted to explore this relationship to get a better understanding of how repondents' personal finances relate to their opinions on economic policy. 
    My initial hypothesis was that people with higher investment values will have a better opinion of government economic policy, since they feel safe investing in the stock market.'''),

    dcc.Graph(
        id = 'jpitti_fig3',
        figure = jpitti_figs[3]
    ),

    html.P('''Although the data has many outliers, those that have a positive opinion of government economic policy tend to have a higher investment value.'''),

    html.H4('''INSERT OTHER EDA HERE'''),

    dcc.Graph(
        id = 'anran_fig0',
        figure = anranyao_figs[0]
    ),

    dcc.Graph(
        id = 'anran_fig1',
        figure = anranyao_figs[1]
    ),

    dcc.Graph(
        id = 'anran_fig2',
        figure = anranyao_figs[2]
    ),
    #####

    html.H2("Predictive Analytics"),

    html.H4("Research Question"),

    html.P("How accurately can we predict income based on other variables found in the survey dataset?"),

    html.H4("Feature Selection"),

    html.P('''INSERT TEXT HERE'''),

    html.H4("Data Cleaning"),

    html.P('''INSERT TEXT HERE'''),

    html.H4("Fitting Machine Learning Models"),

    html.P('''INSERT TEXT HERE'''),

    html.H4("Model Evaluation and Selection"),

    html.P('''INSERT TEXT HERE'''),

    html.H4("Predictions with Final Model"),

    html.P('''INSERT TEXT HERE''')

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)