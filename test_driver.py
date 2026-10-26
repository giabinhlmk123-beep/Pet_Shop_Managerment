import pyodbc

drivers = pyodbc.drivers()

print("SQL Server Drivers:")

for driver in drivers:
    print(driver)