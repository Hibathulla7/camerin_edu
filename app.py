import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'python_app',
    password = 'Python@123',
    database = 'camerin_students',
    port = 3306

)
print("MySql in connection is successfull")

try:
    with connection.cursor() as cursor:
        # cursor.execute("SELECT * FROM STUDENTS")
        # records = cursor.fetchmany()

        # print(records)
        # for record in records :
        #     print(record)
        # 
        # query = """
        #         INSERT INTO STUDENTS
        #         VALUES (%s,%s,%s,%s)
        #     """

        # values = (108,'Akhil','akhil@gmail.com','kochi')
        # cursor.execute(query,values)
        # connection.commit()

        # query = """ ALTER TABLE STUDENTS
        #             ADD COLUMN PHONE VARCHAR(15) NOT NULL DEFAULT '111111111'
        #             """

        # cursor.execute(query)
        # print("Column created successfully...")

        # query = 'DESC students'
        # cursor.execute(query)

        # result = cursor.fetchall()
        # for col in result:
        #     print(col)
        # query = """ ALTER TABLE STUDENTS
        #         MODIFY PHONE INT DEFAULT '111111111'
        #         
        # """

        # query = """ ALTER TABLE STUDENTS
        #                 rename column PHONE to contact_number;
        # #                 """
        # query = """ ALTER TABLE STUDENTS
        #             drop column contact_number;
        #                         """







        
        cursor.execute(query)
        connection.commit()
        print("Column created successfully...")
        
        query = 'DESC students'
        cursor.execute(query)
        
        result = cursor.fetchall()
        for col in result:
                    print(col)



except:
    print("Something went wrong")

finally:    
    connection.close()
    print("Operation completed")