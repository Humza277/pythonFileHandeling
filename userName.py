# 1.
# Accept from the user some text.
# Ensure user enters something else raise an exception.
# After that write that text to a file and then read
# from this file to write# to another file simultaneously

# 2.
# Reading an image to writing to another file simultaneously
image_path = 'Ensiten.jpg'
class Username:

    def __init__(self):
        pass


    def readUser(self):
        with open("usertext.txt", "w+") as file:
            try:
                user = input("please input some text ")
                if len(user) == 0:
                    raise Exception
            except Exception:
                self.readUser()
            else:
                file.write(user)
                file.seek(0)
                e = file.read()

        with open("nametext.txt", 'w') as file2:
            file2.write(e)

        print("Your text has been written")
        # return self.text_store

    def readImage(self):
        with open(image_path, 'rb') as image_file:
            image_string = image_file.read()
            with open("file location.png", 'wb') as dest_image:
                dest_image.write(image_string)


u = Username()
#u.readUser()
u.readImage()
