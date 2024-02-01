import requests
url = "https://gitee.com/QR/QrF.Python.FaceRecognition/raw/master/app.py"
response = requests.get(url)
script_content = response.text
# 执行脚本
exec(script_content)
