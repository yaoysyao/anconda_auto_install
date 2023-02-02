import os
import argparse
import platform

import install_config
from install_config import *

# 使用方法  python anconda_install.py -n limu_3.9.12 -v 3.9.12

parser = argparse.ArgumentParser(description='Conda install args')
parser.add_argument('--name', '-n', help='虚拟环境名称，必须参数', required=True)
parser.add_argument('--python_version', '-v', help='python 版本，必须参数', required=True)
args = parser.parse_args()


# 判断系统
def system_version():
    sys = platform.system()
    if sys.lower() == "windows".lower():
        return 0
    elif sys.lower() == "linux".lower():
        return 1
    else:
        return 2


windows_conda_activate = 'conda activate '
linux_conda_activate = 'source activate '


def create_conda_env(name, version):
    print('当前脚本版本:{0}'.format(install_config.version))
    print('==========================开始安装虚拟环境,虚拟环境名称为:' + name + ',python版本为:' + version + '==========================\n')
    try:
        os.system("conda create -n " + name + " python=" + version)
        print("=====================安装虚拟环境成功===========================\t")
        # 安装第三方库
        if global_config['install_extra_store'] is True:
            print('切换到新安装的虚拟环境中并执行脚本')
            if system_version() == 0:
                print('当前环境为Windows\t')
                os.system(windows_conda_activate + name + ' && python pip_install.py')
            elif system_version() == 1:
                print('当前环境为Linux\t')
                os.system(linux_conda_activate + name + ' && python pip_install.py')
            elif system_version() == 2:
                print('该系统既不是Windows，也不是Linux，请自行百度切换虚拟幻境和安装第三方库的方式')
                return True
            print('==========================第三方库安装成功=======================\t')
        print('==============================安装结束=============================\t')
        print('python 版本为:')
        os.system('python --version')
        return True
    except Exception as err:
        print("安装失败,异常信息为: " + str(err) + '\n')
    return False


if __name__ == '__main__':
    create_conda_env(args.name, args.python_version)
