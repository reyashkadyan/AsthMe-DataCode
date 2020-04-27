# AsthMe-DataCode
Data side scripts for AsthMe app (Monash - IE FinalSem Project)

This API service takes in current location and fetches Air Quality data from openAQ database and sends back the response. 

Example usage: 
https://38cvbo202m.execute-api.us-east-1.amazonaws.com/test/locationaq?lat=-37.910946&lon=145.060374


Example response:
{
    "result": {
        "latitude": "-37.910946",
        "longitude": "145.060374",
        "pm25": 5.3,
        "health_advice": "Good",
        "location": "Brighton",
        "data": {
            "location": "Brighton",
            "city": "Melbourne",
            "country": "AU",
            "distance": 5481.281764570315,
            "measurements": [
                {
                    "parameter": "pm25",
                    "value": 5.3,
                    "lastUpdated": "2020-04-27T05:00:00.000Z",
                    "unit": "µg/m³",
                    "sourceName": "Australia - Victoria",
                    "averagingPeriod": {
                        "value": 1,
                        "unit": "hours"
                    }
                }
            ],
            "coordinates": {
                "latitude": -37.913548,
                "longitude": 144.998
            }
        }
    }
}
