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
    query = """
                    SELECT  * FROM STUDENTS
                    WHERE student_id = 102
                    """
    cursor.execute(query)
    return cursor.fetchone()

try:
    with connection.cursor() as cursor:
        query = """
                SELECT  * FROM STUDENTS
                WHERE student_id = 102
                """
        cursor.execute(query)
        print(" == Orginal Data ==")
        print(get_data())
        # print(cursor.fetchone())

        cursor.execute("""
        update students set city = %s
        where student_id = %s
        """,("Delhi",102))

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

        connection.rollback()
        print("==After Rollback==")
        print(get_data())
        

except Exception as e:
    print(f"Error : {e}")

finally:
    connection.close()
    print("Operation completed")