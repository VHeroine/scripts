class PreconditionError(Exception):
    def __init__(self, val):
        self.val = val


class ComplexRootError(Exception):
    def __init__(self, val):
        self.val = val


def solve(a, b, c):
    """Function for solving the quadratic equation."""
    for i, key in enumerate([a, b, c]):
        if not isinstance(key, (int, float)):
            raise TypeError(f'Exception - {i+1} element has class {type(key)}. Needs to be either float or number class.')
    import math
    a, b, c = map(float, (a, b, c))
    if a == 0:
        raise PreconditionError(f'Exception - precondition violation. You have entered coefficient a equal to {a}')
    discr = b**2 - 4*a*c
    if discr < 0:
        raise ComplexRootError(f'Exception - complex roots for the specified coefficients a = {a}, b = {b}, c = {c}')
    elif discr == 0:
        res = (-b / (2*a),)
    else:
        res = (((-b + math.sqrt(discr)) / (2 * a)), ((-b - math.sqrt(discr)) / (2 * a)))
        res = tuple(sorted(set(res)))
    return res