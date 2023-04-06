import timeit
o=timeit.timeit('"-".join(str(n) for n in range(100))', number=100000); 
print(o)