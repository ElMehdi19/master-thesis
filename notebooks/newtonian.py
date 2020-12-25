#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from scipy.special import i0, k0
from math import sqrt, cos, pi


# In[2]:


# constants
a1 = 0.5       # internal cylinder radius
a2 = 1         # external cylinder non-wavy radius
M = 100        # Hartmann dimensionless number
beta = 0.5     # Casson number
m = 1.5        # Hall number
b = 0.3        # wave amplitude
c = 1          # Wave velocity
eps = b / a2
k2 = M / (1 + pow(m, 2))      # constant in Bessel's equation
k = sqrt(k2)

# radius equations
r1 = a1 / a2   # internal cylinder constant radius
r2 = lambda z: 1 + eps * cos(2 * pi * z)
r2 = np.vectorize(r2)


# In[3]:


def c2(z, dp):
    term_1 = k0(k * r1) - i0(k * r1) * (k0(k * r1) - k0(k * r2(z))) / (i0(k * r1) - i0(k * r2(z)))
    term_1 = pow(term_1, -1)
    term_2 = (dp * (1 + pow(m, 2)) / M) - (i0(k * r1) / (i0(k * r1) - i0(k * r2(z)))) + 1
    return term_1 * term_2
c2 = np.vectorize(c2)

def c1(z, dp):
    term_1 = c - (k0(k * r1) - k0(k * r2(z))) * c2(z, dp)
    term_2 = i0(k * r1) - i0(k * r2(z))
    return term_1 / term_2
c1 = np.vectorize(c1)

def w(r, z, dp):
    #return i0(k * r) + k0(k * r) - ((1 + pow(m, 2)) * dp / M) - 1
    return c1(z, dp) * i0(k * r) + c2(z, dp) * k0(k * r) - ((1 + pow(m, 2)) * dp / M) - 1
    #return c1c(dp) * i0(k * r) + c2c(dp) * k0(k * r) - ((1 + pow(m, 2)) * dp / M) - 1
W = np.vectorize(w)


# In[8]:


z = 0.25
rz = r2(z)
r = np.linspace(r1, rz, 100)
w1 = w(r, z, 0.3) 
w2 = w(r, z, 60) 
w3 = w(r, z, 120)
plt.plot(r, w1, linewidth=1, label='dp/dz = 0.3')
plt.plot(r, w2, linewidth=1, label='dp/dz = 60')
plt.plot(r, w3, linewidth=1, label='dp/dz = 120')
plt.xlim(left=0.5)
plt.legend()
plt.grid()
plt.tight_layout()


# In[5]:


import plotly.graph_objects as go

z = np.linspace(0, 10, 100)
rs = lambda z: 1 + eps * cos(2 * pi * z)
r = np.array([np.linspace(r1, rs(z), 100) for z in z])
#r = r.swapaxes(0,1)
dp = 0.3
w1 = w(r, z, dp)
#z2 = z.reshape(1, 100)
#print(w(0.75, 2, 0.3))

z = np.repeat(z.reshape(1, 100), repeats=100, axis=0)

fig = go.Figure(go.Surface(
    contours = {
        "x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color":"white"},
        "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05}
    },
    x = r,
    y = z[0],
    z = w1
    ))
fig.update_layout(
        scene = {
            "xaxis_title": "Radius r",
            "yaxis_title": "Axial Z",
            "zaxis_title": "Axial velocity w",
            "xaxis": {"nticks": 10},
            "zaxis": {"nticks": 4},
            'camera_eye': {"x": 0, "y": 2.5, "z": 0},
            "aspectratio": {"x": 1, "y": 1, "z": 0.2}
        })
fig.show()


# In[ ]:




