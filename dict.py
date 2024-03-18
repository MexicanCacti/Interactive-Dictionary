import datetime
import json
# FIGURE OUT A WAY TO WEBSCRAPE TO GET DEFINITIONS FROM THE WEB
# word : {word, definition, [synonyms], [antonyms]}
__name__ == '__main__'

class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.synonyms = []
        self.antonyms = []



currentTime = datetime.datetime.now()

# open the settings, settings contain filepaths for text data of dictionary & list of websites to check
try :
    with open("settings.json", 'r') as json_file:
        settings = json.load(json_file)
except IOError:
    print("Error opening settings.json")
else :
    with open("settings.json", 'r') as json_file:
        settings = json.load(json_file)


def main():
    print(settings["dataFile"])
    try :
        with open(settings["dataFile"], 'r') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Error opening")
    else :
        with open(settings["dataFile"], 'r') as json_file:
            data = json.load(json_file)

    while(1):
        newWord = Word("","")
        returnType = promptInput(newWord, data) #returnType = 0 means repeat prompt, returnType = 1 means outputted word/added new word to dict/altered word
        if(returnType == 0) : continue
        elif(returnType == 1) :  
            print(f"{newWord.word}, {newWord.definition}, {newWord.synonyms} , {newWord.antonyms}")
            data[newWord.word] = [newWord.word, newWord.definition, newWord.synonyms, newWord.antonyms]
            with open(settings["dataFile"], 'w') as json_file:
                json.dump(data, json_file, indent = 4)
            print(f"""Options
                [1] : Input a new word
                [Any other input] : Exit program
                """)
        
            choice = input("Choice: ")
            try :
                choice = int(choice)
            except ValueError:
                print("Error converting choice to integer. Defaulting to -1\n")
                choice = -1
            else :
                choice = int(choice)

            if(choice == 1) : continue
            else : break
        else : break
        
    currentTime = datetime.datetime.now()
    print(f"{currentTime}\nExiting program.")


        

def promptInput(newWord, data):
    choice = -1
    while(1):
        word = input("Input word to search: ")
        newWord.word = word
        if not (word in data):
            print("That word is not in my dictionary!")
            while(not choice == 1 or not choice == 2):
                print(f"""Options
                    [1] : Create a new definition for {word}
                    [2] : Search for a different word
                    [-1] : Exit Program
                    """)
                
                choice = input("Choice: ")
                try :
                    choice = int(choice)
                except ValueError:
                    print("Error converting choice to integer. Defaulting to -1\n")
                    choice = -1
                else :
                    choice = int(choice)

                if(choice == 1) :
                    createDefinition(newWord)
                    return 1
                elif(choice == 2) : return 0
                elif(choice == -1) : return -1
                else :
                    print("Invalid choice. Repeating options.\n")
            return 1
        else :
            print("That word is in my dictionary!\nWhat would you like me to do?")
            while(1):
                print(f"""Options
                    [1] : Output definition for {word}
                    [2] : Change definition for {word}
                    [3] : Find synonyms for {word}
                    [4] : Find antonyms for {word}
                    [5] : Input new word
                    [-1] : Exit Program
                    """)
                
                choice = input("Choice: ")
                try :
                    choice = int(choice)
                except ValueError:
                    print("Error converting choice to integer. Defaulting to -1\n")
                    choice = -1
                else :
                    choice = int(choice)

                if(choice == 1) :
                    print(f"Definition: {data[word][1]}\n")
                elif(choice == 2) :
                    createDefinition(newWord)
                    return 1
                elif(choice == 3) :
                    ## here check if empty, if so then search online... maybe sep function to search online for def & for syn
                    print(f"Synonyms: {data[word][2]}\n")
                elif(choice == 4) :
                    ## here check if empty, if so then search online... maybe sep function to search online for def & for ant
                    print(f"Antonyms: {data[word][3]}\n")
                elif(choice == 5) : return 0
                elif(choice == -1) : return -1
                else :
                    print("Invalid choice. Repeating options.\n")


    # Input a word:
    # Check if word valid (Searching Algorithm)
    # output definition if valid OR say if it could not be found. Is there a way to check if a word is valid before searching?
    # the json file is just a large dictionary

    
def createDefinition(newWord):
    choice = -1
    confirm = -1
    while(not choice == 1 or not choice == 2) :
        print(f"""Options
            [1] : Find definition online for {newWord.word}
            [2] : Manually input definition for {newWord.word}
            """)
        choice = input("Choice: ")
        try :
            choice = int(choice)
        except ValueError:
            print("Error converting choice to integer. Defaulting to -1\n")
            choice = -1
        else :
            choice = int(choice)

        if(choice == 1): continue
            ## find online
        elif(choice == 2):
            while(1) :
                newWord.definition = input(f"Input a string for the definiton for {newWord.word}: ")
                print(f"Does \"{newWord.definition}\" look right?")
                print(f"""Options
                    [1] : Yes
                    [Any other input] : No
                    """)
                
                confirm = input("Choice: ")
                try :
                    confirm = int(confirm)
                except ValueError:
                    print("Error converting choice to integer. Defaulting to -1\n")
                    confirm = -1
                else :
                    confirm = int(confirm)
    
                if(confirm == 1) :
                    break
                # else while loop repeats... assuming no response
            break
        else :
            print("Invalid choice. Repeating options.\n")
    findOnline(newWord)
    

def findOnline(newWord) :
    print("Searching online")
    # if definition already exists, make sure to save before 
    # if syn/ant already exist, give option to keep
    # otherwise webscrape from list of websiteToSearch.json



if(__name__ == '__main__'):
    print("Welcome to my interactive dictionary!")
    print("It is currently: " + currentTime.strftime("%m/%d/%y %H:%M:%S"))
    main()