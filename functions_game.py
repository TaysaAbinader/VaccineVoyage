from databaseconnection import connection

def retrieve_hints(selected_country, current_level):
    #SQL query to retrieve 6 hints correlating to the selected country, randomly ordered
    sql_hint= (f"select hints.description from hints inner join countries on countries.country_id = hints.country_id where countries.name = '{selected_country}' and  hints.level = '{current_level}' order by rand();")
    #create a cursor_hint to collect countries
    cursor_hint= connection.cursor()
    cursor_hint.execute(sql_hint)
    result_hint = cursor_hint.fetchall()
    #Assign the 6 random hints into 6 variables
    hint_list = []
    if cursor_hint.rowcount > 0:
        for hint_row in result_hint:
            hint_list.append(hint_row[0])
    return hint_list



def insert_data_disease_table(names, country, cursor):
    sql1 = f"insert into vaccine_voyage.disease (disease_name, visited_country) values ('{names}', '{country}')"
    return cursor.execute(sql1)

def multiple_choice ():
    multiple_choice_countries = ["Paraguay", "Ghana", "Ukraine", "Russia", "Cuba", "Guyana", "Lebanon", ]



def ingredient_country():
    sql = f"Select name from countries order by rand() limit 7"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    list_country =[]
    if cursor.rowcount >0 :
        for row in result:
            list_country.append(row[0])
    return list_country

def point_per_level(current_level):
    sql_point = f"select hints.points from hints where hints.level = '{current_level}' limit 1;"
    # create a cursor_hint to calculate point countries
    cursor_point = connection.cursor()
    cursor_point.execute(sql_point)
    result_point = cursor_point.fetchall()
    point_level = 0
    if cursor_point.rowcount >0 :
        for point_row in result_point:
            point_level = point_row[0]
    return point_level


