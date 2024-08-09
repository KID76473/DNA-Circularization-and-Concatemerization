import numpy as np
import numba
import haversine
import math


@ numba.jit(forceobj=True)
def test():
    print(haversine.haversine([0, 0], [0, np.pi]))
    lat, lat1, lat2, lng = 0, 0, 0, 0

    d = (math.sin(lat * 0.5) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lng * 0.5) ** 2)
    print(2 * math.asin(math.sqrt(d)))


test()
