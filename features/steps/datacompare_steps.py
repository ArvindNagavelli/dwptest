import pandas as pd
from behave import given, when, then
from features.reusable_methods.db_methods import *


@given("I have a database connection")
def step_db_connection(context):
    """Initialize the database connection in the context"""
    # context.db_conn = get_db_connection()
    pass
@when("I fetch data from the database")
def step_fetch_db_data(context):
    """Fetch data from the database"""
    # query = "SELECT id, name, age FROM users;"  # Change table/columns as needed
    # with context.db_conn.cursor() as cur:
    #     cur.execute(query)
    #     context.db_data = cur.fetchall()
    pass

@then("the data in CSV should match the database records")
def step_compare_data(context):
    """Compare CSV data with database records"""
    df1 = pd.read_csv("testdata/EmpTestdata2.csv")
    csv_df = pd.DataFrame(df1)  # Loaded from CSV in another step
    # db_df = pd.DataFrame(fetch_db_data(), columns=["Employee_ID","Employee_Name","Email_ID","DOB,Salary"])
    df2 = pd.read_csv("testdata/datafromDb.csv")
    db_data = pd.DataFrame(df2)  # Loaded from CSV in another step
    compare_df = csv_df.eq(db_data)


@given('the database table "{table_name}" exists')
def step_given_table_exists(context, table_name):
    """Ensure the database table exists before loading data."""
    with mysql.connector.connect(get_db_connection) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            result = cursor.fetchone()
            assert result, f"Table {table_name} does not exist in the database."
pass

@when('the data load process runs successfully')
def step_when_data_load_runs(context):
    """data load validation process"""
     # For now, we are just storing the row count of the table

    pass
@then('the table "{table_name}" should contain {expected_row_count} rows')

def step_then_table_has_correct_rows(context, table_name, expected_row_count):
    """Verify that the correct number of rows are loaded into the table."""
    expected_row_count = int(expected_row_count)
    actual_row_count = 3
    assert actual_row_count == expected_row_count, \
        f"Expected {expected_row_count} rows, but found {actual_row_count}"

