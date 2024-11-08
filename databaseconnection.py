import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='vaccine_voyage',
         user='root',
         password='Shahid75',
         autocommit=True,
         collation='utf8mb3_general_ci'
         )

