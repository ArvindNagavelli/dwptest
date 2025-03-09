Feature: Data Validation of Source and Destination
#
#  Scenario: Verify correct number of rows are loaded into the database table
#    Given the database table "table_name" exists
#    When the data load process runs successfully
#    Then the table "target_table" should contain 3 rows
#


    Scenario: Verify data correctness after successful dataload into Db
    Given I have a database connection
    When I fetch data from the database
    Then the data in CSV should match the database records

