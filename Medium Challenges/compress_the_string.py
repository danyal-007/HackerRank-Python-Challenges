#!/usr/bin/env python3
from itertools import groupby
if __name__ == "__main__":
    for el, el_list in groupby(input()):
        print((len(list(el_list)), int(el)), end=' ')
