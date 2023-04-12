def f(x):
    return x**2


def integrate(a, b, N):
    area = 0
    dx = (b - a) / N
    
    for i in range(N):
        x = a + i*dx
        area += f(x) * dx
        
    return area