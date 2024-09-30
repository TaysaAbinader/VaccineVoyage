from databaseconnection import connection

def retrieve_hints(selected_country, current_level):
    #SQL query to retrieve 6 hints correlating to the selected country, randomly ordered
    sql_hint= (f"select hints.description from hints inner join countries on countries.country_id = hints.country_id where countries.name = '{selected_country}' and  hints.level = '{current_level}' order by rand();")
    print(sql_hint)
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

print(retrieve_hints(Canada,1))




