import json

with open('json_task_file.json', 'r') as f:
    data = json.load(f)

dic = {'colors': []}
for i in data['colors']:
    colors_dict = {'color': i['color']}
    rgba_list = i['code']['rgba']
    rgba = ''.join(str(rgba_list))[1:-4]
    colors_dict['rgb'] = rgba
    colors_dict['hex'] = i['code']['hex']
    dic['colors'].append(colors_dict)
for d in dic['colors']:
    print(d)
with open('done.json', 'w') as f:
    json.dump(dic, f, indent=2)
