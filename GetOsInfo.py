import platform

# 用于获取服务器相关信息


def get_os_system():
    """
    获取操作系统类型
    :return:
    """
    return platform.system()


def get_os_name():
    """
    获取操作系统名
    :return:
    """
    pf = platform.platform()
    if pf.startswith("Linux"):
        return "LINUX"
    elif pf.startswith("Windows-2003"):
        return "Windows2003"
    elif pf.startswith("Windows-2008"):
        return "Windows2008"
    else:
        return pf


def get_os_version():
    """
    获取操作系统版本
    :return:
    """
    return platform.version()


def get_os_release():
    """
    获取操作系统发布号, 例如win 7返回7
    :return:
    """
    return platform.release()


def get_os_architecture():
    """
    获取操作系统位数
    :return:
    """
    return platform.architecture()


def get_machine():
    """
    获取cpu平台类型
    :return:
    """
    return platform.machine()


def get_node():
    """
    获取节点名，即机器名字
    :return:
    """
    return platform.node()


def get_processor():
    """
    获取cpu相关信息
    :return:
    """
    return platform.processor()


def get_uname():
    """
    汇总信息
    :return:
    """
    return platform.uname()


def main():
    print(get_os_system())
    print(get_os_name())
    print(get_os_version())
    print(get_os_release())
    print(get_os_architecture())
    print(get_machine())
    print(get_node())
    print(get_processor())
    print(get_uname())


if __name__ == '__main__':
    main()
