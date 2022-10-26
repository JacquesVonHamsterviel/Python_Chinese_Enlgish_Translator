#!/usr/bin/env python
from flask import Flask, request
from gevent import pywsgi
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer
import warnings, requests
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
    if lan == 'ch':
        translated_text = translation(text, max_length=500)[0]['translation_text']
        return translated_text
    if lan == 'en':
        translated_text = translation_en2zh(text, max_length=500)[0]['translation_text']
        return translated_text
print('接入方式：\n1.POST传输数据到本服务，本机调用http://127.0.0.1:5690/report')
print('2.内网接入，调用http://运行服务的内网IP地址:5690/report')
print('3.外网接入，调用http://服务器公网IP:5690/report')
print('服务开启成功')
server = pywsgi.WSGIServer(('0.0.0.0', 5690), app)
server.serve_forever()
text = 'text'