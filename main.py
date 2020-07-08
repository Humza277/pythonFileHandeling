# reading from and writing to files
# handel exceptions
# CSV
# assignments - add tests


from textFile import TextFile

file_path = "menu.txt"

textfileObject = TextFile(file_path)
#
# print(textfileObject.readTextFile())
#
# textfileObject.writeTextFile()
#print(textfileObject.readTextFileUsingWidth())

print(textfileObject.writeTextFileUsingWidth())

textfileObject.playingwithpythonosmodule()