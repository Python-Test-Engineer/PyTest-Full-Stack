## Clear git cache

`git rm -r --cached .`

## HTML Report

For a self-contained pytest-html report with css and images in one file:

`python -m pytest --html=reports/report.html --self-contained-html -vs`

## Coverage

For brevity, we will select a subset of tests:

`python -m pytest -vs tests\02_py_coffee --cov-report html --cov .`

A report `index.html` will be in htmlcov folder.