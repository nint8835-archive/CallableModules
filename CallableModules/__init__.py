import sys
import inspect
import types


class CallableModule(types.ModuleType):

    def __init__(self, name, old_module, method_name):
        super(CallableModule, self).__init__(name)
        self.old_module = old_module
        self.method_name = method_name
    
    def __getattr__(self, name):
        return getattr(sys.modules[self.old_module], name)

    def __call__(self, *args, **kwargs):
        return getattr(sys.modules[self.old_module], self.method_name)(*args, **kwargs)

def patch(module_name = None, method_name = "__call__"):
    if module_name is None:
        module_name = inspect.currentframe().f_back.f_globals["__name__"]

    oldmodule = sys.modules[module_name]
    sys.modules[module_name] = CallableModule(module_name, module_name + "_OLD", method_name)
    sys.modules[module_name + "_OLD"] = oldmodule
