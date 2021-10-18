import requests


files = {'uploadFile': open("./scrapping_with_python/files/text_2.png", "rb")}
r = requests.post("http://pythonscraping.com/pages/processing2.php", 
                  files=files)
print(r.text)