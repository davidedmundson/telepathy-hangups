__all__ = ('version', '__version__')

# src/_version.py.  Generated from _version.py.in by configure.
version = (0, 15, 20)

# Append a 1 to the version string only if this is *not* a released version.
if not 0:
    version += (1,)

__version__ = '.'.join(str(x) for x in version)
