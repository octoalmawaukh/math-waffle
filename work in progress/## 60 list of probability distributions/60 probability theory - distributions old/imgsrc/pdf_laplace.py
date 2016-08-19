import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_beta(mu, be):
    return lambda x: np.e ** (-abs(x-mu) / (1.0 * be)) / (2*be)

def main():
    rcParams['figure.figsize'] = 8, 6
    # figure(num=None,  facecolor='w', edgecolor='k')
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-10, 10, 0.01)
    mus = [0, 0, 0, -5]
    bet = [1, 2, 4, 4]
    c = ['b','r','y','g']

    for para, parb, color in zip(mus, bet, c): 
        beta = make_beta(para, parb)(x)
        ax.plot(x, beta, color, linewidth=3)

    ax.grid(True)
    plt.xlim(-10, 10)
    plt.ylim(0, 0.5)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()