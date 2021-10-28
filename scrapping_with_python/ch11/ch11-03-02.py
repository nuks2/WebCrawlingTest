from urllib.request import urlretrieve
import subprocess
from PIL import Image
import pytesseract
import os

# for image in sorted(imageList):
#     urlretrieve(image, "page.jpg")
#     p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#     p.wait()
#     f = open("page.txt", "r")
#     print(f.read())

dir_path = "./scrapping_with_python/ch11/preview"

for (root, directories, files) in os.walk(dir_path):
    for file in sorted(files):
        file_path = os.path.join(root, file)
        print(file_path)
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang='eng')
        print(text)
        print('------------------------------------')