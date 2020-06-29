import numpy as np
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input as preprocess_input_vgg
# from keras.applications.resnet50 import ResNet50
# from keras.applications.densenet import DenseNet121
from keras.preprocessing import image
from numpy import linalg as LA


# from keras.applications.resnet50 import preprocess_input as preprocess_input_resnet
# from keras.applications.densenet import preprocess_input as preprocess_input_densenet
class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.weight = 'imagenet'
        self.pooling = 'max'
        self.model_vgg = VGG16(
            weights=self.weight,
      input_shape=(self.input_shape[0], self.input_shape[1], self.input_shape[2]),
             pooling=self.pooling, include_top=False)
        self.model_vgg.predict(np.zeros((1, 224, 224, 3)))

    '''
    Use vgg16/Resnet model to extract features
    Output normalized feature vector
    '''

    # 提取vgg16最后一层卷积特征
    def vgg_extract_feat(self, img_path):
        img = image.load_img(img_path,
        target_size=(self.input_shape[0],
                     self.input_shape[1]))#加载图片
        img = image.img_to_array(img)#转换为数组
        img = np.expand_dims(img, axis=0)#转换为np数组
        img = preprocess_input_vgg(img)#进行VGG处理
        feat = self.model_vgg.predict(img)#提取特征
        norm_feat = feat[0] / LA.norm(feat[0])#求归一化特征向量
        return norm_feat

