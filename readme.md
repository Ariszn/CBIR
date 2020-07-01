# 项目

基于python的keras采用Vgg16实现的一个图像检索系统。实现了一个简单的GUI界面。

# 文件

你解压之后应该会看到这样的文件夹：

--groundtruth

--extract_cnn_vgg16_keras.py

--index.py

--Main.py

--readme.md

--test.py

你需要手动建立两个文件夹，一个是database，一个是models。建立完毕后目录会变成这样：

--database

--models

--extract_cnn_vgg16_keras.py

--index.py

--Main.py

--readme.md

--test.py

# 如何添加数据集？

1.打开index.py，找到

```python
def trainh5(databasepath,h5name):
    database = databasepath
    index = 'models/'+h5name+'.h5'
    img_list = get_imlist(database)
```

将database修改为要训练的数据集的路径，(格式为X://src/temp/),将h5name修改为训练后数据的保存名字，默认保存在./models/路径下。

2.运行index.py

3.添加完毕，推荐把数据集添加到./database/文件夹下，让它有一个独立的文件夹。

# 如何运行？

1.确保你安装了python，以及Keras 、 TensorFlow 、Pillow 、 Numpy、h5py库。如果你没有安装，可以使用

```cmd
pip install X
```

来安装，X为库名称。当然，如果你在中国大陆境内，由于某些不可抗力的存在，推荐使用国内的镜像源。具体实现方法可以百度一下。

2.如果你没有训练过数据集，请先按照添加数据集的方式添加至少一个数据集。

3.运行Main.py，输入图片路径和数据集的名称，搜索，程序会返回前三匹配的图像。

# 如何进行mAP计算？

现在程序提供的mAP计算是基于Oxford数据集。换言之，你在database下必须有Oxford这个数据集，并且保证里面的内容与官方的无差异方可计算成功。当然，如果需要进行其他的mAP计算，你可以修改Cal_mAP.py、CaculateformAP.py、query.py这三个文件达到进行其他mAP计算的效果。由于代码繁琐，这里就不提供教程。如果需要注释的话可以联系维护者。

# 联系维护者

Ari:Ariharasuzune009@gmail.com