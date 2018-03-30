import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))

import CallableModules


def __call__(*args, **kwargs):
    pass


CallableModules.patch()
CallableModules.unpatch()
