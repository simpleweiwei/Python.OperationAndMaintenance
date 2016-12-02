import platform

# 用于获取Python相关信息


def get_python_version():
    """
    获取python版本
    :return:
    """
    return platform.python_version()


def get_python_version_tuple():
    """
    获取python版本号分割后的tuple
    :return:
    """
    return platform.python_version_tuple()


def get_python_branch():
    """
    获取python子版本信息，一般为空
    :return:
    """
    return platform.python_branch()


def get_python_build():
    """
    获取python编译号和日期
    :return:
    """
    return platform.python_build()


def get_python_compiler():
    """
    获取python编译器信息
    :return:
    """
    return platform.python_compiler()


def get_python_implementation():
    """
    获取python实现信息(解释器信息)
    :return:
    """
    return platform.python_implementation()


def get_python_revision():
    """
    获取python类型修改版信息,一般为空
    :return:
    """
    return platform.python_revision()


def main():
    print(get_python_version())
    print(get_python_version_tuple())
    print(get_python_branch())
    print(get_python_build())
    print(get_python_compiler())
    print(get_python_implementation())
    print(get_python_revision())


if __name__ == '__main__':
    main()
