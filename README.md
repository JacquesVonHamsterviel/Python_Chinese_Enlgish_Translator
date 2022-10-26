# Python Chinese&Enlgish Offline Translator
# Python中文英文离线翻译，中英文离线翻译，中英文翻译

使用方法
（ 0.如果有需要请创建并使用虚拟环境： python -m venv Translator，进入文件夹 cd Translator，激活虚拟环境 source bin/activate 或者 call scripts/activate.bat 克隆本仓库： git clone xxx ）

1. 使用前解压model文件夹！！！

2. 使用pip/pip3安装：flask, gevent, transformers, warnings, requests

3. 接入方式：POST传输数据到本服务：http://127.0.0.1:5690/report, 详细参见test_cn_en.py 和 test_en_cn.py



How to use:

(Suggest to use Python virtual environment: python -m venv Translator, cd Transalor, source bin/activate or call scripts/activate.bat, git clone xxx)

1. Unzip the models first!!!

2. Use pip/pip3 to install: flask, gevent, transformers, warnings, requests

3. API requests: post data to http://127.0.0.1:5690/report , check detail in test_cn_en.py and test_en_cn.py

