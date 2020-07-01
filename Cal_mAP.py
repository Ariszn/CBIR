def Cal_mAP(List, path1, path2):
    list1 = [str(i) for i in List]
    list1 = list1[1:]
    list2 = []
    for i in list1:
        tmp1 = i.split("'")
        tmp2 = tmp1[1].split('.')
        list2.append(tmp2[0])

    good = []
    ok = []
    for line in open(path1, 'r'):
         good.append(line.replace('\n', ''))
    for line in open(path2, 'r'):
        ok.append(line.replace('\n',''))
    count = 0
    ap = 0
    AP = 0
                  
    for i in range(len(list2)):
        if list2[i] in good or list2[i] in ok:
            count += 1
            ap += count/(i+1)
    if count:
        AP = ap/count
    return AP

#a =  [b'all_souls_000013.jpg', b'all_souls_000131.jpg', b'magdalen_001141.jpg', b'balliol_000066.jpg', b'all_souls_000126.jpg', b'christ_church_000450.jpg', b'christ_church_000757.jpg', b'oxford_002885.jpg', b'christ_church_001068.jpg', b'christ_church_000093.jpg', b'oxford_001753.jpg']
#path1 = "groundtruth/all_souls_1_good.txt"
#path2 = "groundtruth/all_souls_1_ok.txt"
#print(Cal_mAP(a, path1, path2))

