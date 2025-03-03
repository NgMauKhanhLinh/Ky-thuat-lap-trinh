def LuuFile(path):
    file = open(path, 'w', encoding='utf-8')
    file.writelines("SV001;Trần Thị Mai;1/1/2006\n")
    file.writelines("SV002;Hồ Phạm;2/2/2003\n")
    file.writelines("SV003;Phạm Hùng;3/6/2014\n")
    file.close()

LuuFile("csdlsinhvien.txt")
