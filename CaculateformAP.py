import query
import Cal_mAP
import searchformAp

def getmAP():
    path='G:\作业\多媒体系统\search-picture\database\Oxford'
    list1=query.query('groundtruth/')#获取query的名字
    listpathok=query.Good_Ok('groundtruth/')[0]
    listpathgood = query.Good_Ok('groundtruth/')[1]
    for i in range(0,len(list1)):
        list1[i]=list1[i]+'.jpg'
    allap=0

    for i in range(0,len(list1)):
        list2=searchformAp.search(path+'\\'+list1[i],'Oxford')
        allap+=Cal_mAP.Cal_mAP(list2,
        'groundtruth/'+listpathok[i],
        'groundtruth/'+listpathgood[i])
    mAP=allap/len(list1)
    return mAP
getmAP()
