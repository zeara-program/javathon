import requests

def get(url,headers=None):
  if not headers:
    requests.get(url)
  return requests.get(url,headers=headers)

def post(url,headers=None,data=None):
  if not headers:
    return requests.post(url,data=data)
  if not data:
    print("dataが入力されていません")
  return requests.post(url,headers=headers,data=data)

def delete(url):
  return requests.delete(ur)
