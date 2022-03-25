class Batch:
    def __init__(self, FileName:str):
        self.filename:str = FileName
        self.__clear()
        self.__create()
        for i in ["echo off", "cls"]:
            self.__appendFile(i)

    def __splittedFileName(self):
        return self.filename.split('.')[0] + ".bat"

    def __clear(self):
        newFileName:str = self.__splittedFileName()
        open(newFileName, "w")

    def __create(self):
        newFileName:str = self.__splittedFileName()
        try:
            open(newFileName, "x").close()
            print(f"{newFileName} has been created")
        except:
            print(f"{newFileName} has not been created")

    def __appendFile(self, content:str):
        newFileName:str = self.__splittedFileName()
        f = open(newFileName, "a")
        f.write(content+"\n")
        f.close()

    def cvar(self, variableName:str, content):
        self.__appendFile(f"SET {variableName}={str(content)}")
        return f"%{variableName}%"

    def cprint(self, cvar:str):
        self.__appendFile(f"echo {cvar}")

    def cinput(self, variableName:str ,content):
        self.__appendFile(f"SET /p {variableName}={str(content)}")
        return f"%{variableName}%"
