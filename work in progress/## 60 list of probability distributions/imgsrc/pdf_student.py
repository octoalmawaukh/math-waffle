import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_beta(n):
    return lambda x: (sps.gamma((n+1)/2.0)) * (1.0 + (x*x) / n) ** (-n/2.0 - 1/2.0) * (n * np.pi) ** (-1/2.0) * (sps.gamma(n/2.0)) ** (-1)

def main():
    rcParams['figure.figsize'] = 8, 6
    # figure(num=None,  facecolor='w', edgecolor='k')
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-5, 5, 0.01)
    y = [1, 2, 5, 100]
    c = ['b','r','y','g']

    for n, color in zip(y, c): 
        beta = make_beta(n)(x)
        ax.plot(x, beta, color, linewidth=3)

    ax.grid(True)
    plt.xlim(-5, 5)
    plt.ylim(0, 0.4)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()