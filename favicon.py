import requests
import os
if not os.path.exists("images"): os.makedirs("images")
url = input("enter site name \n")
try:
    response = requests.get("https://"+url+"/favicon.ico", stream=True)
except requests.exceptions.ConnectionError:
    print("check the correctness of the entered site name or internet connection")
else:
    with open("images/"+url.split(".")[0]+".jpg", "wb") as f:
        f.write(response.content)
