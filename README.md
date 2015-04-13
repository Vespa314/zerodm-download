zerodm-download-
================

自动获取动漫下载链接脚本。

## 食用方法

### 更新数据库
`python database.py`

![image](https://github.com/Vespa314/zerodm-download/raw/master/img/1.png)

### 获取单部动画下载地址
支持**模糊输入**，如果模糊输入用词在数据库中搜索结果唯一：
![image](https://github.com/Vespa314/zerodm-download/raw/master/img/6.png)

如果不唯一，则需要作出选择：
![image](https://github.com/Vespa314/zerodm-download/raw/master/img/2.png)

自动获取集数信息后，选择要下载的集数：
![image](https://github.com/Vespa314/zerodm-download/raw/master/img/3.png)

支持3中输入方式：
- 区间选择：2-10
- 单集下载：17
- 全部下载：all

> **注：**前两种选择方法的数字表示的是上图中的索引序号，而非集数！！请重点注意！！

下载成功：
![image](https://github.com/Vespa314/zerodm-download/raw/master/img/4.png)

查看下载链接，全文复制到迅雷即可：
![image](https://github.com/Vespa314/zerodm-download/raw/master/img/5.png)

> **注：**如果出现下载失败，往往是因为迅雷验证码拦截，打开`动画名.txt`，在尾部可以找到下载页面url，输入浏览器人工通过验证，即可继续使用此脚本下载。


### 批量下载模式
在一个txt文件中输入想要下载的动画名，同样支持模糊输入：
![image](https://github.com/Vespa314/zerodm-download/raw/master/img/7.png)

运行：`python zerodm.py xxx.txt`即可：
![image](https://github.com/Vespa314/zerodm-download/raw/master/img/9.png)

> 如果模糊输入对应一部动画，那么不需要作出选择，如上图中的`四月`,如果对应多部，那么需要分别作出选择，然后等待脚本完成即可！
