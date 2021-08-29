import pytesseract as tess
from PIL import Image
import pywhatkit as kit

tess.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

print("Instructions-- The pic you want to convert into handwritten text\n"
      "must be on the same folder with this application or it might not work\n")

ask = int(input("Press 100 if you want to write the text you want  \n"
                "OR\n"
                "Press 200 if you want to convert a file into handwritten text:  \n"))



color = input("please tell us which color do u want your text to be in(please choose between red green and black only!):  \n").lower()

red_text = 250
black_text = 250
green_text = 250





if ask == 100:
    print("Pls write the text below")
    text = input("Here:      ")
    if color == "red":
        kit.text_to_handwriting(text, rgb=(red_text, 0, 0))
        quit()

    elif color == "green":
        kit.text_to_handwriting(text, rgb=(0, green_text, 0))
        quit()

    elif color == "black":
        kit.text_to_handwriting(text, rgb=(0, 0, black_text))
        quit()


elif ask == 200:
    print("Thanks please provide the details ")
    pic = input("Enter the name of the pic :   ")

else:
    print("please choose either 100 or 200 only")





image = Image.open(pic)
fetch_text = tess.image_to_string(image)

split = fetch_text.split()

altogether = " ".join(split)
if color == "red":
    kit.text_to_handwriting(altogether, rgb=(red_text, 0, 0))
    quit()

elif color == "green":
    kit.text_to_handwriting(altogether, rgb=(0, green_text, 0))
    quit()

elif color == "black":
    kit.text_to_handwriting(altogether, rgb=(0, 0, black_text))
    quit()



