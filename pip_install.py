import os


def pip_install():
    print('=======================开始安装第三方库============================\n')
    # 将要批量安装的第三方库写进一个文件，然后读取文件进行安装
    libs = []
    # 读取第三方库安装文件，进行安装，跳过第一行
    with open('pip_install.txt', mode='r', encoding='utf-8', newline='\n') as file:
        for line in file.readlines()[1:]:
            libs.append(line.strip())
    print('需要安装的第三方库为:', libs)

    if len(libs) <= 0:
        print('pip_install.txt 不存在第三方库配置，请使用pip install 自行安装,或者使用<conda remove -n your_env_name --all>删除虚拟环境重新安装')
        return False

    is_continue = input("need continue(y or n):\n")
    # 判断是否继续，如果不继续则退出
    if is_continue.lower() != 'y':
        return False

    lib = None
    try:
        count = 0
        for lib in libs:
            count = count + 1
            print('==========================开始安装第' + str(count) + '个库:', str(lib) + '====================')
            os.system("pip install " + lib + " -i https://pypi.tuna.tsinghua.edu.cn/simple/")
            print("==========================安装成功:\t" + str(lib) + '===============================')
        return True
    except Exception as err:
        print("安装失败\t" + str(lib) + str(err))
    return False


if __name__ == '__main__':
    pip_install()
