class Earth(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is not None:
            # 如果__instance为空则表示为第一次创建实例
            # 通过父类的__new__(cls)创建实例
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            # 返回上一个对象的引用
            return cls.__instance
