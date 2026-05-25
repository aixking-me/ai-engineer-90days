import requests


def get_data(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=5)

        if response.status_code != 200:
            print(f"请求失败，状态码：{response.status_code}")
            return None

        try:
            return response.json()
        except ValueError:
            print("响应内容不是合法 JSON")
            return None

    except requests.exceptions.RequestException as e:
        print("请求异常")
        print(e)
        return None


def post_data(url, payload):
    try:
        response = requests.post(url, json=payload, timeout=5)

        if response.status_code != 200:
            print(f"请求失败，状态码：{response.status_code}")
            return None

        try:
            return response.json()
        except ValueError:
            print("响应内容不是合法 JSON")
            return None

    except requests.exceptions.RequestException as e:
        print("请求异常")
        print(e)
        return None
    
get_url = "https://httpbin.org/get"
get_params = {
    "name": "Tom",
    "age": 18
}

get_result = get_data(get_url, get_params)

if get_result is not None:
    print("GET 结果：")
    print(get_result["args"])


post_url = "https://httpbin.org/post"
post_payload = {
    "message": "Hello API",
    "from": "Python"
}

post_result = post_data(post_url, post_payload)

if post_result is not None:
    print("POST 结果：")
    print(post_result["json"])