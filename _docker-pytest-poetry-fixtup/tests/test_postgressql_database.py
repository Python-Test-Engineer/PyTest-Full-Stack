import fixtup
import psycopg2

# https://dev.to/farcellier/test-beyond-your-code-with-docker-pytest-3b7g


def test_postgres_should_work():
    with fixtup.up("postgres"):
        conn = psycopg2.connect(
            "host=127.0.0.1 dbname=postgres user=postgres password=1234"
        )
        cur = conn.cursor()
        cur.execute("SELECT 1+1")
        res = cur.fetchall()
        assert res[0][0] == 2
        conn.close()
