from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        r'codecy',
        [r'code.pyx']
    ),
]

setup(
    name='codecy',
    ext_modules=cythonize(ext_modules),
)
