import pyodbc


def connect_database():

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=LAPTOP-Q3A48SQV;"
        "DATABASE=dbPetShop;"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return connection