import requests
ip = '118.112.246.42'
ports = []
url = "https://api.threatbook.cn/v3/ip/query"
query = {
    "apikey": "8fe15aa3a912416381da22d2b43ffbbc228f478479794d3c828da540c9dcb3c0",

    "resource": ip
}
response = requests.request("GET", url, params=query)
if response.status_code != 200:
    print(response.text)
    exit(1)
serviceList = response.json().get("data").get(ip).get("ports")
for i in range(len(serviceList)):
    ports.append(serviceList[i].get("port"))