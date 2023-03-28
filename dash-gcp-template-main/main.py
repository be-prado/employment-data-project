

import dash
from dash import html, Dash, dcc, Input, Output
import jpitti_eda
import anranyao_eda
import beprado_eda
import jinxinma_eda

#calls to bring in graphs
jpitti_figs = jpitti_eda.jp_figs()
anranyao_figs = anranyao_eda.run_eda_analysis()
beprado_figs = beprado_eda.run_eda_analysis()
jinxinma_figs=jinxinma_eda.run_eda_analysis()
#initializing dashboard
app = dash.Dash(__name__)
server = app.server

# starting layout

app.layout = html.Div([
    html.H1("Predicting Income Based on Variables from the UM Consumer Survey"),

    html.H2("Exploratory Data Analysis"),

    html.P('''Our group began our project by exploring the relationships between the survey variables.'''),

    ####################################################
    # JOE
    ####################################################

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

    ####################################################
    # JOE DONE
    ####################################################

    ####################################################
    # Anran
    ####################################################
    html.H4("Would the family income affect people's prediction of loan interest rate?"),

    html.P('''From the boxplot below, we can see that the average household income
      of those who expect loan interest rates to fall is lower than the income of 
      those who believe loan interest rates will "go up" or "stay the same".'''),
    dcc.Graph(
        id = 'anran_fig0',
        figure = anranyao_figs[0]
    ),
    html.H4("Would education level affect people's political affiliations?"),

    html.P('''From the bar chart below, we can see that most of the people have no preference regarding political affiliation. 
    Most of the people in Grade 17 are Democrats, comparing to Republican or Independent. Most of the people in Grade 13-17 without 
    college degree, or Grade 13-16 with college degree are Independents. 
    Most of the people in Grade 0-12 with high school diploma are Independents.'''),
    dcc.Graph(
        id = 'anran_fig1',
        figure = anranyao_figs[1]
    ),
    html.H4("What are the political affiliations among people of different ages?"),
    html.P('''From the graph below, we can see that for older people, number of Republican, Independent and Democrats are amost the same.
    However, for younger people(<40), number of Republican are less than the other two.'''),
    dcc.Graph(
        id = 'anran_fig2',
        figure = anranyao_figs[2]
    ),
    ####################################################
    # Anran Done
    ####################################################

    ####################################################
    # BERNARDO
    ####################################################

    # income correlation matrix
    html.H4("Does current economic status correlate with future economic expectation?"),

    html.P("In the graph below, the variable PAGO corresponds to personal finances a year before the survey, PEXP corresponds to the expected personal finances a year after the survey, BAGO corresponds to whether the economy was better or worse a year before the survey, and INEXQ1 corresponds to whether the family income is expected to be larger the following year."),
    dcc.Graph(
        id = 'beprado_fig0',
        figure = beprado_figs[0]
    ),
    html.P("We see that, perhaps surprisingly these variables have a low correlation."),

    # average home-buying attitude per region
    html.H4("How does home and car buying attitudes change between US regions?"),

    html.P("Below, we see the average home and car buying attitude scores for different US regions. Here, 1 corresponds to West, 2 corresponds to North Central, 3 corresponds to Northeast, 4  corresponds to South, and 6 corresponds to N/A. For the home buying attitude score, 1 corresponds to Good, 3 corresponds to Pro-con, and 5 corresponds to Bad."),
    dcc.Graph(
        id = 'beprado_fig1',
        figure = beprado_figs[1]
    ),
    html.P("We see that all US regions are pretty homogenous in terms of buying attitude and that car buying attitudes are consistently more optimistic than home buying attitudes."),

    # economic status and political opinions
    html.H4("Does economic status relate to political perceptions?"),

    html.P("Below we see a correlation table where YTL5 corresponds to income quintile, HTL5 corresponds to home value quintile, STL5 corresponds to stock investment quintile, POLAFF corresponds to political affiliation, BUS5 corresponds to whether the economy will be good or bad in the 5 years after the survey, and GOVT correponds to perception of government economic policy."),
    dcc.Graph(
        id = 'beprado_fig2',
        figure = beprado_figs[2]
    ),
    html.P("We see that the most correlated variable pairs are income quintile with home value quintile, income quintile with stock investment quintile, and economy prediction with perception of economic policy."),

    ##############################################################################
    ####### BERNARDO DONE
    ##############################################################################
    
    ##############################################################################
    ####### JINXIN
    ##############################################################################html.H4("How the mean of income change through time?"),
    html.H4("How the income change through time"),
    html.P("Below, we see the average income go through time"),
    dcc.Graph(
        id = 'jinxinma_fig1',
        figure = jinxinma_figs[0]
    ),
    html.P("We can see in general the income increase through time and continuously increase along the time, the time need to be changed befor we put this parameter into the machine learning model"),
    
    html.H4("How the income change through time in the home rent group and the home buying group"),
    html.P('Below, we draw the line of income of people who buy their home and people who rent their home'),
    dcc.Graph(
        id = 'jinxinma_fig1',
        figure = jinxinma_figs[1]
    ),
    html.P("We can see in general the income increase through time for two group of people in different speed. In the next section we want to know the difference of income increasing in two different group."),
           
    html.H4("How the income difference change differently in the two group of people(House own and House rental)"),
    html.P('Below, we draw the bar graph of  income changes between year of people who buy their home and people who rent their home'),
    dcc.Graph(
        id = 'jinxinma_fig1',
        figure = jinxinma_figs[2]
    ),
    html.P('We can see in general the people who buy a house have bigger income changes than the people who rent a house'),
    ##############################################################################
    ####### JINXIN DONE
    ##############################################################################

    html.H4('''INSERT OTHER EDA HERE'''),

    html.H2("Predictive Analytics"),

    html.H4("Research Question"),

    html.P("How accurately can we predict income based on other variables found in the survey dataset?"),

    html.H4("Feature Selection"),

    html.P('''We initially chose variables to predict income based on economic literature.
      Based on "Exploring the Factors That Influence Income and Wealth Distribution in the United States" by Gregory B. Fairchild and Aaron McKee (Journal of Poverty, 2016), we chose home value, home ownership, investment value, age, region, sex, marital status, education level, and political affiliation. 
      We felt that these variables in the dataset best captured the personal dimensions that influence income.'''),

    html.H4("Data Cleaning"),

    html.P('''For monetary variables, we decided to inflate the dollar amounts to the year 2020 so that the values were consistent.
      We did so using the cpi library, which has support for money inflation. 
      There were quite a few missing variables, which we replaced with the categorical means. 
      For example, in the home amount column, there were a lot of values of the form “9999998” and “9999999” which we concluded were missing values.
      Nominal variables like region, sex, and marital status were recoded using one-hot encoding using pandas.'''),

    html.H4("Fitting Machine Learning Models"),

    html.P('''INSERT TEXT HERE'''),

    html.H4("Model Evaluation and Selection"),

    html.P('''INSERT TEXT HERE'''),

    html.H4("Predictions with Final Model"),

    html.P('''INSERT TEXT HERE''')
    
    ])

# -

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)


