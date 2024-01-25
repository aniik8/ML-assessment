"""
In this assessment, there is A dash board layout with a RadioItem and a Dropdown
also a Pie chart and Bar chart
"""
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Create Dash app instance
app = dash.Dash(__name__)

# Read the wildfire data into pandas dataframe
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/\
IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')

# Extract year and month from the date column
df['Month'] = pd.to_datetime(df['Date']).dt.month_name()  # Used for the names of the months
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Layout Section of Dash
app.layout = html.Div(children=[
    # Title for the Dashboard
    html.H1('Australia Wildfire Dashboard',
             style={'textAlign': 'center', 'color': '#503D36', 'font-size': 26}),

    # Outer division
    html.Div([
        # First inner division for radio items and dropdown
        html.Div([
            # Radio items to select the region
            html.H2('Select Region:', style={'margin-right': '2em'}),
            dcc.RadioItems(
                options=[
                    {"label": "New South Wales", "value": "NSW"},
                    {"label": "Northern Territory", "value": "NT"},
                    {"label": "Queensland", "value": "QL"},
                    {"label": "South Australia", "value": "SA"},
                    {"label": "Tasmania", "value": "TA"},
                    {"label": "Victoria", "value": "VI"},
                    {"label": "Western Australia", "value": "WA"}
                ],
                value="NSW",
                id='region',
                inline=True
            ),
            # Dropdown to select year
            html.Div([
                html.H2('Select Year:', style={'margin-right': '2em'}),
                dcc.Dropdown(
                    options=[{'label': str(year), 'value': year} for year in df['Year'].unique()],
                    value=df['Year'].min(),
                    id='year'
                )
            ]),
        ]),

        # Second Inner division for adding 2 output graphs
        html.Div([
            html.Div([], id='plot1'),
            html.Div([], id='plot2')
        ], style={'display': 'flex'})
    ])
])

# Callback function to update plots based on input
@app.callback(
    [Output(component_id='plot1', component_property='children'),
     Output(component_id='plot2', component_property='children')],
    [Input(component_id='region', component_property='value'),
     Input(component_id='year', component_property='value')]
)
def reg_year_display(input_region, input_year):
    """
    Callback function to update plots based on selected region and year.

    Args:
        input_region (str): Selected region.
        input_year (int): Selected year.

    Returns:
        tuple: Tuple containing two children elements for plot1 and plot2.
    """
    # Filter data
    region_data = df[df['Region'] == input_region]
    y_r_data = region_data[region_data['Year'] == input_year]

    # Plot one - Monthly Average Estimated Fire Area
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean()
    fig1 = px.pie(values=est_data, names=est_data.index,
                  title=f"{input_region}: Monthly Average Estimated Fire Area in year {input_year}")

    # Plot two - Monthly Average Count of Pixels for Presumed Vegetation Fires
    veg_data = y_r_data.groupby('Month')['Count'].mean()
    fig2 = px.bar(x=veg_data.index, y=veg_data.values,
    title=f'{input_region}: Average Count of Pixels for Presumed \
    Vegetation Fires in year {input_year}')

    return [dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)]


if __name__ == '__main__':
    app.run_server()
