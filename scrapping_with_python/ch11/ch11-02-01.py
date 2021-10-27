from PIL import Image
import pytesseract


# im = Image.open('./scrapping_with_python/ch11/files/text_2.png')
im = Image.open('./scrapping_with_python/ch11/files/textBad.png')
text = pytesseract.image_to_string(im, lang='eng')
print(text)