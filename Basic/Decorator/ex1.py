def hello():
    print("hello")


def deco(fn):
    def deco_hello():
        print("*" * 20)
        fn()
        print("*" * 20)

    return deco_hello
