#gets the name of the file
filename = str(input("Type filename\nExample: 'filename.txt'\n"))

file = open(filename, "rt")

#creates de result file and checks if it already exists
try:
    open("result.txt", "x").close()
except Exception as error:
    print(error)
    
resultFile = open("result.txt", "wt")

#gets the lyrics
fileText = file.read()
file.close()

punctuationList = [" ", "!", "\n", "?", ",", ".", "(", ")", "[", "]", "{", "}", ";", ":", "/", "+", "-", "_", "="]


#buffer? for the words of the lyrics
wordString = ""

#quantity of meows per word will be put here
meowString = ""

#string that will be written in the end
writeString = ""

#writing process
for index in range(len(fileText)):
    i = fileText[index]
    if i not in punctuationList and index != len(fileText)-1:
        wordString += i
    else:
        meowString = ""
        
        roundInt = int(round(len(wordString)/3, 0))
        if roundInt == 0 and len(wordString) > 0:
            roundInt = 1
        
        for j in range(roundInt):
            if wordString[0] == wordString[0].upper():
                meowString += "Meow"
            else:
                meowString += "meow"
            
        wordString = ""
        writeString += meowString
        
        if i in punctuationList:
            writeString += i
        
resultFile.write(writeString)
resultFile.close()

#pause
input()

