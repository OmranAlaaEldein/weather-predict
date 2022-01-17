import csv
import datetime
import dateparser
import json

from MyApi import ApiWeather 
from sklearn import tree
from sklearn import metrics
from sklearn.naive_bayes import  GaussianNB
from sklearn.model_selection import train_test_split

from datetime import date,timedelta


class WeatherPredict:
	def __init__(self):
		self.filePath='merge.csv'
		self.dataset=[]
		self.output={}
		self.loadCsv()

		self.model = GaussianNB()
		GaussianNB(priors=None,var_smoothing=1e-09)
		
		self.NaiveBayesTest()
		#self.model.fit(self.dataset,self.target)

		
		

	def ReturnValue(self,word):
		if(word=='CSL Fault' or word=='ACInput'):
			return float(1)
		if(word=='FCB Mains Failure' or word=='BSC6900 GSM'):
			return float(2)
		if(word=='Mains Fail' or word=='BTS3900'):
			return float(3)
		if(word=='Mains Failure' or word=='BTS3900 WCDMA'):
			return float(4)
		if(word=='Mains Input Out of Range' or word=='Controller'):
			return float(5)
		if(word=='OML Fault' or word=='GBTS'):
			return float(6)
		if(word=='Mains'):
			return float(7)
		if(word=='MICRO BTS3900'):
			return float(8)
			

	def loadCsv(self):
		lines=csv.reader(open(self.filePath, 'r'), delimiter=",")
		self.dataset=list(lines)
		self.target=[]
		del self.dataset[0]
		for i in range(0,len(self.dataset)):
			#treatment first and last tow cell (convert it to float)
			self.dataset[i][0]=dateparser.parse(self.dataset[i][0]).timetuple().tm_yday
			self.dataset[i][len(self.dataset[i])-2]=self.ReturnValue(self.dataset[i][len(self.dataset[i])-2])			
			self.target.insert(i,self.ReturnValue(self.dataset[i][len(self.dataset[i])-1]))#self.dataset[i][len(self.dataset[i])-1]=self.ReturnValue(self.dataset[i][len(self.dataset[i])-1])
			
			#convert the rest
			for j in range(1,len(self.dataset[i])-2):
				self.dataset[i][j]=float(self.dataset[i][j])
			del self.dataset[i][len(self.dataset[i])-1]


	def NaiveBayes(self,newData):
		return self.model.predict(newData) #[[-0.8, -1, 8.0 , 7.7],[-0.48, -14, 85 , 7.5]]


	def NaiveBayesTest(self):
		X_train, X_test, y_train, y_test = train_test_split(self.dataset,self.target, test_size=0.3,random_state=109)
		self.model.fit(X_train, y_train)
		y_pred=self.model.predict(X_test)
		self.accureacy=metrics.accuracy_score(y_test, y_pred)
		print('accureacy : ',self.accureacy)

	
	def DecisionTree(self,newData):
		clf = tree.DecisionTreeClassifier()
		clf = clf.fit(self.dataset,self.target)

		clf.predict(newData)
		print(clf.predict_proba(newData))


	def work(self,newData):
		#newData=self.BuildArray(newData)
		return self.NaiveBayes(newData)
		#self.DecisionTree(newData)

	def BuildArray(self,FutureWeather):
		PredictWeather=[]
		print(FutureWeather)
		for i in FutureWeather.keys():
			for number in range (1,9):
				PredictWeather.append([i , FutureWeather[i][0] , FutureWeather[i][1] , FutureWeather[i][2] , FutureWeather[i][3] , FutureWeather[i][4] , number])
		return 	PredictWeather




	def CallApi(self):
		y=ApiWeather()
		y.callApi()
		y.gitInformation()
		test=y.ReturnFutureWeather()
		del y
		return test


	def NameError(self,numberError):
		if(numberError==1 ):
			return 'CSL Fault'
		if(numberError==2 ):
			return 'FCB Mains Failure'
		if(numberError==3 ):
			return 'Mains Fail'
		if(numberError==4 ):
			return 'Mains Failure'
		if(numberError==5 ):
			return 'Mains Input Out of Range'
		if(numberError==6 ):
			return 'OML Fault'
		


	def Predict(self,test):
		result=[]

		for dateWeather in test.keys():
			test[dateWeather][0]=test[dateWeather][0]-273.15
			test[dateWeather][1]=test[dateWeather][1]-273.15
			myData=[ [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 1],
					 [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 2],
					 [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 3],
					 [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 4],
					 [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 5],
					 [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 6],
					 [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 7],
					 [dateWeather , test[dateWeather][0],test[dateWeather][1],test[dateWeather][2],test[dateWeather][3],test[dateWeather][4] , 8] ] 
			
			z=x.work(myData)
			result.extend( [ [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'ACInput' , self.NameError(z[0])],
					 		 [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'BSC6900 GSM' , self.NameError(z[1])],
					 		 [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'BTS3900' , self.NameError(z[2])],
							 [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'BTS3900 WCDMA' , self.NameError(z[3])],
							 [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'Controller' , self.NameError(z[4])],
							 [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'GBTS' , self.NameError(z[5])],
							 [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'Mains' , self.NameError(z[6])],
							 [ (date(date.today().year, 1, 1) + timedelta(days=dateWeather)).strftime('%m/%d/%Y') , 'MICRO BTS3900' , self.NameError(z[7]) ] ] )
			

		return result



x=WeatherPredict()
print(json.dumps(x.Predict(x.CallApi())))
del x
