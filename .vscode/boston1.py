import requests
url = input('输入网址:')
response = requests.get(url)
response.encoding =  'utf-8'
text = response.text
print(text)