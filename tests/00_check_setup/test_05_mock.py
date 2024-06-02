"""MOCK"""
#  https://www.youtube.com/watch?v=ZLeNbmpx7cc
import unittest
from unittest.mock import Mock
from requests.exceptions import Timeout
import pytest

cx_Oracle = Mock()


@pytest.mark.mocks
def query_database(sql: str):
    """doc string"""
    db_user = "blah"
    db_pass = "blah"
    db_dsn = "(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = tcp)(host = host1) (Port = 1525))) (CONNECT_DATA = (SID = orcl)))"

    try:
        res = (
            cx_Oracle.connect(db_user, db_pass, dsn=db_dsn)
            .cursor()
            .execute(sql)
            .fetchall()
        )
        print("Query executed successfully.")
    except:
        print("Insert the error into a log table.")

    return res[0][0]


@pytest.mark.mocks
class TestDatabase(unittest.TestCase):
    """doc string"""

    def test_0021_query_database(self):
        """doc string"""
        sql = "select max(id) from orders"
        cx_Oracle.connect().cursor().execute(sql).fetchall.return_value = [(100,)]
        self.assertEqual(query_database(sql), 100)

    def test_0021_query_database(self):
        """doc string"""
        sql = "select max(id) from orders"
        cx_Oracle.connect().cursor().execute(sql).fetchall.side_effect = [
            [(100,)],
            Timeout,
        ]
        self.assertEqual(query_database(sql), 100)
        with self.assertRaises(Exception):
            query_database(sql)


if __name__ == "__main__":
    unittest.main()
