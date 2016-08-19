import numpy as np
import matplotlib.pyplot as plt 
from pylab import rcParams

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2))

def main():
    rcParams['figure.figsize'] = 8, 6
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-4, 4, 0.01)
    s = np.sqrt([0.2, 1, 5, 0.5])
    m = [0, 0, 0, -2] 
    c = ['b','r','y','g']

    for sig, mu, color in zip(s, m, c): 
        gauss = make_gauss(1, sig, mu)(x)
        ax.plot(x, gauss, color, linewidth=3)

    ax.grid(True)
    plt.xlim(-4, 4)
    plt.ylim(0, 1)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best',prop={'size':20})
    plt.savefig('foo.pdf', bbox_inches='tight')

if __name__ == '__main__':
   main()