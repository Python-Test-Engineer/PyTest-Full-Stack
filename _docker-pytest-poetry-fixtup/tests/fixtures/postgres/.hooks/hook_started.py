from time import monotonic
import psycopg2

start = monotonic()
connected = False
timeout = 5
while not connected:
    try:
        conn = psycopg2.connect(
            "host=127.0.0.1 dbname=postgres user=postgres password=1234"
        )
        connected = True
        conn.close()
    except Exception:
        if monotonic() - start > timeout:
            raise TimeoutError()
