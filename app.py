# -*- coding: UTF-8 -*-
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from base64 import b64encode
from sys import argv
import json
import requests
import voice_recognition as voice_recognition
from mutagen.mp3 import MP3 as mp3
import pygame
import time



app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/air', methods=['GET', 'POST'])
def air():
     return render_template('air.html')

@app.route('/light', methods=['GET', 'POST'])
def light():
     return render_template('light.html')

@app.route('/tv', methods=['GET', 'POST'])
def tv():
     return render_template('tv.html')

@app.route('/air_on', methods=['GET', 'POST'])
def air_on():
     return render_template('air_on.html')

@app.route('/light_on', methods=['GET', 'POST'])
def light_on():
     return render_template('light_on.html')

@app.route('/tv_on', methods=['GET', 'POST'])
def tv_on():
     return render_template('tv_on.html')

@app.route('/result_air', methods=['GET', 'POST'])
def on_air():
    headers = {
    'authorization': 'Bearer ASjSnenmPqNqiDhj1pUJwPwyNeptsgG4-dePSvEBHfoVhu-I0Ek1G1IADCp1OKg-1dM7rT76RdnLyqOEdcyYCnJeTco69L0TZaVGPuFVg3Ys',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }
    data = '["aircon_on"]'
    response = requests.post('https://api-google.gh.auhome.au.com/smarthome/execute/commands', headers=headers, data=data)
    return render_template('result.html')

@app.route('/result_tv', methods=['GET', 'POST'])
def on_tv():
    headers = {
    'authorization': 'Bearer ASjSnenmPqNqiDhj1pUJwPwyNeptsgG4-dePSvEBHfoVhu-I0Ek1G1IADCp1OKg-1dM7rT76RdnLyqOEdcyYCnJeTco69L0TZaVGPuFVg3Ys',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }
    data = '["power"]'
    response = requests.post('https://api-google.gh.auhome.au.com/smarthome/execute/commands', headers=headers, data=data)
    return render_template('result.html')

@app.route('/result_light', methods=['GET', 'POST'])
def on_light():
    headers = {
    'authorization': 'Bearer ASjSnenmPqNqiDhj1pUJwPwyNeptsgG4-dePSvEBHfoVhu-I0Ek1G1IADCp1OKg-1dM7rT76RdnLyqOEdcyYCnJeTco69L0TZaVGPuFVg3Ys',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }
    data = '["on"]'
    response = requests.post('https://api-google.gh.auhome.au.com/smarthome/execute/commands', headers=headers, data=data)
    return render_template('result.html')

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    filename = 'Thank you.mp3' #再生したいmp3ファイル
    pygame.mixer.init()
    pygame.mixer.music.load(filename) #音源を読み込み
    mp3_length = mp3(filename).info.length #音源の長さ取得
    pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
    time.sleep(mp3_length + 0.25) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
    pygame.mixer.music.stop() #音源の長さ待ったら再生停
    return render_template('tv_on.html')

@app.route('/record', methods=['GET', 'POST'])
def send():
     global user_phrase
     user_phrase = voice_recognition.main()
     print(user_phrase)
     print(type(user_phrase))
     test = "aa"
     user_phrase = user_phrase
     return render_template('record.html',user_pharase=user_phrase, test=test)


@app.route('/answer_for_air', methods=['GET', 'POST'])
def workup_air():
    headers = {
    'authorization': 'Bearer ASjSnenmPqNqiDhj1pUJwPwyNeptsgG4-dePSvEBHfoVhu-I0Ek1G1IADCp1OKg-1dM7rT76RdnLyqOEdcyYCnJeTco69L0TZaVGPuFVg3Ys',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }
    data = '["on"]'
    response = requests.post('https://api-google.gh.auhome.au.com/smarthome/execute/commands', headers=headers, data=data)
    return render_template('result.html')

if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0', ssl_context=('open_ssl/server.crt', 'open_ssl/server.key'), threaded=True, debug=True)
    app.run(host='0.0.0.0', ssl_context=('open_ssl/server.crt', 'open_ssl/server.key'))
