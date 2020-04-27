import io
import boto3
import os
import pandas as pd
import requests
import json
from datetime import datetime,timedelta


print("loading CheckLocation Lambda function")


def lambda_handler(event, context):
    # 1. Parse Query string params
	latitude = event['queryStringParameters']['lat']
	longitude = event['queryStringParameters']['lon']

	print('QP - latitude = ' + latitude)
	print('QP - longitude = ' + longitude)
	
	## reading data from s3
	#os.environ["AWS_ACCESS_KEY_ID"] = 'AKIAJ5JSN345HFTEPNWQ'
	#os.environ["AWS_SECRET_ACCESS_KEY"] = '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'#

	#s3_client = boto3.client('s3')
	#response = s3_client.get_object(Bucket="openaqmelb",Key="data_pm25_20200426.csv")
	#file = response["Body"]
	
	
	data_pm25 = pd.read_csv('data_pm25_20200426.csv', delimiter=",", low_memory=False)

	today = datetime.now()
	dayofweek = today.weekday()
	week = int(today.strftime("%V"))
	oneweeklag = today - timedelta(weeks=1)
	oneweeklag_week = int(oneweeklag.strftime("%V"))
	onemonthlag = today - timedelta(weeks=4)
	onemonthlag_week = int(onemonthlag.strftime("%V"))
	twomonthlag = today - timedelta(weeks=8)
	twomonthlag_week = int(twomonthlag.strftime("%V"))
	threemonthlag = today - timedelta(weeks=12)
	threemonthlag_week = int(threemonthlag.strftime("%V"))
	
	# build request URL
	url = 'https://38cvbo202m.execute-api.us-east-1.amazonaws.com/test/locationaq?lat=' + latitude + '&lon=' + longitude
	print('QP - Request URL = ' + url)

    # read request
	request = requests.get(url).json()
	request_result = request['result']
	if request_result:
		location = request_result['location']
		pm25_current = request_result['pm25']
		health_advice_current = request_result['health_advice']
		
		# Daily average pm25 data for each location - location,lat,lon,date,dayofweek,value(daily avg)
		data_pm25_daily = data_pm25.groupby(['location','date','week','dayofweek']).agg({'value': 'mean'}).reset_index()
		data_pm25_daily['date'] = pd.to_datetime(data_pm25_daily['date'])
		data_pm25_daily['date'] = data_pm25_daily['date'].dt.strftime("%Y-%m-%d")
		
		lagdata =  data_pm25_daily[((data_pm25_daily.week == oneweeklag_week) | (data_pm25_daily.week==onemonthlag_week)) & (data_pm25_daily.location==location) & (data_pm25_daily.dayofweek == dayofweek)]
		
		def healthAdvice(pm25_daily):
			if(pm25_daily<27):
				health_advice = 'Good'
			else:
				health_advice = 'Bad'
        
			return health_advice
			
		lagdata['health_advice'] = lagdata['value'].apply(healthAdvice)
		
		oneweeklag_health_advice = lagdata[lagdata['date']==oneweeklag.strftime("%Y-%m-%d")]['health_advice'].values[0]
		oneweeklag_value = lagdata[lagdata['date']==oneweeklag.strftime("%Y-%m-%d")]['value'].values[0]

		onemonthlag_health_advice = lagdata[lagdata['date']==onemonthlag.strftime("%Y-%m-%d")]['health_advice'].values[0]
		onemonthlag_value = lagdata[lagdata['date']==onemonthlag.strftime("%Y-%m-%d")]['value'].values[0]
		
		
		
		
		pastdataforcurrentweek = data_pm25_daily[((data_pm25_daily.week==onemonthlag_week) | (data_pm25_daily.week==twomonthlag_week) | (data_pm25_daily.week==threemonthlag_week)) & (data_pm25_daily.location==location)]
		
		responseObj_pastdata = {}
		weeks = pastdataforcurrentweek['week'].unique()
		counter = 0
		for week in weeks:
			weekstr = ''
			counter+=1
			if(counter == 1): 
				weekstr = 'threemonthslag'
			if(counter == 2): 
				weekstr = 'twomonthslag'
			if(counter == 3): 
				weekstr = 'onemonthslag'
            
			week_df = pastdataforcurrentweek[pastdataforcurrentweek.week==week]
			responseObj_pastdata[weekstr] = week_df.to_dict(orient='records')


		# Construct body of response
		respObj = {}
		respObj['date'] = today.date().strftime("%Y-%m-%d")
		respObj['location'] = location
		respObj['pm25_current'] = pm25_current
		respObj['health_advice_current'] = health_advice_current
		respObj['date_oneweeklag'] = oneweeklag.strftime("%Y-%m-%d")
		respObj['pm25_oneweeklag'] = oneweeklag_value
		respObj['health_advice_oneweeklag'] = oneweeklag_health_advice
		respObj['date_onemonthlag'] = onemonthlag.strftime("%Y-%m-%d")
		respObj['pm25_onemonthklag'] = onemonthlag_value
		respObj['health_advice_onemonthlag'] = onemonthlag_health_advice
		
		finalResp = {}
		
		finalResp['pastDataForCurrentWeek'] = responseObj_pastdata
		finalResp['CurrentDayInPast'] = respObj
		


		#print('QP - PM2.5 current value = ' + str(pm25_current))
		#print('QP - PM2.5 Last week = ' + str(pm25_oneweeklag))
		#print('QP - PM2.5 last month = ' + str(pm25_onemonthklag))
    # Construct body of response
	else:
		finalResp = {}
		finalResp['error'] = 'Data not retrived from source'


	# Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(finalResp)

    # 4. Return the response object
	return responseObject