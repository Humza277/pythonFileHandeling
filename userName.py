# 1.
# Accept from the user some text.
# Ensure user enters something else raise an exception.
# After that write that text to a file and then read
# from this file to write# to another file simultaneously

# 2.
# Reading an image to writing to another file simultaneously
image_path = 'Ensiten.jpg' # image path for the image


class Username:

    def __init__(self):
        pass

    def readUser(self):
        with open("usertext.txt", "w+") as file:  # open up the file
            try:
                user = input("please input some text ")
                if len(user) == 0:  # if the user text is equal to zero, raise the exception
                    raise Exception
            except Exception:
                self.readUser()  # self call to the method to run again
            else:
                file.write(user)  # write waht the user said to file
                file.seek(0)  # track back to the begging of the file
                e = file.read()  # assign the vairable to read

        with open("nametext.txt", 'w') as file2:  # open up the second file
            file2.write(e)  # write to the second file

        print("Your text has been written")
        # return self.text_store

    def readImage(self):
        with open(image_path, 'rb') as image_file:  # opens the image
            image_string = image_file.read()  # appends the file to a variable
            with open("file location.png", 'wb') as dest_image:  # opens up destination file
                dest_image.write(image_string)  # writes the previous image to the current file

        print("File has been saved")


u = Username()
# u.readUser()
u.readImage()
