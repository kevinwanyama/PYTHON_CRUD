import db_connection as dbconn;


class Update:
    def func_UpdateData(self):
        # Get the sqlconnection
        connection = dbconn.getConnection()

        id = input('Enter Employee Id = ')

        try:
            # Fetch data that needs to be updated
            sql = "select * from Employee where Id = ?"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t age')
            print('------------------------------------------')
            print('{}\t\t {} \t\t\t{}'.format(item[0], item[1], item[2]))
            print('------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = input('Enter new Name = ')
            age = input('Enter new age = ')
            query = "update Employee set Names =?, Age =? where Id =?"

            # Execute the update query
            cursor.execute(query, [name, age, id])
            connection.commit()
            print('Data updated successfully')
        except:
            print('Something wrong, please check')
        finally:
            # close the connection
            connection.close()
