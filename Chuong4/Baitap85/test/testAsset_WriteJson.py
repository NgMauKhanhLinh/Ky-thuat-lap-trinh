from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Asset import Asset

assets=[]
assets.append(Asset("AS1","May chieu 1",2017,18))
assets.append(Asset("AS2","May chieu 2",2017,17))
assets.append(Asset("AS3","May chieu 3",2024,25))
assets.append(Asset("AS4","May chieu 4",2019,20))
assets.append(Asset("AS5","May chieu 5",2018,10))
assets.append(Asset("AS6","May chieu 6",2018,5))
assets.append(Asset("AS7","May chieu 7",2021,50))
print("Danh sach tai san:")
for a in assets:
    print(a)
jff=JsonFileFactory()
filename="../dataset/assets.Json"
jff.write_data(assets,filename)