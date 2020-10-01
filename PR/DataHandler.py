import DataLoader
import Colecter
import Merger
import Datafilter

def loadData():
       files=DataLoader.getData()
       print(files)
       return files

def getDatabase(querry,files):
       people=Colecter.parseData(files)
       database=Merger.merge(people)
       response=Datafilter.filter(database,querry)
       return response



