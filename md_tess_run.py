import pytesseract
import os

from PIL import Image

the_pages = os.listdir('./pages')

for the_page in the_pages:

    with Image.open(f"pages/{the_page}") as img:
        the_output = pytesseract.image_to_string(img,
            lang="jamie",
            config="--psm 1 --oem 3")
        img.close()

    with open(f'pages/{the_page}.txt', "a") as f:
        f.write(the_output)
        f.close()
