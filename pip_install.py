import os
from install_config import *


def pip_install():
    print('=======================开始安装第三方库============================\n')
    # 将要批量安装的第三方库写进一个文件，然后读取文件进行安装
    libs = []
    with open('pip_install.txt', mode='r', encoding='utf-8', newline='\n') as file:
        for line in file.readlines():
            libs.append(line.strip())

    if len(libs) <= 0:
        print('pip_install.txt 不存在第三方库配置，请使用pip install 自行安装,或者使用<conda remove -n your_env_name --all>删除虚拟环境重新安装')
        return False

    is_continue = input("need continue(y or n):\n")
    # 判断是否继续，如果不继续则退出
    if is_continue.lower() != 'y':
        return False

    print('需要安装的第三方库为:', libs)
    lib = None
    try:
        count = 0
        for lib in libs:
            count = count + 1
            print('==========================开始安装第' + str(count) + '个库:', str(lib) + '====================')
            if global_config['use_mirror'] is True:
                os.system("pip install " + lib + " -i " + global_config['mirror_url'])
            else:
                os.system("pip install " + lib + " -i https://pypi.org/simple/")
            print("==========================安装成功:\t" + str(lib) + '===============================')
    except Exception as err:
        print("安装失败\t" + str(lib) + str(err))


if __name__ == '__main__':
    pip_install()
