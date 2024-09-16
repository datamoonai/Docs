import requests

url = "http://127.0.0.1:9394/detect"

payload = {}
files=[
  ('file_img',('full.jpg',open('../sample_images/full.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.json())