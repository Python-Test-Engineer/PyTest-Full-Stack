## Clear git cache

`git rm -r --cached .`

## HTML Report

For a self-contained pytest-html report with css and images in one file:

`python -m pytest --html=reports/report.html --self-contained-html`

## Coverage

`python -m pytest --cov-report html --cov .`