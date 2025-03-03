from Chuong4_File.Pickle_File import FileUtil

list=FileUtil.loadModel("mydata.dat")
for p in list:
    print(p)
