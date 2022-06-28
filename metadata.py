'''
The image contained in the files contains precious metadata
We are seeking the location of where this was taken
'''
from exif import Image
import time

# Open image file for reading (binary mode)
with open('image.jpg', 'rb') as image_file:
  my_image = Image(image_file)

# Get Exif tags
print("GPS information and phone model")
print (my_image.gps_latitude)
print (my_image.gps_longitude)
print (my_image.model)
print ("Deleting Data...")
time.sleep(3)

#Now Lets Delete the GPS Information

my_image.gps_latitude = (0,0,0)
my_image.gps_longitude = (0,0,0)

print("Now the GPS data is gone")
print (my_image.gps_latitude)
print (my_image.gps_longitude)
print (my_image.model)

'''
You can save the image to use or upload to the internets
'''
'''
with open('modified_image.jpg', 'wb') as new_image_file:
  new_image_file.write(my_image.get_file())
'''
# reference https://github.com/TNThieding/exif/blob/master/docs/usage.rst
