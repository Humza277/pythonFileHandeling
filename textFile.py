class TextFile:
    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    def readTextFile(self):
        try:
            file = open(self.file_path, 'r')
        except Exception as e:
            print(e)
        else:

            # #self.text_storage = file.read()
            # # file = open(self.file_path, 'r')
            # # file.close()
            # #self.text_storage = file.read(3) reads charcters in the file
            # #self.text_storage = file.read()
            # self.text_storage = file.readlines()
            # print(file.tell())
            # print(file.read(1))
            # file.seek(0, 1)

            # for line in file:
            #     print(line)

            file.close()
        return self.text_storage

    def writeTextFile(self):
        file = open("writer.txt", "w")  # create and write to file
        file.write("My first python created file")
        file.close()
        file = open("writer.txt", "a+")  # appends to the created file
        file.write("\nwoo cloud")
        file.close()
        print(file.closed)
        print(file.name)
        print(file.mode)
        return self.text_storage

    def readTextFileUsingWidth(self):
        with open("menu.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage

    def writeTextFileUsingWidth(self):
        with open("writer.txt", "w+") as file:  # w+ write and read mode
            file.write("using Writer with functionality")
            print(file.tell())  # tells the current position
            file.seek(0)  # repositions the pinter to the beginning
            self.text_storage = file.read()
            return self.text_storage

    # what is a dynamically types
    # what is the different betwen stongly type and dynanically types
    # one is comiled at run time and the other is as

    def playingwithpythonosmodule(self):
        import os
        print(os.getcwd())  # get current working directory
        # os.remove("writer.txt")
        print(os.listdir())
        # os.rename("menu.txt", "order.txt")
        os.chdir("C:/Users\humza/Documents/filehandeling")
        print(os.getcwd())

        # os.mkdir("Humza")
        # os.rmdir("Humza")

    def playingwithException(self):
        try:
            file = open(self.file_path, 'r')
        except Exception as e:
            print(e)
            print("File is not present")
        else:
            self.text_storage = file.readline()
            file.close()
        finally:
            print("will run for sure!!")
            return self.text_storage

    def raiseException(self):
        try:
            firstValue = input("Enter your name")

            if (len(firstValue)) == 0:
                raise Exception
        except Exception:
            print("We do not accept empty names")

        else:
            print("Thank you for entering your name::", firstValue)
