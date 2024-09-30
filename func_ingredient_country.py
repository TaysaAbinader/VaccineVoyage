import mysql.connector
connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='vaccine_voyage',
        user='root',
        password='06042004',
        aoutocommit=True)

def ingredient_country():
    sql = f"Select name from countries order by rand() limit 7"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    list_country =[]

    if cursor.rowcount >0 :
        for row in result:
            list_country.append(row[0])
            country1, country2,country3, country4, country5, country6, country7 = list_country

    return

