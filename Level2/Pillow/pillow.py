from PIL import Image, ImageEnhance, ImageFilter
import os

# image = Image.open('logo.png')
# box = (0, 28, 128, 100)
# region = image.crop(box)
# region.save('logo_resized.png')


# logo = Image.open('logo.png')
# new_resized = logo.resize((100,100))
# new_resized.save('logo_resized.png')

# def img_mod(image_given, filters, save=False):
#     image = Image.open(f'{image_given}.png')
#     if filters == 'Enhanced':
#         filtered = ImageEnhance.Contrast(image)
#     elif filters == 'Color':
#         filtered = ImageEnhance.Color(image)
#     elif filters == 'Brightness':
#         filtered = ImageEnhance.Brightness(image)
#     else:
#         filtered = ImageEnhance.Sharpness(image)
#
#     if save:
#         filtered.save(f'{image_given}_modified.png')
#
#     filtered.show()
# #
#
# # img_mod('dog', 'BLUR', True)
#



# def image_modifier(size, check_path, width, height):
#     path = os.listdir(check_path)
#     for fname in path:
#         if fname.__contains__('.png') or fname.__contains__('.jpg'):
#             image = Image.open(f'{check_path}\\{fname}')
#             logo = Image.open('logo_resized.png')
#             image = image.resize(size)
#             image.paste(logo, (width - logo.size[0], height - logo.size[1]), logo)
#             image.show()
#             fname.rsplit('.png')
#             image.save(f'modified_{fname}')
#
#
# width = 1000
# height = 1000
# size_photo = width, height
# temp_path = '..\\'
# folder = 'Pillow'
# path = os.path.join(temp_path, folder)
# image_modifier(size_photo, path, width, height)


# def photo_redo(val, image_given):
#     image = Image.open(image_given)
#     new_pixel = (val, val, val)
#     new_minus_pixel = (-val, -val, -val)
#     new_data = []
#     if 0 < val < 255:
#         for i in range(100000):
#             new_data.append(new_pixel)
#         image.putdata(new_data)
#         image.show()
#     elif val > 255:
#         print("Value is over 255.")
#     elif 0 > val > -255:
#         for i in range(10000):
#             new_data.append(new_minus_pixel)
#         image.putdata(new_data)
#         image.show()
#     else:
#         print("ERROR")
#
#
# #
# #
# photo_redo(300, '..\\Test\\dogo.png')


# def photo_redo(val, image_given):
#     image = Image.open(image_given)
#     new_pixel = (val, val, val)
#     new_minus_pixel = (-val, -val, -val)
#     new_data = []
#     if 0 < val < 255:
#         for i in range(100000):
#             new_data.append(new_pixel)
#         image.putdata(new_data)
#         image.show()
#     elif val > 255:
#         for i in range(100000):
#             new_data.append((0, 0, 0))
#         image.putdata(new_data)
#         image.show()
#     elif 0 > val > -255:
#         for i in range(10000):
#             new_data.append(new_minus_pixel)
#         image.putdata(new_data)
#         image.show()
#     else:
#         for i in range(100000):
#             new_data.append((255, 255, 255))
#         image.putdata(new_data)
#         image.show()
#
#
# photo_redo(-300, '..\\Test\\dogo.png')


# --------------------------------------------------STASIO-----------------------------
# from PIL import Image
# import os
#
# def get_list(folder):
#     files = os.listdir(folder)
#     images = []
#     for i in files:
#         if i.endswith(('.jpg', '.png')):
#            images.append(folder+'/'+i)
#     return images
#
# def pic_resize(pic, height):
#     im = Image.open(pic)
#     width = round(im.size[1]/im.size[0]*height)
#     im = im.resize((height, width))
#     return im
#
# def optimize_images(folder, height):
#     os.mkdir(f'{folder}/optimized')
#     logo = Image.open('logo_cropped.png')
#     pic_num = 0
#     for i in get_list(folder):
#         pic = Image.open(i)
#         pic = pic_resize(i, height)
#         logo_location = (
#             pic.size[0]-logo.size[0],
#             pic.size[1]-logo.size[1],
#             pic.size[0],
#             pic.size[1])
#         pic.paste(logo, logo_location, logo)
#         pic_num += 1
#         pic.save(f'{folder}/optimized/picture_{pic_num}.png')
#
#
# optimize_images("./", 200)


from PIL import Image
import os


# def ribos(sk):
#     if sk < 0:
#         return 0
#     elif sk > 255:
#         return 255
#     return sk
#
#
# def adjust_colors(img, r, g, b):
#     img = Image.open(img)
#     data = img.getdata()
#     new_data = []
#     for pixel in data:
#         red = ribos(pixel[0] + r)
#         green = ribos(pixel[1] + g)
#         blue = ribos(pixel[2] + b)
#         new_pixel = (red, green, blue)
#         new_data.append(new_pixel)
#
#     img.putdata(new_data)
#     return img
#
#
# new_img = adjust_colors('logo.png', 0, 0, 0)
# new_img.show()


# def turn_binary(img, r, g, b):
#     img = Image.open(img)
#     data = img.getdata()
#     new_data = []
#     black = 0, 0, 0
#     white = 255, 255, 255
#     for pixel in data:
#         if pixel[0] >= r or pixel[1] >= g or pixel[2] >= b:
#             new_data.append(black)
#         else:
#             new_data.append(white)
#
#     img.putdata(new_data)
#     return img