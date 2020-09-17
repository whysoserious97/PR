import DataLoader
import Colecter
import Merger
import Datafilter
def getDatabase(querry):
       files=DataLoader.getData()
       # files=['File_route_2.csv', 'File_route_3.json', 'File_route_1.xml', 'File_route_12.csv', 'File_route_11.xml', 'File_route_32.csv', 'File_route_31.yml',
       # 'File_route_33.csv', 'File_route_331.csv', 'File_route_332.json', 'File_route_4.json']
       print(files)
       people=Colecter.parseData(files)
       database=Merger.merge(people)
       # f=open('database.txt','w')
       # for data in database:
       #        f.write(str(data)+'\n')
       # f.close()
       response=Datafilter.filter(database,querry)
       # print(response,database)
       return response
getDatabase('SelectColumn bitcoin_address')


