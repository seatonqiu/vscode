from PIL import Image
import os
import os.path
img = Image.open(r"F:\code\vscode\change_resolution\camera0.jpg")
out = img.resize((96,96), Image.ANTIALIAS)
out.save(r'F:\code\vscode\change_resolution\out1.jpg')
