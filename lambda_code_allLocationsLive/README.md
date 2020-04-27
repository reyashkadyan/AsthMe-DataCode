# AsthMe-DataCode
Data side scripts for AsthMe app (Monash - IE FinalSem Project)

This AWS API service gets the live air quality for all locations in melbourne

Main file: handler_function.py

example usage:
https://zag12540b6.execute-api.us-east-1.amazonaws.com/test/locationslive


example response:

{
    "live": [
        {
            "location": "Alphington",
            "pm25": 5,
            "health_advice": 1
        },
        {
            "location": "Box Hill",
            "pm25": 8.1,
            "health_advice": 1
        },
        {
            "location": "Brighton",
            "pm25": 4.7,
            "health_advice": 1
        },
        {
            "location": "Brooklyn",
            "pm25": 5.6,
            "health_advice": 1
        },
        {
            "location": "Coolaroo",
            "pm25": 3.1,
            "health_advice": 1
        },
        {
            "location": "Dallas",
            "pm25": 2.1,
            "health_advice": 1
        },
        {
            "location": "Dandenong",
            "pm25": 6,
            "health_advice": 1
        },
        {
            "location": "Footscray",
            "pm25": 11,
            "health_advice": 1
        },
        {
            "location": "Macleod",
            "pm25": 5.8,
            "health_advice": 1
        },
        {
            "location": "Melbourne CBD",
            "pm25": 10.3,
            "health_advice": 1
        },
        {
            "location": "Mooroolbark",
            "pm25": 8,
            "health_advice": 1
        }
    ]
}
