import numpy as np
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_weibull(k, lam):
    return lambda x: np.e ** (- (x / lam) ** k) * k / lam * (x / lam) ** (k - 1)

def main():
    rcParams['figure.figsize'] = 8, 6
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(0, 2.5, 0.01)
    l = [1, 1, 1, 1] 
    k = [0.5, 1, 1.5, 5] 
    c = ['b','r','y','g']

    for kk, lam, color in zip(k, l, c): 
        gauss = make_weibull(kk, lam)(x)
        ax.plot(x, gauss, color, linewidth=3)

    ax.grid(True)
    plt.xlim(0, 2.5)
    plt.ylim(0, 2.5)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()