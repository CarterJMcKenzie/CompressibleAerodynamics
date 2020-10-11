import math as ma
import Isentropic
from scipy import optimize


def mach_relation(M, k):
    M2 = ((1 + abs((k - 1) / 2) * M ** 2) / (k * M ** 2 - (k - 1) / 2)) ** 0.5
    return M2


def density_ratio(M, k, opt=0):
    ratio = (k + 1) * M ** 2 / (2 + (k - 1) * M ** 2)
    if opt:
        ratio = ratio - opt
    return ratio


def pressure_ratio(M, k, opt=0):
    ratio = 1 + 2 * k / (k + 1) * (M ** 2 - 1)
    if opt:
        ratio = ratio - opt
    return ratio


def temperature_ratio(M, k, opt=0):
    ratio = (1 + 2 * k / (k + 1) * (M ** 2 - 1)) * (2 + (k - 1) * M ** 2) / ((k + 1) * M ** 2)
    if opt:
        ratio = ratio - opt
    return ratio


def stagnation_pressure_ratio(M, k, R, opt=0):
    cp = k * R / (k - 1)
    ds = cp*ma.log((1 + 2 * k / (k + 1) * (M ** 2 - 1)) * ((2 + (k - 1) * M ** 2) / ((k + 1) * M ** 2))) - R * \
         ma.log((1 + 2 * k / (k + 1) * (M ** 2 - 1)))
    ratio = ma.exp(-ds / R)
    if opt:
        ratio = ratio - opt
    return ratio


def stagnation_pressure_ratio2(M, k, R, opt=0):
    p02_p01 = stagnation_pressure_ratio(M, k, R)
    p01_p1 = Isentropic.stagnation_pressure_ratio(M,k)
    p02_p1 = p02_p01 * p01_p1
    if opt:
        p02_p1 = p02_p1 - opt
    return p02_p1


def optimizer(k, R, p2_p1=0, rho2_rho1=0, T2_T1=0, p02_p01=0, p02_p1=0):
    if p2_p1:
        m = optimize.bisect(pressure_ratio, 1, 50, (k, p2_p1))
    if rho2_rho1:
        m = optimize.bisect(density_ratio, 1, 50, (k, rho2_rho1))
    if T2_T1:
        m = optimize.bisect(temperature_ratio, 1, 50, (k, T2_T1))
    if p02_p01:
        m = optimize.bisect(stagnation_pressure_ratio, 1, 50, (k, R, p02_p01))
    if p02_p1:
        m = optimize.bisect(stagnation_pressure_ratio2, 1, 50, (k, R, p02_p01))
    return m

if __name__ == '__main__':
    # tabulate values
    M1 = 2
    k = 1.4
    R = 287
    p2_p1 = pressure_ratio(M1, k)
    rho2_rho1 = density_ratio(M1, k)
    T2_T1 = temperature_ratio(M1, k)
    p02_p01 = stagnation_pressure_ratio(M1, k, R)
    p02_p1 = stagnation_pressure_ratio2(M1, k, R)
    M2 = mach_relation(M1, k)
    print(M1, p2_p1, rho2_rho1, T2_T1, p02_p01, p02_p1, M2)
    m = optimizer(k, R, p2_p1=p2_p1)
    print(m)
