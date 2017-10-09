import requests

result = requests.get("http://roctbb.ru")

print(result.text)
