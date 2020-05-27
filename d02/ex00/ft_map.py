def ft_map(func, iter):
    out = []
    if (not hasattr(func, '__call__') or not isinstance(iter, list)):
        print("bad arguments")
    else:
        for i in iter:
            try:
                out.append(func(i))
            except:
                print("can't use function with {}".format(i))
                return ([])
    return (out)


r = ["A", "B", "C", "D"]
r2 = [1, 2 , 3, -4]

print(ft_map((lambda x: x**2), r2))
print(ft_map((lambda x: x**2), r))
print(ft_map(abs, r2))
print(ft_map("abs", r2))