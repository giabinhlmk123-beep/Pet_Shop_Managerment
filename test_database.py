from database.database import connect_database


try:
    connection = connect_database()
    print("Kết nối database thành công!")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sys.databases")
    rows = cursor.fetchall()
    print("Danh sách database:")
    for row in rows:
        print(row[0])

    cursor.close()
    connection.close()

except Exception as e:
    print("Kết nối database thất bại!")
    print("Lỗi:", e)