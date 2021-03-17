import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-2, 2.5, 0.5)

with plt.style.context('fivethirtyeight'):
    plt.plot(x, np.abs(x), linewidth=2)
    plt.title('$y=|x|$', y=-0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.tight_layout()
    plt.savefig('absx.png', transparent=True)
    plt.show()

