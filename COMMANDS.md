## Clear git cache

`git rm -r --cached .`

## HTML Report

For a self-contained pytest-html report with css and images in one file:

`python -m pytest --html=reports/report.html --self-contained-html -vs tests/00_check_setup`

`--self-contained` means just one file and if we don't specify tests it will work on all `tests` folder.

## Coverage

`python -m pytest -vs tests\02_py_coffee --cov-report html --cov .`

A report `index.html` will be in htmlcov folder.

## xdist

`python -m pytest -vs  .\tests\00_check_setup\Xtest_09_xdist.py -n 2`

Not included in usual test suite as it is designed as a demo for xdist.