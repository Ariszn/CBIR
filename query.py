import os
def Good_Ok(path):
    g_list = []
    o_list = []
    for root,dirs,files in os.walk(path):
        for each in files:
            if each.endswith("good.txt"):
                g_list.append(str(each))
            if each.endswith("ok.txt"):
                o_list.append(str(each))
    return [g_list,o_list]
def query(path):
    count = 0
    list1 = []
    list2 = []
    list3 = []
    
    for root,dirs,files in os.walk(path):
        for each in files:
            if each.endswith(".txt"):
                count += 1
                if count%4==0:
                    path1 = path+"\\"+each
                    for line in open(path1, 'r'):
                        list1.append(line)
                        
    list2 = [i[5:] for i in list1]  # 去掉前五个字符“oxc1_”

    for i in list2:  # 按空格分割后取第一个元素
        tmp = []
        tmp = i.split()
        list3.append(tmp[0])

    #print(list3)
    return list3        
            

                        
