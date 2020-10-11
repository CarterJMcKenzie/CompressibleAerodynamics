from scipy import optimize

# table A.3
def total_temp(cp, T01, T02):
    q = cp*(T02-T01)
    return q


def static_pressure_ratio(M, k, opt=0):
    ratio = (1 + k) / (1 + k * M ** 2)
    if opt:
        ratio = ratio-opt
    return ratio


def static_temperature_ratio(M, k, opt=0):
    ratio = ((1 + k) / (1 + k * M ** 2)) ** 2 * M ** 2
    if opt:
        ratio = ratio-opt
    return ratio


def static_density_ratio(M, k, opt=0):
    ratio = ((1 + k * M ** 2) / (1 + k)) * (1 / M) ** 2
    if opt:
        ratio = ratio-opt
    return ratio


def static_stagnation_pressures_ratio(M, k, opt=0):
    ratio = (1 + k) / (1 + k * M ** 2) * ((2 + (k - 1) * M ** 2)/(k + 1)) ** (k / (k - 1))
    if opt:
        ratio = ratio-opt
    return ratio


def static_stagnation_temperature_ratio(M, k, opt=0):
    ratio = ((1 + k) * M ** 2 / (1 + k * M ** 2) ** 2) * (2 + (k - 1) * M ** 2)
    if opt:
        ratio = ratio-opt
    return ratio


def mach_number(k, supersonic, p_star_r=0, T_star_r=0, rho_star_r=0, p0_star_r=0, T0_star_r=0):

    # create optimizer initial guesses
    if supersonic:
        g1 = 1
        g2 = 10
    if not supersonic:
        g1 = 0.001
        g2 = 1

    # run optimizer specific to input ratio
    if p_star_r:
        m = optimize.bisect(static_pressure_ratio, g1, g2, (k, p_star_r))
    if T_star_r:
        m = optimize.bisect(static_temperature_ratio, g1, g2, (k, T_star_r))
    if rho_star_r:
        m = optimize.bisect(static_density_ratio, g1, g2, (k, rho_star_r))
    if p0_star_r:
        m = optimize.bisect(static_stagnation_pressures_ratio, g1, g2, (k, p0_star_r))
    if T0_star_r:
        m = optimize.bisect(static_stagnation_temperature_ratio, g1, g2, (k, T0_star_r))
    return m


if __name__ == "__main__":
    M = 0.62
    k = 1.4

    # tabulate ratios
    p_star_r = static_pressure_ratio(M, k)
    T_star_r = static_temperature_ratio(M, k)
    rho_star_r = static_density_ratio(M, k)
    p0_star_r = static_stagnation_pressures_ratio(M, k)
    T0_star_r = static_stagnation_temperature_ratio(M, k)
    print(M, p_star_r, T_star_r, rho_star_r, p0_star_r, T0_star_r)

    # determine mach from a ratio
    M2 = mach_number(k, supersonic=False, T_star_r=T_star_r)
    print(M2)