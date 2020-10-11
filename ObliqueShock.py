import numpy as np


def theta_beta_mach_relation_for_theta(beta, M, k):
    theta = np.arctan(2*1/np.tan(beta) * ((M**2 * np.sin(beta)**2 -1)/(M**2*(k+np.cos(2*beta))+2)))
    return theta


def theta_beta_mach_relation_for_mach(theta, beta, k):
    numerator = np.tan(theta) - 2*1/np.tan(beta)
    denominator =  2*1/np.tan(beta)*np.sin(beta)**2 - np.tan(theta)*(k+np.cos(2*beta))
    mach = (numerator/denominator)**0.5
    return mach


def flat_plate_coefficient_of_lift(M, alpha, k, p_ratio1, p_ratio2):
    return 2/(k*M**2)*(p_ratio2-p_ratio1)*np.cos(alpha)


def flat_plate_coefficient_of_drag(M, alpha, k, p_ratio1, p_ratio2):
    return 2/(k*M**2)*(p_ratio2-p_ratio1)*np.cos(alpha)

