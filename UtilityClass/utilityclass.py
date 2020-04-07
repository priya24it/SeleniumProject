import logging
import inspect
import pandas as pd

class commonclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    @staticmethod
    def getTestdatatocreateaccount():
        #dataframe = pd.read_excel("Testdata\\testdata.xlsx")
       # dataframe = pd.DataFrame(dataframe)
        dict ="priya"
        dict = str(dict)
        i = len(dict)
        dict = dict[1:i - 1]
        dict = dict.replace("[", "(")
        dict = dict.replace("]", ")")
       # dict = "[" + dict + "]"
        #print(dict)
        return [dict]
