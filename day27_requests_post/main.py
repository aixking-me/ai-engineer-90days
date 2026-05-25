import requests


def post_data(url, payload):
    try:
        response = requests.post(url, json=payload, timeout=5)

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


url = "https://httpbin.org/post"

payload = {
    "name": "Tom",
    "age": 18,
    "message": "Hello API"
}

data = post_data(url, payload)

if data is not None:
    print(data["json"])