from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Asset import Asset

jff=JsonFileFactory()
filename="../dataset/assets.Json"
assets=jff.read_data(filename, Asset)
for a in assets:
    print(a)