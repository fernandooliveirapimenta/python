from design_patterns.singleton.Singleton import Singleton

if __name__ == '__main__':
    s = Singleton()
    print(s)
    s = Singleton.getInstance()
    print(s)
    s = Singleton.getInstance()
    print(s)
    s = Singleton()
    print(s)
