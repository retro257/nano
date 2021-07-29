from bs4 import BeautifulSoup
import requests

a = open("a.txt", "w")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
num = 1

while True:
    
    num += 1
    req = requests.get("https://www.thebluebook.com/search.html?region=45&searchsrc=thebluebook&class=0180&searchTerm=Architectural+%26+Cabinet+Woodwork&page={num}", headers=headers)
    if "The Blue Book Building & Construction Network  - Captcha" in req.text:
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path="/home/vaz1m/dr/chromedriver")
        driver.get("https://www.thebluebook.com/search.html?region=45&searchsrc=thebluebook&class=0180&searchTerm=Architectural+%26+Cabinet+Woodwork&page={num}")
        from Xlib import X
        from Xlib.display import Display
        from Xlib.ext.xtest import fake_input
        d = Display()
        d.warp_pointer(0, 0)
        fake_input(d, X.ButtonPress, 1)
        d.sync()
        driver.quit()
    print(req)
    print(req.status_code)
    if req.status_code != 200:
        break

    pars = BeautifulSoup(req.text, "html.parser")

    a.write(req.text)

    print(pars.find_all("a", class_="cname"))

