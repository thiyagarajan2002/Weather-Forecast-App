from flask import Flask, render_template,url_for,request
import requests
from datetime import datetime
app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def Home():
    return render_template('home.html')


 

#location = input("Enter the city name: ")
def getresult(location):
  complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=016cb5ed243330161c1e10d51e0658de"
  api_link = requests.get(complete_api_link)
  api_data = api_link.json()
  #create variable to store data
  temp_city = ((api_data['main']['temp']) - 273.15)
  weather_desc = api_data['weather'][0]['description']
  hmdt = api_data['main']['humidity']
  wind_spd = api_data['wind']['speed']
  date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
  ls=[]
  ls.append(temp_city)
  ls.append(hmdt)
  ls.append(weather_desc)
  ls.append(wind_spd)
  ls.append(date_time)
  return ls



@app.route("/result", methods=['POST','GET'])
def result():
  location1 = (request.form['location'])
  get_result=getresult(location1)
  return render_template('Result.html',location=location1,temperature=get_result[0],humidity=get_result[1],weather_description=get_result[2],wind_speed=get_result[3],time_date=get_result[4])
  
if __name__ == '__main__':
    app.run(debug=True)
