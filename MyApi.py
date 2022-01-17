import json
import requests
import datetime
import dateparser


class ApiWeather:
	def __init__(self):
		self.url = 'http://api.openweathermap.org/data/2.5/forecast?q=Damascus,Syria&appid=2d0556d73d5fa213e01ea62bd1ef892d'
		
	def callApi(self):
		response = requests.post(self.url)
		self.x=response.json()

	def gitInformation(self):
		self.FutureWeather={}
		for i in range(0,len(self.x['list'])):
			d=dateparser.parse(self.x['list'][i]['dt_txt'])
			if d.day!=datetime.datetime.now().day:
				numberDay=d.timetuple().tm_yday
				if(numberDay not in self.FutureWeather.keys()):
					self.FutureWeather[numberDay]=[ self.x['list'][i]['main']['temp_max'],  #x['list'][i]['dt_txt']
												    self.x['list'][i]['main']['temp_min'],
													self.x['list'][i]['main']['pressure'],
													self.x['list'][i]['main']['humidity'],
													self.x['list'][i]['wind']['speed'] ,1	]
				else:
					self.FutureWeather[numberDay]=[	self.FutureWeather[numberDay][0]+self.x['list'][i]['main']['temp_max'],  #x['list'][i]['dt_txt']
													self.FutureWeather[numberDay][1]+self.x['list'][i]['main']['temp_min'],
													self.FutureWeather[numberDay][2]+self.x['list'][i]['main']['pressure'],
													self.FutureWeather[numberDay][3]+self.x['list'][i]['main']['humidity'],
													self.FutureWeather[numberDay][4]+self.x['list'][i]['wind']['speed']   ,
													self.FutureWeather[numberDay][5]+1 ]
	
		for i in self.FutureWeather.keys():
			self.FutureWeather[i][0]=(self.FutureWeather[i][0]/self.FutureWeather[i][5])
			self.FutureWeather[i][1]=(self.FutureWeather[i][1]/self.FutureWeather[i][5])
			self.FutureWeather[i][2]=(self.FutureWeather[i][2]/self.FutureWeather[i][5])
			self.FutureWeather[i][3]=(self.FutureWeather[i][3]/self.FutureWeather[i][5])
			self.FutureWeather[i][4]=(self.FutureWeather[i][4]/self.FutureWeather[i][5])
			del self.FutureWeather[i][5]
		#self.FutureWeather.sort(0)	
		

	def printArray(self):
		for i in self.FutureWeather.keys():
			for number in range (1,9):
				print(i , self.FutureWeather[i][0] , self.FutureWeather[i][1] , self.FutureWeather[i][2] , self.FutureWeather[i][3] , self.FutureWeather[i][4] , number)

	def ReturnFutureWeather(self):
		PredictWeather={}
		PredictWeather=self.FutureWeather
		return PredictWeather

	def ReturnArray(self):
		PredictWeather=[]
		for i in self.FutureWeather.keys():
			for number in range (1,9):
				PredictWeather.append([i , self.FutureWeather[i][0] , self.FutureWeather[i][1] , self.FutureWeather[i][2] , self.FutureWeather[i][3] , self.FutureWeather[i][4] , number])
		return 	PredictWeather
