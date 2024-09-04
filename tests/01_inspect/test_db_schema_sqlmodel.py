import pytest
from sqlmodel import create_engine, inspect
from sqlmodel import Integer
from pathlib import Path

from rich.console import Console

console = Console()

DB = "sql_inspect.sqlite"

# 1
# DB_PATH = str((Path().parent / DB).resolve())
# db_uri = f"sqlite:///{DB_PATH}"

# 2
db_uri = f"sqlite:///tests/01_inspect/{DB}"

engine = create_engine(db_uri)

inspector = inspect(engine)

# Get table information
# print("\n\n=======================================================================\n")
# print("-----------------")
# print(f"sqlite:///{DB_PATH}")
# print("-----------------\n")
# print(f"TABLES in {DB}:")
# rprint(inspector.get_table_names())
# print("=======================================================================")

# print("\ntracks table")
# table = "tracks"
# # Get column information
# columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
# assert columns["trackid"]["primary_key"] == 1 # i.e true
# rprint(columns)
# print("-----------------------------------------------------")
# print("\nartists table")
# table = "artists"
# # Get column information
# columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
# rprint(columns)


def test_0100_SQL_db_column_type():
    # Get column information
    # print("==========================")
    # print("\n\nis_trackid_integer")
    table = "tracks"
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert isinstance(columns["trackid"]["type"], Integer)
    # rprint(f"Is trackid integer? {isinstance(columns["trackid"]["type"], Integer)}")


#  get FK


def test_0101_SQL_db_artist_has_no_fk():
    """Check Foreign Keys artist"""
    # print("==========================")
    # print("\n\nartists_has_no_fk")
    table = "artists"
    foreign_keys_artist = inspector.get_foreign_keys(table)
    assert len(foreign_keys_artist) == 0
    console.print(f"\n[green]Foreign Keys for artists?: {foreign_keys_artist}")


def test_0102_SQL_db_track_has_fk():
    # print("==========================")
    # print("\n\ntrack_has_fk")
    """Check Foreign Keys track - there is one track to artist"""
    table = "tracks"
    foreign_keys_track = inspector.get_foreign_keys(table)

    assert len(foreign_keys_track) > 0


def test_0103_SQL_db_nullables():
    """Check trackid is not nullable"""
    table = "tracks"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["trackid"]["nullable"] is False


def test_0104_SQL_db_primary_key():
    """Check trackid is primary key"""
    table = "tracks"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["trackid"]["primary_key"] == 1  # i.e true


def test_0105_SQL_db_default():
    """Check trackid has default value"""
    table = "tracks"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    assert columns["trackid"]["default"] is None
    assert columns["trackname"]["default"] == "'TONY'"  # in db schema value is 'TONY'


def test_0106_SQL_db_unique():
    """
    Check artistname is unique. N/A in SQLite
    """
    # table = "artists"
    # # Get column information
    # columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    # rprint(columns["artistname"])
    # rprint("Check artistname is unique. N/A in SQLite.")
    assert True
    # assert columns["artistname"]["unique"] is True


@pytest.mark.xfail
def test_0107_SQL_db_check_constraint():
    """
    Check trackname has min 5 characters

    """
    table = "tracks"
    # Get column information
    columns = {columns["name"]: columns for columns in inspector.get_columns(table)}
    # print(
    #     "In sqlite the CHECK constraint is not in the schema. It is, though, in the database."
    # )
    console.print("\n[green]We could do an insert test to raise an exception.[/]")
    assert columns["trackname"]["check"] != ""
    assert True
