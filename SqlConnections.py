#INSERT INTO Table (1,2) values (1,2)

def insert_data_disease_table(names, country, cursor):
    sql1 = f"insert into vaccine_voyage (disease_name, visited_country) values ('{names}', '{country}')"
    return cursor.execute(sql1)

