import json
import requests

print("loading CheckLocation Lambda function")


def lambda_handler(event, context):
    # 1. Parse Query string params
    # latitude = event['queryStringParameters']['lat']
    # longitude = event['queryStringParameters']['lon']

    # print('QP - latitude = ' + latitude)
    # print('QP - longitude = ' + longitude)
	

    # build request URL
    request_latest_url = 'https://api.openaq.org/v1/latest?parameter=pm25&city=Melbourne'
    print('QP - Request URL = ' + request_latest_url)

    # read request
    request = requests.get(url).json()
    request_results = response['results']
    if request_results:
        responseObj = {}
        for location in request_results:
            data = {}
            for param in location['measurements']:
                data[param['parameter']] = param['value']
                
            data['coordinates'] = location['coordinates']
            loc = location['location']
            responseObj[loc] = data


    if response_latest['results']:
        # Construct body of response
        transactionResponse = {}
        transactionResponse['live'] = responseObj

	# Construct body of response
    else:
        transactionResponse = {}
        transactionResponse['error'] = 'Data not retrived from source'

		
    # Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    # 4. Return the response object
    return responseObject