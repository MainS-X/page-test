import requests

def get_email_data():
    # 设置URL
    url = "https://mail.134300.xyz/api/v1/mailbox/df1/20250212T072406-9202"
    
    # 设置请求头
    headers = {
        "Accept": "application/json"
    }
    
    try:
        # 发送GET请求
        response = requests.get(url, headers=headers)
        
        # # 检查响应状态码
        # response.raise_for_status()
        
        # # 打印响应头信息
        # print("Status Code:", response.status_code)
        # print("\nHeaders:")
        # for header, value in response.headers.items():
        #     print(f"{header}: {value}")
            
        # 打印响应内容
        #print("\nResponse Body:")
        # print(response.json())
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    email_data = get_email_data()
    text = email_data["body"]["text"]
    print(text)
