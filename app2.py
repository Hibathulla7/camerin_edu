import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'python_app',
    password = 'Python@123',
    database = 'camerin_students',
    port = 3306

)
print("MySql in connection is successfull")

def get_data():
    query = """ SELECT * FROM COURSES 
        WHERE course_id = 201"""
    cursor.execute(query)
    return cursor.fetchone()
try:
    with connection.cursor as cursor:
        print(" == Orginal Data ==")
        print(get_data())

        cursor.execute("""
                update courses set course_name = %s
                where course_id = %s
                """,("DSML",203))
        print(get_data())
        
        connection.commit()
        
        print("== After Commit ==")
        print(get_data())

        cursor.execute("""
                        update students set city = %s
                        where student_id = %s
                        """,("Thrissur",102))
        print("== After Commit 2 (Before ROLLBACK) ==")
        print(get_data())
        
except Exception as e:
    print(f'Error : {e}')

finally:
    print("Operation completed")    