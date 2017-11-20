class Polynomial:
    def __init__(self, coeffs):
        self._coeffs = coeffs
        self._deg = len(coeffs) - 1

    def __call__(self, x):
        value = 0
        for i, coeff in enumerate(self._coeffs):
            value += coeff * x ** i
        return value

    @property
    def deriv(self):
        d_coeffs = [0]*self._deg
        for i in range(self._deg):
            d_coeffs[i] = (i+1)*self._coeffs[i+1]
        return Polynomial(d_coeffs)


if __name__ == '__main__':
    my_poly = Polynomial([0])
    my_poly_deriv = my_poly.deriv
    print(my_poly._coeffs)
    print(my_poly_deriv._coeffs)
    print("result : ", my_poly(1))
    print("result : ", my_poly_deriv(1))
    my_poly = Polynomial([1,2,3,4])
    my_poly_deriv = my_poly.deriv
    print(my_poly._coeffs)
    print(my_poly_deriv._coeffs)
    print("result : ", my_poly(1))
    print("result : ", my_poly_deriv(1))
