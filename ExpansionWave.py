import numpy as np
from scipy import optimize


def prandtl_meyer_function(M, k):
    return ((k+1)/(k-1))**0.5 * np.arctan( ((k-1)/(k+1)*(M**2-1))**0.5 ) - np.arctan( (M**2-1)**0.5 )


def prandtl_meyer_opt_fx(M, k, v2):
    v = v2 - np.rad2deg(prandtl_meyer_function(M, k))
    return v


def prandtl_meyer_equation(theta2, M , k=1.4, t1=0):
    """input degrees, output degrees, t2 = theta 2, M = mach number, k = specific heat"""
    v1 = prandtl_meyer_function(M, k)
    v1 = np.rad2deg(v1)
    v2 = v1 + theta2
    M2 = optimize.bisect(prandtl_meyer_opt_fx, 1.01, 10, (k, v2))
    return v2, M2


if __name__ == "__main__":
    # find M2 and v2 if air
    alpha = 5  # deg
    M1 = 2.2
    v2, M2 = prandtl_meyer_equation(alpha, M1, k=1.4)
    print(v2, M2)
