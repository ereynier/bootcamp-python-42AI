def ft_reduce(func, iter):
    ret = iter[0]
    if (not hasattr(func, '__call__') or not isinstance(iter, list)):
        print("bad arguments")
    else:
        for i in range(len(iter) - 1):
            try:
                ret = func(ret, iter[i + 1])
            except:
                print("can't use function with {}".format(i))
                return (None)
    return (ret)


def do_sum(x1):
    return (x1 + x1)


r = [1, 2, 3, 4]
r2 = [1]

print(ft_reduce(do_sum, r))
print(ft_reduce(do_sum, r2))