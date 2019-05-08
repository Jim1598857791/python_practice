import csv
def readCSV2List(csvfile):
    try:
        file=open(csvfile,'r',encoding="GBK")# 读取以utf-8
        context = file.read() # 读取成str
        list_result=context.split("\n")#  以回车符\n分割成单独的行
        #每一行的各个元素是以【,】分割的，因此可以
        length=len(list_result)
        for i in range(length):
            list_result[i]=list_result[i].split(",")
        return list_result
    except Exception :
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();# 操作完成一定要关闭

def writeCSV(a,b):
    try:
        if b=='1':
            csvFile = open('result\ 1号.csv','a+', newline='') # 设置newline，否则两行之间会空一行
        elif b=='2':
            csvFile = open('result\ 2号.csv','a+', newline='') # 设置newline，否则两行之间会空一行
        elif b=='3':
            csvFile = open('result\ 3号.csv','a+', newline='') # 设置newline，否则两行之间会空一行
        elif b=='out':
            csvFile = open('result\校外.csv','a+', newline='') # 设置newline，否则两行之间会空一行
        elif b=='hotel':
            csvFile = open('result\济大宾馆.csv','a+', newline='') # 设置newline，否则两行之间会空一行
        elif b=='East':
            csvFile = open('result\东校区.csv','a+', newline='') # 设置newline，否则两行之间会空一行
        else:
            csvFile = open('result\R未找到.csv','a+', newline='') # 设置newline，否则两行之间会空一行
        writer = csv.writer(csvFile)
        m = len(a)
        for i in range(m):
            writer.writerow(a[i])
    except:
        print("文件写入转换失败，请检查文件路径及文件编码是否正确")
    finally:
        csvFile.close()



csv_reader_Sum=readCSV2List('csv\SummaryTableALL.csv')
csv_reader_Sum=csv_reader_Sum[:-1]

csv_reader_Sum_Name=readCSV2List('csv\SummaryTableName.csv')
csv_reader_Sum_Name=csv_reader_Sum_Name[:-1]

csv_reader_Sum_English=readCSV2List('csv\SummaryTableEnglish.csv')
csv_reader_Sum_English=csv_reader_Sum_English[:-1]

csv_reader_1=readCSV2List('csv\One.csv')
csv_reader_2=readCSV2List('csv\Two.csv')
csv_reader_3=readCSV2List('csv\Three.csv')
csv_reader_Out=readCSV2List('csv\Out.csv')
# csv_reader_East=readCSV2List('csv\East.csv')
csv_reader_Hotel=readCSV2List('csv\Hotel.csv')


print(csv_reader_1[10])
# print(csv_reader_2[10])
print(csv_reader_3[10])
# print(csv_reader_Out[10])
# print(csv_reader_East[1])
print(csv_reader_Hotel[1])


one=[]
two=[]
three=[]
out=[]
Hotel=[]
# East=[]
err=[]
for row in csv_reader_Sum_Name:
    x=csv_reader_Sum_Name.index(row)
    y=[csv_reader_Sum[x],]
    if row in csv_reader_1:
        print(row,"在1号公寓")
        one.append(x)
        writeCSV(y,'1')
    elif row in csv_reader_2:
        print(row,"在2号公寓")
        two.append(x)
        writeCSV(y,'2')
    elif row in csv_reader_3:
        print(row,"在3号公寓")
        three.append(x)
        writeCSV(y,'3')
    elif row in csv_reader_Out:
        print(row,"在校外")
        out.append(x)
        writeCSV(y,'out')
    elif row in csv_reader_Hotel:
        print(row,"在宾馆")
        Hotel.append(x)
        writeCSV(y,'hotel')
    # elif row in csv_reader_East:
    #     print(row,"在东校区")
    #     East.append(x)
    #     writeCSV(y,'East')
    elif csv_reader_Sum_English[x] in csv_reader_1 :
        print(row,"中文名查找失败;",csv_reader_Sum_English[x],",英文名成功,在1号")
        one.append(x)
        writeCSV(y,'1')
    elif csv_reader_Sum_English[x] in csv_reader_2 :
        print(row,"中文名查找失败;",csv_reader_Sum_English[x],"，英文名成功，在2号")
        two.append(x)
        writeCSV(y,'2')
    elif csv_reader_Sum_English[x] in csv_reader_3 :
        print(row,"中文名查找失败;",csv_reader_Sum_English[x],"，英文名成功，在3号")
        three.append(x)
        writeCSV(y,'3')
    elif csv_reader_Sum_English[x] in csv_reader_Out :
        print(row,"中文名查找失败;",csv_reader_Sum_English[x],"，英文名成功，在校外")
        out.append(x)
        writeCSV(y,'out')
    # elif csv_reader_Sum_English[x] in csv_reader_East :
    #     print(row,"中文名查找失败;",csv_reader_Sum_English[x],"，英文名成功，在东校区")
    #     Hotel.append(x)
    #     writeCSV(y,'hotel')
    elif csv_reader_Sum_English[x] in csv_reader_Hotel :
        print(row,"中文名查找失败;",csv_reader_Sum_English[x],"，英文名成功，在宾馆")
        Hotel.append(x)
        writeCSV(y,'hotel')
    else:
        print(row,"中文名查找失败;",csv_reader_Sum_English[x],"，英文名失败")
        err.append(x)
        writeCSV(y,'err')


print('one=',len(one),one)
print('two=',len(two),two)
print('three=',len(three),three)
print('out=',len(out),out)
print('Hotel=',len(Hotel),Hotel)
# print('East=',len(East),East)
print('err=',len(err),err)


