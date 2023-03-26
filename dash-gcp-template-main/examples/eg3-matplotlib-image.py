import dash
from dash import html
import pandas as pd
import seaborn as sns
import io
import matplotlib.pyplot as plt
import base64

app = dash.Dash(__name__)
server = app.server

titanic_df = sns.load_dataset('titanic')
fig = sns.catplot(x="sex", y="age", hue="survived", col="pclass", data=titanic_df, kind="bar", errorbar=None,
                  height=4, aspect=.7)

fig.set_axis_labels("", "Mean Age")

buf = io.BytesIO() # create an in-memory buffer
plt.savefig(buf, format = "png")  # save your image into this buffer
plt.close()
data = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
app.layout = html.Img(id='example', src=data)


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
