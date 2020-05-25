import time
import sys


def ft_progress(lst):
    t0 = time.time()
    bar = ""
    k = 0
    for i in lst:
        percent = i / abs(((lst.start - lst.stop) / lst.step))
        percent = percent * 100 + 1
        for j in range(0, int((percent * 25) / 100)):
            bar += "="
            k = j
        if (k < 24):
            bar += ">"
        t = time.time() - t0
        eta = ((100 * t) / percent) - t
        if (eta < 0):
            eta = 0
        sys.stdout.write('ETA: %.2fs [%d%%][%-25s]%d/%d \
| elapsed time %.2fs\r' % (eta, percent, bar, i + 1, lst.stop, t))
        sys.stdout.flush()
        bar = ""
        yield (i)


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
