import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_beta(alp, bet):
    return lambda x: bet ** alp * x ** (alp - 1) * np.e ** (- bet * x) / sps.gamma(alp)

def main():
    rcParams['figure.figsize'] = 8, 6
    ax = plt.figure().add_subplot(1,1,1)
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    # figure(num=None,  facecolor='w', edgecolor='k')
    x = np.arange(0, 20, 0.01)
    pie = [2, 3, 9, 7.5]
    dru = [0.5, 0.5, 2, 1]
    c = ['w','w','w','w']

    for para, parb, color in zip(pie, dru, c): 
        beta = make_beta(para, parb)(x)
        ax.plot(x, beta, color, linewidth=3)

    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()