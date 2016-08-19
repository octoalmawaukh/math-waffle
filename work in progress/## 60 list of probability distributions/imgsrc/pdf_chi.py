import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_chi(k):
    return lambda x: np.e ** (-x / 2) * 2 ** (-k / 2) / sps.gamma(k/2) * x ** (k / 2 - 1)

def main():
    rcParams['figure.figsize'] = 8, 6
    # figure(num=None,  facecolor='w', edgecolor='k')
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(0, 10, 0.01)
    k = [2, 4, 6, 8] 
    c = ['b','r','y','g']

    for kk, color in zip(k, c): 
        beta = make_chi(kk)(x)
        ax.plot(x, beta, color, linewidth=3)

    ax.grid(True)
    plt.xlim(0, 10)
    plt.ylim(0, .5)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()