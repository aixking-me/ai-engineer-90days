import requests

url = "https://httpbin.org/get"

params = {
    "name": "Tom",
    "age": 18
}

try:
    response = requests.get(url, params=params, timeout=5)
    print(response.status_code)

    data = response.json()

    print(data["url"])
    print(data["args"])

except requests.exceptions.RequestException:
    print("请求失败，请检查网络或网址")