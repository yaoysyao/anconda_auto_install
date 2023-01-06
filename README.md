# anconda_auto_install

## anconda_auto_install(anconda python虚拟环境一键安装脚本，同时支持安装第三方库)

## 使用方法

1. 安装anconda成功后，此时电脑上已经有了基础的python环境，并且配置了全局变量，在命令行终端可以使用conda的命令，由于conda自带基础的python环境，所以可以直接使用此脚本
2. 代码中不使用任何第三方库，全部是python自带的库函数，所以只要有python基础环境就可以使用
3. 在anconda终端启动python，然后执行以下命令
   #### python anconda_install.py -n test_3.9.12(虚拟环境名称) -v 3.9.12(python版本)
   即可进行安装
4. 可在install_config.py文件中进行配置，配置是否安装第三方库以及是否使用镜像和镜像地址，如果需要在安装虚拟环境后同时安装一些第三方库，请在pip_install.txt中写明第三方库名和相应的版本号，如果不写版本号将默认安装最新版本，格式如：pandas==1.0.0
5. 镜像源使用的是清华镜像源，可以根据自己的需要修改install_config.py中的配置，进行镜像源配置，目前只支持单个镜像源
6. 经过测试，目前支持Linux和Windows，macOS并未测试

## 如有任何问题，请在ISSUES提出