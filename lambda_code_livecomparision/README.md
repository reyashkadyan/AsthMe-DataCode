# AsthMe-DataCode
Data side scripts for AsthMe app (Monash - IE FinalSem Project)

This AWS API service takes in current location and returns historical trend for current week till 3 months. 


Example Usage: 
https://5fdqai2y94.execute-api.us-east-1.amazonaws.com/test/livecomparison?lat=-37.919746&lon=145.061214

Example response:

{
    "pastDataForCurrentWeek": {
        "threemonthslag": [
            {
                "location": "Brighton",
                "date": "2020-02-03",
                "week": 6,
                "dayofweek": 0,
                "value": 4.950000000000001
            },
            {
                "location": "Brighton",
                "date": "2020-02-04",
                "week": 6,
                "dayofweek": 1,
                "value": 5.927272727272728
            },
            {
                "location": "Brighton",
                "date": "2020-02-05",
                "week": 6,
                "dayofweek": 2,
                "value": 5.564166666666665
            },
            {
                "location": "Brighton",
                "date": "2020-02-06",
                "week": 6,
                "dayofweek": 3,
                "value": 43.84583333333333
            },
            {
                "location": "Brighton",
                "date": "2020-02-07",
                "week": 6,
                "dayofweek": 4,
                "value": 24.504166666666663
            },
            {
                "location": "Brighton",
                "date": "2020-02-08",
                "week": 6,
                "dayofweek": 5,
                "value": 11.020833333333334
            },
            {
                "location": "Brighton",
                "date": "2020-02-09",
                "week": 6,
                "dayofweek": 6,
                "value": 4.931666666666666
            }
        ],
        "twomonthslag": [
            {
                "location": "Brighton",
                "date": "2020-03-02",
                "week": 10,
                "dayofweek": 0,
                "value": 3.2083333333333335
            },
            {
                "location": "Brighton",
                "date": "2020-03-03",
                "week": 10,
                "dayofweek": 1,
                "value": 3.4625000000000004
            },
            {
                "location": "Brighton",
                "date": "2020-03-04",
                "week": 10,
                "dayofweek": 2,
                "value": 4.274583333333333
            },
            {
                "location": "Brighton",
                "date": "2020-03-05",
                "week": 10,
                "dayofweek": 3,
                "value": 1.3483333333333336
            },
            {
                "location": "Brighton",
                "date": "2020-03-06",
                "week": 10,
                "dayofweek": 4,
                "value": 1.611666666666667
            },
            {
                "location": "Brighton",
                "date": "2020-03-07",
                "week": 10,
                "dayofweek": 5,
                "value": 1.801666666666667
            },
            {
                "location": "Brighton",
                "date": "2020-03-08",
                "week": 10,
                "dayofweek": 6,
                "value": 1.225
            }
        ],
        "onemonthslag": [
            {
                "location": "Brighton",
                "date": "2020-03-30",
                "week": 14,
                "dayofweek": 0,
                "value": 2.3675
            },
            {
                "location": "Brighton",
                "date": "2020-03-31",
                "week": 14,
                "dayofweek": 1,
                "value": 2.7875
            },
            {
                "location": "Brighton",
                "date": "2020-04-01",
                "week": 14,
                "dayofweek": 2,
                "value": 7.0
            },
            {
                "location": "Brighton",
                "date": "2020-04-02",
                "week": 14,
                "dayofweek": 3,
                "value": 4.879166666666667
            },
            {
                "location": "Brighton",
                "date": "2020-04-03",
                "week": 14,
                "dayofweek": 4,
                "value": 1.47
            },
            {
                "location": "Brighton",
                "date": "2020-04-04",
                "week": 14,
                "dayofweek": 5,
                "value": 0.8545454545454544
            },
            {
                "location": "Brighton",
                "date": "2020-04-05",
                "week": 14,
                "dayofweek": 6,
                "value": 0.07458333333333333
            }
        ]
    },
    "CurrentDayInPast": {
        "date": "2020-04-27",
        "location": "Brighton",
        "pm25_current": 4.9,
        "health_advice_current": "Good",
        "date_oneweeklag": "2020-04-20",
        "pm25_oneweeklag": 6.245833333333333,
        "health_advice_oneweeklag": "Good",
        "date_onemonthlag": "2020-03-30",
        "pm25_onemonthklag": 2.3675,
        "health_advice_onemonthlag": "Good"
    }
}
