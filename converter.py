import PIL.ImageOps
import cv2 as cv2
from PIL import Image, ImageChops
import numpy as np

#
# from PIL import Image
# from PIL import ImageFilter
#
# # Open an already existing image
# imageObject = Image.open("jet2.jpg");
#
# # Apply sharp filter
# sharpened1 = imageObject.filter(ImageFilter.SHARPEN);
# sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);
#
#
# sharpened2.save('sharpened.jpg')

#-------------------------------------------------------------------------------


# img = Image.open("sharpened.jpg")
#
# img_pbm = img.convert('1')
# img_pbm.save('bg_removed.pbm')

# converted_img = inverted_img.convert('1')
# converted_img.save('new1.pbm')
# -----------------------------------------------------------------------------------------------------


img = Image.open("tank/tank2_new.png")

img_data = img.getdata()

lst = []
for i in img_data:
    lst.append(i[0]*0.0001925+i[1]*0.01514+i[2]*0.80991)

new_img = Image.new("1", img.size)
new_img.putdata(lst)

# To Black & White
im = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("tank4.pbm", im)

# inv_img = ImageChops.invert(new_img)

# new_img.save("tank4.pbm")


# To invert colors
# -------------------------------------------------------------------------------

# image = Image.open('jet2.pbm')
# inverted_image = PIL.ImageOps.invert(new_img)
# inverted_image.save("heli1.pbm")

# -------------------------------------------------------------------------------

# image = Image.open('heli1.pbm')
# inverted_image = PIL.ImageOps.invert(inverted_image)
# inverted_image.save("tank2.pbm")

# new = PIL.ImageOps.invert((inverted_image))
# new.save("heli1.pbm")
# inverted_image.save("heli.pbm")
