"""
Módulo con la solución completa del péndulo simple.
"""

import numpy as np
import scipy as sci


def period(
    L=1,
    g=sci.constants.value("standard acceleration of gravity"),
    phi_max=sci.constants.pi / 4,
):
    """
    Calcula el periodo real de un péndulo simple.

    Parámetros
    ----------
    L : longitud [m] del brazo
    g : aceleración gravitatoria [m/s^2]
    phi_max:  ángulo máximo/inicial [rad]

    Regresa
    -------
    T : periodo real [s]

    Fuente: Wikipedia (verificado por mí)
    """

    T = 4.0 * np.sqrt(L / g) * sci.special.ellipk(np.sin(phi_max / 2.0) ** 2)

    return T


def movement(
    t,
    L=1,
    g=sci.constants.value("standard acceleration of gravity"),
    phi_max=sci.constants.pi / 4,
):
    """
    Calcula la posición vs. tiempo de un péndulo simple.

    Parámetros
    ----------
    t : tiempo [s]
    L : longitud [m] del brazo
    g : aceleración gravitatoria [m/s^2]
    phi_max:  ángulo máximo/inicial [rad]

    Regresa
    -------
    phi : ángulo real [rad]

    Fuente: Wikipedia (verificado por mí)
    """

    k = np.sin(phi_max / 2.0)
    m = k**2

    sn, cn, dn, ph = sci.special.ellipj(np.sqrt(g / L) * t, m)

    phi = 2.0 * np.arcsin(k * cn / dn)

    return phi
