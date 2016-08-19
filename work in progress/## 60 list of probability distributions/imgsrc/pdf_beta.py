import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_beta(N, alf, bet):
    return lambda x: x ** (alf - 1) * (1-x) ** (bet-1) / sps.beta(alf, bet)

def main():
    rcParams['figure.figsize'] = 8, 6
    # figure(num=None,  facecolor='w', edgecolor='k')
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(0, 1, 0.01)
    s = [0.5, 2, 1, 2] 
    m = [0.5, 5, 3, 2] 
    c = ['b','r','y','g']

    for alf, bet, color in zip(s, m, c): 
        beta = make_beta(1, alf, bet)(x)
        ax.plot(x, beta, color, linewidth=3)

    ax.grid(True)
    plt.xlim(0, 1)
    plt.ylim(0, 2.5)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()