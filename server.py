from flask import Flask, request, jsonify,request, redirect, url_for
from recommendCrop import recommend_crop
from flask import render_template
import requests
import json
import http.client
conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('home.html')
    # return "<p>Hello, World!</p>"
@app.route('/recommend-crop', methods=['POST'])
def get_recommendation():
    # data = request.json
    print("request object is:")
    print(request.form['ph'])
    print(request.form['latitude'])
    print(request.form['longitude'])
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    ph = request.form['ph']
    N = request.form['N']
    P = request.form['P']
    K = request.form['K']
    # ph = int(request.form['ph'])
    weather  = json.loads(getWeather(latitude, longitude))
    # temperature = weather['currentWeather']['temperature']
    # humidity = weather['currentWeather']['humidity']
    temperature = weather['current']['temp_c']
    humidity = weather['current']['humidity']
    windSpeed = weather['current']['wind_kph']
    
    
    print(weather)
    print("temperature is:", temperature)
    print("humidity is:",humidity )
    print("humidity is:",windSpeed )
    # Get recommendation from your recommendation function
    try:    
        recommended_crop = recommend_crop(N,P, K, ph, temperature, humidity)
        return render_template('home.html', crop = recommended_crop, temperature = temperature, humidity = humidity, windSpeed = windSpeed)
        # return jsonify({'crop': recommended_crop})
    except Exception as e:
        print(e)


    

@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/schemes")
def schemes():
    return render_template('schemes.html')
@app.route("/community")
def community():
    return render_template('community.html')
@app.route("/community1")
def community1():
    return render_template('community/community1.html')


# @app.route("/weather")
def getWeather(latitude, longitude):
    
    headers = {
        'X-RapidAPI-Key': "620e3887c6msha79ba1c139c2a78p1cd18fjsndcfa6908bc7a",
        'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
    }

    conn.request("GET", "/current.json?q={latitude}%2C-{longitude}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return data
    # import requests

    # url = "https://easy-weather1.p.rapidapi.com/current/basic"
    # latitude = float(latitude)
    # longitude = float(longitude)
    # lat = '{:.3f}'.format(latitude)
    # long ='{:.3f}'.format(longitude)

    # querystring = {"latitude":lat,"longitude":long}

    # headers = {
    #     "X-RapidAPI-Key": "620e3887c6msha79ba1c139c2a78p1cd18fjsndcfa6908bc7a",
    #     "X-RapidAPI-Host": "easy-weather1.p.rapidapi.com"
    # }

    # response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    # return response.json()

 
    # return render_template('weather.html', data = data)


if __name__ == '__main__':
    app.run(debug=True)
