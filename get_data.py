# -*- coding:utf-8 -*-
import csv
all_list=[]
with open('pred.csv', 'r',encoding='utf-8') as fp:
    #     # 使用DictReader创建的reader对象
    #     # 不会包含的那行数据
    reader = csv.DictReader(fp)
    index =1
    for line in reader:
        label = line["label"][1:-1]
        label = float(label)
        if label >= 0.5:
            data={
                'id':index,
                'label':"Dog",
            }
            index +=1
        else:
            data = {
                'id': index,
                'label': "Cat",
            }
            index += 1
        all_list.append(data)
headers = ['id', 'label']
with open('submission.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.DictWriter(fp,headers)
    # 写入表头数据的时候，需要执行writeheader函数
    writer.writeheader()
    writer.writerows(all_list)

