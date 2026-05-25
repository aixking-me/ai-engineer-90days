import requests


def get_data(url, params=None, headers=None):
    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=5
        )

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


def main():
    url = "https://httpbin.org/headers"

    headers = {
        "Authorization": "Bearer test-token",
        "User-Agent": "Python-Student-Manager"
    }

    data = get_data(url, headers=headers)

    if data is not None:
        print(data["headers"])


if __name__ == "__main__":
    main()