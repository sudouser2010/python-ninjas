from time import time


A = 0
B = 10
N = 20000000


# run itegration via Python integrate function
print('From Python-Only')
from code import integrate as integrate_from_python_only
t1 = time()
print(
    integrate_from_python_only(A, B, N)
)
t2 = time()
print(f'Took {t2-t1} seconds\n')


# run itegration via Cython integrate function
print('From Cython')
from codecy import integrate as integrate_from_cython
t1 = time()
print(
    integrate_from_cython(A, B, N)
)
t2 = time()
print(f'Took {t2-t1} seconds')