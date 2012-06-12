from multipolyfit import multipolyfit, mk_sympy_function
import numpy as np

def test_multipolyfit():
    xs = np.array([[1,2,3,4,5]]).T
    y = np.array([2,3,4,5,6])
    betas = multipolyfit(xs, y, 2)

    # 1 + x + 0x**2
    assert np.linalg.norm(betas - np.asarray((1,1,0))) < .0001




def test_model():
    xs = np.array([[1,2,3,4,5], [1,-1,1,-1,1]]).T
    y = np.array([2,2,4,4,6])
    model = multipolyfit(xs, y, 2, model_out = True)

    yhat = np.asarray(map(model, xs[:,0], xs[:,1]))

    assert np.linalg.norm(y - yhat) < .0001

def test_sympy():
    try:
        from sympy import symbols
        xs = np.array([[1,2,3,4,5], [1,-1,1,-1,1]]).T
        y = np.array([2,3,4,5,6])
        betas, powers = multipolyfit(xs, y, 2, powers_out=True)

        expr = mk_sympy_function(betas, powers)
        x0, x1 = symbols('x0,x1')
        symbol_sets = {tuple(sorted(arg.free_symbols)) for arg in expr.args}
        assert symbol_sets == {tuple(), (x0,), (x1,), (x0, x1)}
    except ImportError:
        pass

