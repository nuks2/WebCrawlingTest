from PIL import Image
import pytesseract


image = Image.open('./scrapping_with_python/ch11/training/9ZBG3.jpg')
text = pytesseract.image_to_string(image, lang='eng')
print(text)

print('-----------------')
tessdata_dir_config = r'--tessdata-dir "/Volumes/DevHD/LearningProjects/WebCrawlingTest/scrapping_with_python/ch11/training/"'
text = pytesseract.image_to_string(image, lang='eng', config=tessdata_dir_config)
print(text)