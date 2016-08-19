import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_beta(a, b):
    return lambda x: (a * x / (a * x + b)) ** (0.5 * a) * (b / (b + x * a)) ** (0.5 * b ) / (x * sps.beta(a / 2.0, b /2.0))

def main():
    rcParams['figure.figsize'] = 8, 6
    # figure(num=None,  facecolor='w', edgecolor='k')
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(0, 5, 0.01)
    mus = [1, 2, 10, 100]
    bet = [1, 1, 1, 100]
    c = ['b','r','y','g']

    for para, parb, color in zip(mus, bet, c): 
        beta = make_beta(para, parb)(x)
        ax.plot(x, beta, color, linewidth=3)

    ax.grid(True)
    plt.xlim(0, 5)
    plt.ylim(0, 2.5)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()