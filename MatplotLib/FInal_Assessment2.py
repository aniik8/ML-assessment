#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
                   'IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/'
                   'historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years
year_list = list(range(1980, 2024, 1))

# Create the layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard",
            style={'textAlign': 'left', 'color': '#503D36', 'font-size': 24}),
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value='Select Statistics',
            placeholder='Select a report type'
        )
    ]),
    html.Div(dcc.Dropdown(
        id='select-year',
        options=[{'label': str(i), 'value': i} for i in year_list],
        value='select-year'
    )),
    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex'})
    ])
])

# Callbacks
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_statistics):
    """
    Callback function to update the year dropdown based on the selected statistics.

    Args:
    - selected_statistics (str): The selected statistics option.

    Returns:
    - bool: True if the dropdown should be disabled, False otherwise.
    """
    if selected_statistics == 'Yearly Statistics':
        return False
    return True

@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'),
     Input(component_id='select-year', component_property='value')]
)
def update_output_container(selected_statistics, input_year):
    """
    Callback function to update the output container based on the selected statistics and year.

    Args:
    - selected_statistics (str): The selected statistics option.
    - input_year (str): The selected year.

    Returns:
    - list: A list of Div elements containing graphs.
    """
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
        # Recession Report Statistics
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        r_chart = dcc.Graph(
            figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                           title="Average Automobile Sales fluctuation over Recession Period"))
    
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                        
        r_charttwo = dcc.Graph(figure=px.bar(average_sales, x='Vehicle_Type', y='Automobile_Sales',
                                             title='Average Number of Vehicles Sold by Type'))
   
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        r_chartthree = dcc.Graph(
            figure=px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type',
                          title="Total Expenditure by Vehicle Type"))
   
        unempl = recession_data.groupby(['Vehicle_Type', 'unemployment_rate'])['Automobile_Sales'].mean().reset_index()
        r_chartfour = dcc.Graph(
            figure=px.bar(unempl, x='Vehicle_Type', y='Automobile_Sales', color='unemployment_rate',
                          title='Effect of Unemployment Rate on Vehicle Type and Sales'))

        return [
        html.Div(className='chart-item', children=[html.Div(children=r_chart), html.Div(children=r_charttwo)],
                     style={'display': 'flex'}),
        html.Div(className='chart-item', children=[html.Div(children=r_chartthree), html.Div(children=r_chartfour)],
                     style={'display': 'flex'})
        ]

    elif (input_year and selected_statistics == 'Yearly Statistics'):
        # Yearly Report Statistics
        yearly_data = data[data['Year'] == input_year]
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        y_chartone = dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales'))
        monthly_sales = data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        y_charttwo = dcc.Graph(figure=px.line(monthly_sales, x='Month', y='Automobile_Sales',
                                            title='Total Monthly Automobile Sales')) 
        avr_vdata = yearly_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        y_chartthree = dcc.Graph(figure=px.bar(avr_vdata, x='Year', y='Automobile_Sales',
                                       title='Average Vehicles Sold by Vehicle Type in the year '
                                                 f'{input_year}'))   
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        y_chartfour = dcc.Graph(figure=px.pie(exp_data, values='Advertising_Expenditure', names='Vehicle_Type'))

        return [
        html.Div(className='chart-item', children=[html.Div(children=y_chartone), html.Div(children=y_charttwo)],
                     style={'display': 'flex'}),
        html.Div(className='chart-item', children=[html.Div(children=y_chartthree), html.Div(children=y_chartfour)],
                     style={'display': 'flex'})
        ]

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
