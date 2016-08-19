import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_beta(alp, bet):
    return lambda x: bet ** alp * x ** (alp - 1) * np.e ** (- bet * x) / sps.gamma(alp)

def main():
    rcParams['figure.figsize'] = 8, 6
    # figure(num=None,  facecolor='w', edgecolor='k')
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(0, 20, 0.01)
    pie = [2, 3, 9, 7.5]
    dru = [0.5, 0.5, 2, 1]
    c = ['b','r','y','g']

    for para, parb, color in zip(pie, dru, c): 
        beta = make_beta(para, parb)(x)
        ax.plot(x, beta, color, linewidth=3)

    ax.grid(True)
    plt.xlim(0, 20)
    plt.ylim(0, 0.4)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()