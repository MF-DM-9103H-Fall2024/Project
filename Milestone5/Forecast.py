from dash import Dash, html, dcc, Input, Output
import joblib
import pandas as pd

# Initialize the Dash app
app = Dash(__name__)

# Load the trained model and scaler
regressor = joblib.load('./models/weather_regressor.pkl')
scaler = joblib.load('./models/weather_scaler.pkl')

# Load weather data
weather_data = pd.read_csv('./data/Cleaned_NYC_Weather_2022-2024.csv')

# Define the prediction function
def predict_tomorrow(data, scaler, model):
    # Use the last available row as input
    latest_data = data.iloc[-1][['TMAX', 'TMIN', 'AWND', 'WDF2', 'WESF', 'WESD']].values.reshape(1, -1)
    
    # Scale the input data
    latest_data_scaled = scaler.transform(latest_data)
    
    # Predict using the trained model
    prediction = model.predict(latest_data_scaled)
    
    # Return predictions as a dictionary
    return {
        'TMAX': round(prediction[0], 1),
        'TMIN': round(prediction[1], 1),
        'PRCP': round(prediction[2], 1),
        'AWND': round(prediction[3], 1)
    }

# Define the app layout
app.layout = html.Div([
    html.H1("NYC Weather Tomorrow"),
    
    html.Div(id='forecast-display', style={'font-size': '20px', 'margin': '20px 0'}),

    html.Label("Are you satisfied with the forecast?"),
    html.Div([
        html.Button('Sunny Day', id='sunny-button', n_clicks=0),
        html.Button('Rainy Day', id='rainy-button', n_clicks=0),
        html.Button('Snowy Day', id='snowy-button', n_clicks=0),
        html.Button('Windy Day', id='windy-button', n_clicks=0),
    ], style={'margin': '10px 0'}),

    html.Div(id='user-choice-display', style={'font-size': '18px', 'margin': '20px 0'}),

    dcc.Graph(id='weather-graph', animate=True),
])

# Define the callback
@app.callback(
    [Output('forecast-display', 'children'),
     Output('user-choice-display', 'children'),
     Output('weather-graph', 'figure')],
    [Input('sunny-button', 'n_clicks'),
     Input('rainy-button', 'n_clicks'),
     Input('snowy-button', 'n_clicks'),
     Input('windy-button', 'n_clicks')]
)
def update_weather(sunny_clicks, rainy_clicks, snowy_clicks, windy_clicks):
    # Get tomorrow's weather prediction
    forecast = predict_tomorrow(weather_data, scaler, regressor)
    
    # Initialize user choice message
    user_choice_message = "Default Prediction"
    
    # Adjust forecast based on button clicks
    if sunny_clicks:
        forecast['TMAX'] += 5
        forecast['PRCP'] = 0
        user_choice_message = "Enjoy the sunny day!"
    elif rainy_clicks:
        forecast['PRCP'] += 10
        user_choice_message = "Don't forget your umbrella!"
    elif snowy_clicks:
        forecast['PRCP'] += 5
        forecast['TMAX'] -= 5
        user_choice_message = "Time for a snowball fight!"
    elif windy_clicks:
        forecast['AWND'] += 5
        user_choice_message = "Hold onto your hat!"

    # Create forecast message
    forecast_message = (
        f"Tomorrow's Forecast: Max Temp: {forecast['TMAX']}°C, "
        f"Min Temp: {forecast['TMIN']}°C, Precipitation: {forecast['PRCP']} mm, "
        f"Wind Speed: {forecast['AWND']} m/s"
    )

    # Generate the graph
    figure = {
        'data': [
            {'x': ['Max Temp', 'Min Temp', 'Precipitation', 'Wind Speed'],
             'y': [forecast['TMAX'], forecast['TMIN'], forecast['PRCP'], forecast['AWND']],
             'type': 'bar', 'name': 'Weather Parameters'}
        ],
        'layout': {
            'title': 'Weather Forecast for Tomorrow',
            'xaxis': {'title': 'Parameters'},
            'yaxis': {'title': 'Values'}
        }
    }
    return forecast_message, user_choice_message, figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)