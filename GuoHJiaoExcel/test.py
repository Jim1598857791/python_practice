import csv

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

csv_reader_2=readCSV2List('csv2\CountTest.csv')
csv_reader_2=csv_reader_2[:-1]
print(type(csv_reader_2))


# 省政府奖学金
# 济南市友城奖学金
# 中津水泥奖学金
# 交换生奖学金
# 校长奖学金

# 自费生
# 自费生小计
# 总计
zf=[]
kong=[]
sheng=[]
you=[]
shui=[]
jiao=[]
xiao=[]
zi=[]
err=[]
for x in csv_reader_2:
    print('x=', x)
    ll = csv_reader_2.index(x)
    print('index=', ll)
    ss = (','.join(x))
    if(ss.find('中国')):
        zf.append(ll)
    elif(ss.find('孔')):
        kong.append(ll)
    elif(ss.find('省')):
        sheng.append(ll)
    elif(ss.find('友')):
        you.append(ll)
    elif(ss.find('水泥')):
        shui.append(ll)
    elif(ss.find('交换')):
        jiao.append(ll)
    elif(ss.find('校长')):
        xiao.append(ll)
    elif(ss.find('自费')):
        zi.append(ll)
    else:
        err.append(ll)
print('zf=', len(zf), zf)
print('kong=', len(kong), kong)
print('sheng=', len(sheng), sheng)
print('you=', len(you), you)
print('shui=', len(shui), shui)
print('jiao=', len(jiao), jiao)
print('xiao=', len(xiao), xiao)
print('zi=', len(zi), zi)
print('err=', len(err), err)



