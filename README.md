# Agent-Shell 「代行终端」
Simple Python Shell with powerful skills  
--小脚本,大力量!

## 使用方法:
### 1.下载所有文件
将所有文件放置于同一文件夹中.
### 2.设置环境变量
新建环境变量`ashdir`,并设置其值为本项目的绝对路径.
### 3.开始使用
运行ash.py:
```
python <文件路径>/ash.py
```
如果没有报错的话，现在就可以直接使用了!
## 功能介绍:
### .env
以下列格式编辑.env文件:
```
环境变量名@待添加的路径1
环境变量名@待添加的路径2
环境变量名@待添加的路径3
```
即可在当前Shell中使用所添加的环境变量.
注意:此方法添加的临时环境变量只能在当前Shell中使用,其他程序无效!
### .launch
以下列格式编辑.launch文件:
```
命令1
命令2
命令3
```
即可在Agent Shell启动时运行所添加的命令.
### .shortcut
以下列格式编辑.shortcut文件:
```
捷径1@命令1
捷径2@命令2
捷径3@命令3
```
即可在当前Shell中使用'捷径1','捷径2','捷径3'来快速运行对应命令.
## 已知问题
脚本实现方法为os.system()模块，  
该模块会将命令运行在单独的线程中，  
导致部分关联性命令无法正常使用，  
暂时无法修复。 
