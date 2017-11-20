import numpy as np
from numpy import zeros, eye


class ExtendedKalmanFilter(object):

    def __init__(self, x, F, B, P, Q, R, Hx, HJacobian):

        self._x = x
        self._F = F
        self._B = B
        self._P = P
        self._Q = Q
        self._R = R
        self._Hx = Hx
        self._HJacobian = HJacobian


    def update(self, z):

        P = self._P
        R = self._R
        x = self._x

        H = self._HJacobian(x)

        S = H * P * H.T + R
        K = P * H.T * S.I
        self._K = K

        hx =  self._Hx(x)
        y = np.subtract(z, hx)
        self._x = x + K * y

        KH = K * H
        I_KH = np.identity((KH).shape[1]) - KH
        self._P = I_KH * P * I_KH.T + K * R * K.T

    def predict(self, u=0):
        self._x = self._F * self._x + self._B * u
        self._P = self._F * self._P * self._F.T + self._Q

    @property
    def x(self):
        return self._x
