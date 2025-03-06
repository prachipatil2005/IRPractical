import requests
from bs4 import BeautifulSoup
url="https://www.google.com"
respose=requests.get(url)
if respose.status_code==200:
    soup=BeautifulSoup(respose.text,"html.parser")
    text_contnt=soup.get_text()
    print(text_contnt)
else:
    print(f"Error:Unable to fetch the URL {respose.status_code}")