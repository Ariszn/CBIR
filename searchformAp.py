import h5py
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from extract_cnn_vgg16_keras import VGGNet


def search(querypath, h5name):
    # 要搜的原图path，h5文件的name，原数据集的path
    query = querypath
    index = 'models/' + h5name + '.h5'
    result = 'database/' + h5name + '/'
    h5f = h5py.File(index, 'r')
    feats = h5f['dataset_1'][:]
    imgNames = h5f['dataset_2'][:]
    h5f.close()


    # read  query image
    queryImg = mpimg.imread(query)
    # 初始化 VGGNet16 模块
    model = VGGNet()
    #提取query图片的特征
    queryVec = model.vgg_extract_feat(query)
    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]
    # 检索出三张相似度最高的图片
    maxres = 11
    imlist = []
    # 输出相似度
    for i, index in enumerate(rank_ID[0:maxres]):
        imlist.append(imgNames[index])
        #print("image names: " +
         #     str(imgNames[index]) +
          #    " scores: %f"
           #   % rank_score[i])
    #print("top %d images in order are: " % maxres, imlist)
    # 输出前三张
    return imlist
