emp1={"Ma":"NV1",
     "Ten":"Nguyễn Mậu Khánh Linh",
    "Tuoi":25}
dataset=[emp1,
         {"Ma":"NV2","Ten":"Nguyễn Thị Mai Nhung","Tuoi":27}
         ]
dataset.append({"Ma":"NV3","Ten":"Nguyễn Thắm","Tuoi":22})
print("Danh sách nhân viên:")
for emp in dataset:
    print(emp["Ha"],emp["Ten"].emp["Tuoi"])