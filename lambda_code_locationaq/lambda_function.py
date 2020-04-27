# AWS Lambda code for checking the air quality at current location

# Import Libs
import json
import requests

print("loading CheckLocation Lambda function")


def lambda_handler(event, context):
    # 1. Parse Query string params
    latitude = event['queryStringParameters']['lat']
    longitude = event['queryStringParameters']['lon']

    print('QP - latitude = ' + latitude)
    print('QP - longitude = ' + longitude)

    # build request URL
    request_latest_url = 'https://api.openaq.org/v1/latest?coordinates=' + latitude + ',' + longitude + '&radius=20000&parameter=pm25'
    print('QP - Request URL = ' + request_latest_url)

    # read request
    response_latest = requests.get(request_latest_url).json()
    if response_latest['results']:
        nearest_latest = sorted(response_latest['results'], key=lambda i: i['distance'])[0]
        nearest_latest_measurements = nearest_latest['measurements']
        pm25_current = nearest_latest_measurements[0]['value']
        location = nearest_latest['location']
        health_advice = ''

        # https://www.epa.vic.gov.au/for-community/environmental-information/air-quality/pm25-particles-in-the-air
        if (pm25_current < 27):
            health_advice = 'Good'
        elif (pm25_current >= 27 & pm25_current < 62):
            health_advice = 'Moderate'
        elif (pm25_current >= 62 & pm25_current < 97):
            health_advice = 'Poor'
        elif (pm25_current >= 97 & pm25_current < 370):
            health_advice = 'Very Poor'
        elif (pm25_current >= 370):
            health_advice = 'Hazardous'
        else:
            health_advice = 'Good'

    if response_latest['results']:
        # Construct body of response
        transactionResponse = {}
        transactionResponse['latitude'] = latitude
        transactionResponse['longitude'] = longitude
        transactionResponse['pm25'] = pm25_current
        transactionResponse['health_advice'] = health_advice
        transactionResponse['location'] = location
        transactionResponse['data'] = nearest_latest
        
        transactionResponseResult = {}
        transactionResponseResult['result'] = transactionResponse

        print('QP - PM2.5 current value = ' + str(pm25_current))
        print('QP - Health Advice = ' + health_advice)
    # Construct body of response
    else:
        transactionResponse = {}
        transactionResponse['error'] = 'Data not retrived from source'
        transactionResponseResult = {}
        transactionResponseResult['result'] = transactionResponse

    # Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponseResult)

    # 4. Return the response object
    return responseObject