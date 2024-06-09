This is based on the following article: 

 - https://dev.to/farcellier/test-beyond-your-code-with-docker-pytest-3b7g

Copy and run from outside PyTest-Full-Stack

- `python -m venv venv`
- `.\venv\Scripts\activate` or Mac equivalent
- `pip install -r requirements.txt`
- remove `REACTIVATE_` from front of `test_postgressql_database.py`. This was done to prevent the tests running in PFS. Once can use --ignore in command line or pytest.ini.
- `python -m pytest .\tests\test_postgressql_database.py -vs`

*Make sure docker is running!*