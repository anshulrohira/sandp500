import pandas as pd

df = pd.DataFrame()

def parseXMLFile(fileName , Mapping , Date):
    pass
def parseExcelFile(fileName , Mapping , Date):
    df = pd.read_excel(fileName)
    df.rename(columns=Mapping, inplace=True)
    if Date:
        df['Date'] = Date
    df.set_index("Date", inplace=True)
    df = df.sort_index(ascending=False)

    return df


def parseCSVFile(fileName , Mapping , Date):
    df = pd.read_csv(fileName)
    df.rename(columns=Mapping , inplace= True)
    if Date:
        df['Date'] = Date
    df.set_index("Date",inplace=True)
    df = df.sort_index(ascending=False)
    df = df[[['Name','Open','Close']]]
    return df