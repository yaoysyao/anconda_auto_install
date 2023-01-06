# anconda_auto_install

## anconda_auto_install(anconda python虚拟环境一键安装脚本，同时支持安装第三方库)

## 使用方法

1. 安装anconda成功后，此时电脑上已经有了基础的python环境，并且配置了全局变量，在命令行终端可以使用conda的命令，由于conda自带基础的python环境，所以可以直接使用此脚本
2. 代码中不使用任何第三方库，全部是python自带的库函数，所以只要有python基础环境就可以使用
2. 在终端运行命令 
   #### python anconda_install.py -n test_3.9.12(虚拟环境名称) -v 3.9.12(python版本) 
   即可进行安装
3. 如果需要在安装虚拟环境后同时安装一些第三方库，请在pip_install.txt中写明第三方库名和相应的版本号，
    #### 注意：此文件第一行注释不可删除,即使不安装任何第三方库也不要删除
   此文件中有两个第三方库的例子，使用前如果不需要请先删除，如果不写版本号将默认安装最新版本，镜像源使用的是清华镜像源，如果需要修改镜像源，请在pip_install.py中修改
4. 经过测试，目前支持Linux和Windows，macOS并未测试

## 如有任何问题，请在ISSUES提出