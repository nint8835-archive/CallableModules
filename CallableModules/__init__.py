import sys
import inspect
import types


class CallableModule(types.ModuleType):
    """
    Proxy module that implements __call__, allowing you to call the module
    """
    def __init__(self, name, method_name):
        """
        Initialize a new proxy module
        :param name: The name of the proxy module
        :param method_name: The name of the method to call on the original module
        """
        super(CallableModule, self).__init__(name)
        self._original_module = name + "_ORIGINAL"
        self._method_name = method_name

    def __getattr__(self, name):
        # Get the value from the original module
        return getattr(sys.modules[self._original_module], name)

    def __call__(self, *args, **kwargs):
        # Call the method on the original module
        return getattr(sys.modules[self._original_module], self._method_name)(*args, **kwargs)


def patch(module_name=None, method_name="__call__"):
    """
    Patches a module to allow it to be callable
    :param module_name: The name of the module
    :param method_name: The method to call when the module is called
    """
    # If no module name is provided, use the name of the module that is calling this method
    if module_name is None:
        module_name = inspect.currentframe().f_back.f_globals["__name__"]

    # Create a backup of the existing module
    original_module = sys.modules[module_name]
    # Replace the module with a proxy module that implements __call__
    sys.modules[module_name] = CallableModule(module_name, method_name)
    # Restore the original module to <module_name>_ORIGINAL
    sys.modules[module_name + "_ORIGINAL"] = original_module


def _callable_patch(module_name=None, method_name="__call__"):
    """
    Patches a module to allow it to be callable
    :param module_name: The name of the module
    :param method_name: The method to call when the module is called
    """
    # If no module name is provided, use the name of the module that is two levels back
    # This method -> proxy module -> caller module
    if module_name is None:
        module_name = inspect.currentframe().f_back.f_back.f_globals["__name__"]
    # Patch the module
    patch(module_name, method_name)


# Patch this module, so you can use a callable module to make your modules callable
patch(module_name="CallableModules", method_name="_callable_patch")
