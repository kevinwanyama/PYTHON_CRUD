import db_connection as dbconn


class Create:
    def func_CreateData(self):
        # Get the sql connection
        connection = dbconn.getConnection()

        names = input('Enter Names = ')
        age = input('Enter Age = ')

        try:
            query = "INSERT INTO Employee(Names, Age ) Values (?,?)"
            cursor = connection.cursor()

            # Execute the sql query
            cursor.execute(query, [names, age])

            # Commit the data
            connection.commit()
            print('Data saved successfully')

        except:
            print('Something wrong, please check')

        finally:
            # close the connection
            connection.close()
