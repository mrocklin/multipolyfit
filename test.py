from multipolyfit import multipolyfit
import numpy as np

def test_multipolyfit():
    xs = np.array([[1,2,3,4,5],[1,1,1,1,1]]).T
    y = np.array([2,3,4,5,6])
    model = multipolyfit(xs, y, 2, model_out = True)
    yhat = np.asarray(map(model, xs[:,0], xs[:,1]))

    assert np.linalg.norm(y - np.asarray(yhat)) < .0001
