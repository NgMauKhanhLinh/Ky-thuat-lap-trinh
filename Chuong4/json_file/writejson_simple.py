import json

data = {'products': []}
data['products'].append({
    'name': 'Heineken',
    'price': '$1.5',
    'slogan': 'Chỉ Có Thể Là Heineken'
})
data['products'].append({
    'name': 'Tiger',
    'price': '$1.3',
    'slogan': 'Tiger Beer - Bản Lĩnh Đàn Ông'
})
data['products'].append({
    'name': 'Sapporo',
    'price': '$1.4',
    'slogan': 'Tận Hưởng Từng Khoảnh Khắc'
})

with open('data.json', 'w', encoding='utf8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

