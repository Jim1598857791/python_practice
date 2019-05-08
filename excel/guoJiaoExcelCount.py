import csv


def readCSV2List( csvfile ):
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
        file.close();  # 操作完成一定要关闭


# csv_reader_1=readCSV2List('csv2\One.csv')
# csv_reader_1=csv_reader_1[:-1]

csv_reader_2=readCSV2List('csv2\Two.csv')
csv_reader_2=csv_reader_2[:-1]

# csv_reader_3=readCSV2List('csv2\Three.csv')
# csv_reader_3=csv_reader_3[:-1]

# csv_reader_Out=readCSV2List('csv2\Out.csv')
# csv_reader_Out=csv_reader_Out[:-1]
#
# # csv_reader_East=readCSV2List('csv\East.csv')
# csv_reader_Hotel=readCSV2List('csv2\Hotel.csv')
# csv_reader_Hotel=csv_reader_Hotel[:-1]
countResult=[]
for x in  csv_reader_2:
    if(x.find('中国')):
        countResult[1]= countResult[1]+1
    elif(x.find('孔')):
        countResult[2]= countResult[1]+1

