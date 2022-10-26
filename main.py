#!/usr/bin/env python
from flask import Flask, request
from gevent import pywsgi
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer
import warnings
import time
import base64

warnings.filterwarnings('ignore')
print('加载模型，请稍后。。。')
model = AutoModelWithLMHead.from_pretrained('./model/zh-en')
tokenizer = AutoTokenizer.from_pretrained('./model/zh-en')
translation = pipeline('translation_zh_to_en', model=model, tokenizer=tokenizer)
model_en2zh = AutoModelWithLMHead.from_pretrained('./model/en-zh')
tokenizer_en2zh = AutoTokenizer.from_pretrained('./model/en-zh')
translation_en2zh = pipeline('translation_en_to_zh', model=model_en2zh, tokenizer=tokenizer_en2zh)
app = Flask(__name__)

@app.route('/report', methods=['POST'])
def translate():
    text = request.form['text']
    lan = request.form['lan']
    if lan == 'zh':
        translated_text = translation(text, max_length=500)[0]['translation_text']
        #time.sleep(0.1)
        return translated_text
    if lan == 'en':
        translated_text = translation_en2zh(text, max_length=500)[0]['translation_text']
        #time.sleep(0.1)
        return translated_text
@app.route('/base64', methods=['POST'])
def base64_translate():
    text = request.form['text']
    lan = request.form['lan']
    verify_key=request.form['verify_key']
    try:
    	   text=base64.b64decode(text.encode()).decode()
    except Exception as ex:
        return "DecodeError"
    if lan == 'zh':
        translated_text = translation(text, max_length=500)[0]['translation_text']
        #time.sleep(0.1)
        return base64.b64encode((verify_key+translated_text).encode())
    if lan == 'en':
        translated_text = translation_en2zh(text, max_length=500)[0]['translation_text']
        #time.sleep(0.1)
        return base64.b64encode((verify_key+translated_text).encode())

print('服务开启成功: http://127.0.0.1:5690/report')
server = pywsgi.WSGIServer(('0.0.0.0', 5690), app)
server.serve_forever()
text = 'text'
