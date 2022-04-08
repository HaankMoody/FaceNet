from PIL import Image
from IPython.display import display
from image_handling import show_img

img_PIL = Image.open(r'C:\Repositories\FaceNet\example_pictures\img_0238.webp')
#img_PIL.show()

show_img('C:\Repositories\FaceNet\example_pictures\img_0238.webp')