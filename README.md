# TFiller

#### 介绍
模拟输入的自动填表工具，拥有图形化UI，可以保存之前的填写结果，支持存储多表结果
最新更新已转移到仓库 [https://gitee.com/xingzhouren/tfiller](https://gitee.com/xingzhouren/tfiller)

label: 自动填表工具，批量填表

#### 软件架构
* python: 3.9
* UI: tkinter
* module: win32api

#### 安装教程
1.  `pip install -r requirements.txt`
2.  `python TFillerFree.py`

#### 使用说明
1. 下载release中的exe文件运行
2. 右栏输入框填写需要填写的内容，每空一行
3. 需要保存时在下方输入文件名，点击保存，可以看到左栏中已经出现保存的表单信息
4. 点击左栏保存的表单可以切换当前的表单并可以在右侧编辑
5. 需要删除时，选中保存的表单，点击删除
6. 点击执行，可以执行右侧表单中的自动填写，程序将在点击后3秒进行自动填写，需在3秒内将鼠标光标聚焦于需要填写的位置
7. 祝：使用愉快
