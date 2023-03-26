def data_cleaning():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    df = pd.read_csv("./unprocessed_dataset.zip")

    test = df[['POLAFF', 'GASPX1', "GAS1PX1", "CAR",'GOVT', 'INVAMT']]

    fter = test[(test['POLAFF'] != " ") & (test['GASPX1'] != " ") & (test["GAS1PX1"] != " ") & (test['GOVT'] != " ") & (test["INVAMT"] != 99999998)]

    fter = fter.apply(pd.to_numeric, axis=1)

    def g_recode(gas):
        r_dic = {
        1: "Go up",
        2: "Stay the same",
        3: "Go down",
        8: "Don't know",
        9: "No answer"
        }
        return r_dic.get(gas)

    def pol_recode(pol):
        r_dic = {
        1:	"Republican",
        2:	"Democrat",
        3:	"Independent",
        8:	"Don't know",
        9:	"No answer"
        }
        return r_dic.get(pol)

    def car_recode(car):
        r_dic = {
        1:	"Good",
        3:	'Pro-con',
        5:	'Bad',
        8:	"Don't Know",
        9:	'No answer'
        }
        return r_dic.get(car)
    
    def gov_recode(gov):
        r_dic = {
        1:	"Good job",
        3:	"Only fair",
        5:	"Poor job",
        8:	"Don't Know",
        9:	"No Answer"
        }
        return r_dic.get(gov)

    fter['gov'] = fter['GOVT'].apply(gov_recode)

    fter['gas_5yr'] = fter['GASPX1'].apply(g_recode)

    fter["gas_1yr"] = fter["GAS1PX1"].apply(g_recode)

    fter['recode_pol'] = fter['POLAFF'].apply(pol_recode)

    fter['veh_att'] = fter['CAR'].apply(car_recode)


    fter = fter.replace(to_replace='None', value=np.nan).dropna()

    f_long = fter.melt(id_vars = ['recode_pol', 'veh_att'],value_vars= ['gas_5yr', 'gas_1yr'], var_name="outlook_year", value_name='expectation')

    d_list = [fter, f_long]

    return d_list



def jp_figs():
    import pandas as pd
    import plotly.express as px
    d_list = data_cleaning()
    fig1 = px.density_heatmap(d_list[1], x = "recode_pol", y = "expectation", facet_col='outlook_year',
                            category_orders={'outlook_year': ['gas_1yr', 'gas_5yr']},
                            labels={"recode_pol": "Political Affiliation", "expectation":"Expectation"})
    fig2 = px.density_heatmap(d_list[1], x = "veh_att", y = "expectation", facet_col='outlook_year',
                            category_orders={'outlook_year': ['gas_1yr', 'gas_5yr']},
                            labels={"veh_att": "Vehicle Buying Attitude 1-Year Outlook", "expectation":"Expectation"})
    fig3 = px.parallel_categories(d_list[0], dimensions=['veh_att', "gas_1yr", "gas_5yr"], labels={"veh_att": "Vehicle Buying Attitude 1-Year Outlook", "gas_1yr":"Gas Price 1-Year Outlook", "gas_5yr":"Gas Price 5-Year Outlook"})
    fig4 = px.box(d_list[0], x = "gov", y = "INVAMT", labels={'gov':"Opinion of Government Economic Policy", 'INVAMT':"Total Value of Investments ($)"})

    fig_list = [fig1, fig2, fig3, fig4]
    return fig_list
