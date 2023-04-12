cdef f(double x):
    return x**2


def integrate(double a, double b, int N):
    cdef int i
    cdef double area, x, dx
    
    area = 0
    dx = (b - a) / N
    
    for i in range(N):
        x = a + i*dx
        area += f(x) * dx
        
    return area