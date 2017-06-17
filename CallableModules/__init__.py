import sys
import inspect
import types


class CallableModule(types.ModuleType):

    def __init__(self, name, old_module):
        super().__init__(name)
        self.old_module = old_module
    
    def __getattr__(self, name):
        return getattr(sys.modules[self.old_module], name)

    def __call__(self, *args, **kwargs):
        return sys.modules[self.old_module].__call__(*args, **kwargs)

def patch(module_name = None):
    if module_name is None:
        module_name = inspect.currentframe().f_back.f_globals["__name__"]

    oldmodule = sys.modules[module_name]
    sys.modules[module_name] = CallableModule(module_name, module_name + "_OLD")
    sys.modules[module_name + "_OLD"] = oldmodule
