import os

import h5py
import numpy as np

from extract_cnn_vgg16_keras import VGGNet


#获取文件夹中的所有图片列表
def get_imlist(path):
    return [os.path.join(path, f)
            for f in os.listdir(path) if f.endswith('.jpg')]


def trainh5(databasepath="",h5name=""):
    database = databasepath
    index = 'models/'+h5name+'.h5'
    img_list = get_imlist(database)

    print("--------------------------------------------------")
    print("                 训练集开始                        ")
    print("--------------------------------------------------")

    feats = []
    names = []

    model = VGGNet()
    for i, img_path in enumerate(img_list):
        norm_feat = model.vgg_extract_feat(img_path)  #提取特征
        img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_name)
        print("提取图片 No. %d 的特征,总共有 %d 张图片"
              % ((i + 1), len(img_list)))

    feats = np.array(feats)
    output = index
    print("--------------------------------------------------")
    print("               正在写入特征库 ...                  ")
    print("--------------------------------------------------")

    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_1', data=feats)
    h5f.create_dataset('dataset_2', data=np.string_(names))
    h5f.close()
trainh5()