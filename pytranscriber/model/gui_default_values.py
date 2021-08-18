import json
import os

class GUI_DefaultValues(): 
    def __init__(self): 
        self.langCode = ""
        self.selectedFolder = ""
        self.outputFolder = ""
        self.loadFromFile()

    def loadFromFile(self):
        filePath = "user_data/default_values.json"
        if not os.path.isfile(filePath):
            return
        jsonStr = open(filePath,)
        jsonData = json.load(jsonStr)
        
        for propName in jsonData:
            if propName in self.__dict__:
                self.__dict__[propName] = jsonData[propName]

    def writeToFile(self):
        jsonStr = json.dumps(self.__dict__)
        if not os.path.isdir('user_data'):
            os.mkdir('user_data')        
        f = open("user_data/default_values.json", "w")
        f.write(jsonStr)
        f.close()
        return