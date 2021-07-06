from captcha.image import ImageCaptcha
import random, string
import os
import shutil


# randomizando as geramento de ltras
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# gerador dos arquivos
def generator(quantidade):
   image_captcha = ImageCaptcha ()
   s = 0
   for s in range(0, quantidade):
      image = image_captcha.generate_image(randomword(5))
      s += 1
      image_captcha.write(randomword(5),f'{s}.png')
      source = f'{s}.png'
      destination = 'bdcaptcha'
      shutil.move(source, destination)

generator(# quantidade desejada)

