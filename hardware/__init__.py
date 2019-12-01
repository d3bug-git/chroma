from .broche import *
import platform
if platform.system() != 'Windows':
    from .hardware import *