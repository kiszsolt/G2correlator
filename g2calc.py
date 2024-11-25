import numpy as np
import matplotlib.pyplot as plt

def coincidence(c1, c2, window, bindwidth):
    hw = window+bindwidth/2
    hist = []
    for t1 in c1:
        r1 = c2[np.where(t1-hw<=c2)]
        range = r1[np.where(r1<=t1+hw)]-t1
        if np.size(range):
            hist = np.append(hist, range)

    return hist

def coincidence2(c1, c2, window, binwidth):
    hw = window+binwidth/2

    for t1 in c1:
        r1 = c2[np.where(t1<=c2)]
        range = r1[np.where(r1<=t1+hw)]-t1
        if np.size(range):
            hist = np.append(hist, range)

    return hist

n=int(200000)
mu = 3000
nu = 30000
dtau = np.random.default_rng().exponential(scale=mu, size=n-1)
# dT = np.random.default_rng().exponential(scale=nu, size=n-1)
dT = np.random.default_rng().integers(nu, size=n-1)
dt = dtau+dT

s0 = np.zeros(n, dtype='int')
i = 0
for t in dt:
    s0[i+1] = int(s0[i]+t)
    i = i+1

s0 = s0+100

r = np.random.default_rng().integers(2, size=n)

c1 = (r*s0).astype('int32')
c2 = ((1-r)*s0).astype('int32')

c1 = c1[c1>0]
c2 = c2[c2>0]

num_bins = 200

fig, ax = plt.subplots()

hist = coincidence(c1, c2, 30000, 400)
# hist2 = coincidence2(c1, c2, 30000, 400)
# the histogram of the data
h1 = hist[hist<2*nu]
h2 = h1[-2*nu<h1]
n, bins, patches = ax.hist(h2, num_bins, density=True)




fig.tight_layout()
plt.show(block=True)