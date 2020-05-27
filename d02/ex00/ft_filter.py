def ft_filter(func, iter):
    out = []
    ret = 0
    if ((not hasattr(func, '__call__') and func != None) or not isinstance(iter, list)):
        print("bad arguments")
    else:
        if (func == None):
            for i in iter:
                if (i):
                    out.append(i)
        else:  
            for i in iter:
                try:
                    ret = func(i)
                    if (ret):
                        out.append(i)
                except:
                    print("can't use function with {}".format(i))
                    return ([])
    return (out)


r = [0, "A", "B", "C", "D"]
r2 = [0, 1, 2 , 3, -4]

print(ft_filter((lambda x: x % 2 == 0), r2))
print(ft_filter(None, r))
