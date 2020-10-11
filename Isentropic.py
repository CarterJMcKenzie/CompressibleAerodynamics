# table A.1
def stagnation_temperature_ratio(M, k):
    ratio = 1 + (k - 1) / 2 * M ** 2
    return ratio


def stagnation_pressure_ratio(M, k):
    ratio = (1 + (k - 1) / 2 * M ** 2) ** (k / (k - 1))
    return ratio


def stagnation_density_ratio(M, k):
    ratio = (1 + (k - 1) / 2 * M ** 2) ** (1 / (k - 1))
    return ratio


# fix
def stagnation_area_ratio(M, k):
    ratio = (stagnation_temperature_ratio(M, k)) ** 0.5
    return ratio


if __name__ == '__main__':
    M = 2
    k = 1.4
    p0_p = stagnation_pressure_ratio(M, k)
    rho0_rho = stagnation_density_ratio(M, k)
    T0_T = stagnation_temperature_ratio(M, k)
    A0_Astar = stagnation_area_ratio(M, k)
    print(M, p0_p, rho0_rho, T0_T, A0_Astar)