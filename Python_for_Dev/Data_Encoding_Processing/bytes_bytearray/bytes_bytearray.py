# a = bytes([66,67,68,69])
# print(a)

# with open("image.jpg", "rb+") as image:
#     #pointer at 0
#     image.seek(0)
#     image_data = bytes(image.read())
#     print(image_data[:10])

#     #changing the bytes
#     image_data[0] = 100
#     image.write(image_data)
    
#     image.seek(0)
#     print(image_data[:10])


with open("image.jpg", "rb+") as image:
    #pointer at 0
    image.seek(0)
    image_data = bytearray(image.read())
    print(image_data[:10])

    #changing the bytes
    image_data[0] = 100
    image.write(image_data)
     
    image.seek(0)
    print(image_data[:10])
   