#!/usr/bin/env python

import psutil, sys

if __name__ == "__main__":
    if len (sys.argv) > 1:
        if 'cpu' in sys.argv[1]:
            cpu = psutil.cpu_times_percent(interval=1, percpu=False)
            for c in ['idle', 'user', 'guest', 'iowait', 'steal', 'system']:
                print 'system. {}: {}'.format(c,getattr(cpu, c))

        if 'mem' in sys.argv[1]:
            mem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            for c in ['total', 'used', 'free', 'buffers', 'inactive', 'cached']:
                print 'virtual {}: {}'.format(c,getattr(mem, c))

            print 'swap total {}'.format(swap.total)
            print 'swap used {}'.format(swap.used)
            print 'swap free {}'.format(swap.free)



