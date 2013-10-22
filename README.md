Multivariate Polynomial Fit
===========================

Holds a python function to perform multivariate polynomial regression in Python
using NumPy

[See related question on
stackoverflow](http://stackoverflow.com/questions/10988082/multivariate-polynomial-regression-with-numpy)

This is similar to numpy's polyfit function but works on multiple covariates

Origin
------

This code originated from the following question on StackOverflow

[http://stackoverflow.com/questions/10988082/multivariate-polynomial-regression-with-numpy](http://stackoverflow.com/questions/10988082/multivariate-polynomial-regression-with-numpy)

Author
------

[Matthew Rocklin](http://matthewrocklin.com)

License
-------

New BSD license. See LICENSE.txt

Disclaimer
----------

This is not a commonly used method.  It often results in a solution with many
non-zero coeffieicients like

    10 x**2 + 0.01 x y - 0.02 x + 20 y - 0.03 y**2

Instead of a sparse solution like

    10 x**2 + 20 y

To obtain sparse solutions (like the second) where near-zero elements are
eliminated you should probably look into L1 regularization
