from django.db import connection

def get_nextautoincrement( mymodel ):
    cursor = connection.cursor() #@UndefinedVariable
    cursor.execute( "SELECT Auto_increment FROM temporary.tables WHERE table_name='%s';" % \
                    mymodel._meta.db_table)
    row = cursor.fetchone()
    cursor.close()
    return row[0]
