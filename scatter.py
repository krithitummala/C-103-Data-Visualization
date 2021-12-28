import pandas as pd
import plotly.express as px

df = pd.read_csv("covid_data.csv")

fig = px.scatter(
    df,
    x="Date",
    y="Cases",
    title="COVID Data Of Different Countries",
    color="Country",
    size_max=5
)
fig.show()