from PIL import Image
import subprocess


def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    subprocess.call(["tesseract", newFilePath, "./scrapping_with_python/ch11/files/output/output"])

    outputFile = open("./scrapping_with_python/ch11/files/output/output.txt", 'r')
    print(outputFile.read())
    outputFile.close()


cleanFile('./scrapping_with_python/ch11/files/text_2.png', './scrapping_with_python/ch11/files/text_2_clean.png')

