import numpy as np
import matplotlib.pyplot as plt
from cmath import pi, exp

def fft(ys):
    N = len(ys)
    print("N:", N)
    He = dft(ys[::2])
    print("He:", He)
    Ho = dft(ys[1::2])
    print("Ho:", Ho)

    ns = np.arange(N)
    print("ns:", ns)
    W = np.exp(-1j * 2*pi * ns / N)
    print("W:", W)

    print("final result")

    print(np.tile(He, 2) + W * np.tile(Ho, 2))

    return np.tile(He, 2) + W * np.tile(Ho, 2)

def fft_better(ys):
    N = len(ys)
    print("N:", N)
    He = dft_better(ys[::2])
    print("He:", He)
    Ho = dft_better(ys[1::2])
    print("Ho:", Ho)

    ns = list(range(0, N))
    print("ns:", ns)
    W = [exp(-1j*2*pi*n/N) for n in ns]
    print("W:", W)

    odd_result = Ho+Ho
    odd_result = [odd_result[i]*my_w for i, my_w in enumerate(W)]
    print("odd_result:", odd_result)
    print("final result")
    print((He + He) + odd_result)

    return (He + He) + odd_result

def dft(xs):
    N = len(xs)
    # print("N:", N)
    ns = np.arange(N) / N
    # print("ns:", ns)
    ks = np.arange(N)
    # print("ks:", ks)
    args = np.outer(ks, ns)
    # print("args:", args)
    M = np.exp(-1j * 2 * pi * args)
    # print("M:", M)
    amps = M.dot(xs)
    # print("amps:", amps)
    return amps

def dft_better(xs):
    N = len(xs)
    # print("N:", N)
    ks = list(range(0, N))
    # print("ks:", ks)
    ns = [x/N for x in ks]
    # print("ns:", ns)
    args = []
    M =[]
    amps = []
    for i, val in enumerate(ks):
        args.append([])
        M.append([])
        currentdot = 0
        for j, val2 in enumerate(ns):
            args[i].append(val*val2)
            M[i].append(exp(-1j*2*pi*val*val2))
            currentdot += (M[i][j] * xs[j])
        amps.append(currentdot)
    # print("args:", args)
    # print("M:", M)
    # print("amps:", amps)
    return amps

if __name__ == '__main__':
    #dft([4, 4, 8, 8, 4, 4, 4, 8, 4, 4, 8, 8, 8, 4, 4, 8, 8, 4, 4, 8])
    list_ = [1, 2, 3, 4, 5, 6]
    # dft(list_)
    # dft_better(list_)
    fft(list_)
    fft_better(list_)
