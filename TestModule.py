from CallableModules import patch

def __call__(*args, **kwargs):
    print(args, kwargs)

a = 1
b = 2
c = 3
patch()