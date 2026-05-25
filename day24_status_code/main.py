import requests


def get_data(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            print(f"请求失败，状态码：{response.status_code}")
            return None

        try:
            data = response.json()
            return data
        except ValueError:
            print("响应内容不是合法 JSON")
            return None

    except requests.exceptions.RequestException as e:
        print("请求异常")
        print(e)
        return None


url = "https://httpbin.org/get"

params = {
    "name": "Tom",
    "age": 18
}

data = get_data(url, params)

if data is not None:
    print(data["url"])
    print(data["args"])