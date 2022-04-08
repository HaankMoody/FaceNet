from PIL import Image
from IPython.display import display

def show_img(path):
    img_PIL = Image.open(path, 'r')
    img_PIL.show()

