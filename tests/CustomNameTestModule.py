import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))

import CallableModules

test = True

def call_module(*args, **kwargs):
    return True

CallableModules.patch(method_name="call_module")