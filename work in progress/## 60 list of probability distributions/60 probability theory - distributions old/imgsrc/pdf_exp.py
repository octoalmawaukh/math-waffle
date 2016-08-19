import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_beta(lam):
    return lambda x: lam * np.e ** (- lam * x)

def main():
    rcParams['figure.figsize'] = 8, 6
    # figure(num=None,  facecolor='w', edgecolor='k')
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(0, 5, 0.01)
    lamy = [2, 1, 0.5, 0.25]
    c = ['b','r','y','g']

    for para, color in zip(lamy, c): 
        beta = make_beta(para)(x)
        ax.plot(x, beta, color, linewidth=3)

    ax.grid(True)
    plt.xlim(0, 5)
    plt.ylim(0, 1.6)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()