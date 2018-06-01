import pyodbc

cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                      "Server=CZLTOS1A35.ad001.siemens.net;"
                      "Database=slovakia_test;"
                      "UID=sk_adm;"
                      "PWD=Pass6789;")

cursor = cnxn.cursor()
# for row in cursor.tables():
#    print(row.table_name)
cursor.execute("select ID, Last_Name, First_Name from tbl_zamestnanci")
rows = cursor.fetchall()
for row in rows:
    print(row.ID, row.Last_Name, row.First_Name)
# cursor.execute("INSERT INTO tbl_zamestnanci(Last_Name, First_Name) VALUES (?, ?)", ("Banan", "Bananovic"))
# cursor.execute("DELETE FROM tbl_zamestnanci WHERE ID=13")
cursor.commit()
