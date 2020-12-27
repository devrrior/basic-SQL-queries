# import psycopg2 as db
import mysql.connector as db

class DataBase:


    def __init__(self):

        self.__connection = db.connect(
            host = 'den1.mysql2.gear.host',
            database = 'testdata0',
            user = 'testdata0',
            password = 'Er26-!o7TX9I'
        )

        self.__cursor = self.__connection.cursor()

    def print_user(self):

        sentence = 'SELECT * FROM contacto'

        try:

            self.__cursor.execute(sentence)

            for user in self.__cursor.fetchall():
                print('ID:', user[0])
                print('Nombre:', user[1])
                print('Apellido:', user[2])
                print('Email:', user[3])
                print('____________\n')

        except Exception as e:
            raise e
        

    def select_user(self,data):

        sentence = 'SELECT * FROM contacto WHERE id_user = %s'
        self.__cursor.execute(sentence,data)

    def add_user(self,data,many):

        sentence = 'INSERT INTO contacto (nombre,apellido,email) VALUES(%s ,%s ,%s)'

        try:

            if many == True:

                self.__cursor.executemany(sentence,data)
                
            else:

                self.__cursor.execute(sentence,data)

            self.__connection.commit()
 
        except Exception as e:
            raise e

    def update_user(self,data,many):

        sentence = 'UPDATE contacto SET nombre = %s, apellido = %s, email = %s WHERE id_user = %s'

        try:
            if many == True:

                self.__cursor.executemany(sentence,data)
                
            else:

                self.__cursor.execute(sentence,data)

            self.__connection.commit()
 
        except Exception as e:
            raise e



    def delete_user(self,data,many):

        sentence = 'DELETE FROM contacto WHERE id_user = %s'

        try:

            if many == True:

                self.__cursor.executemany(sentence,data)
                
            else:

                self.__cursor.execute(sentence,data)

            self.__connection.commit()
 
        except Exception as e:
            raise e



    def get_cursor(self):
        return self.__cursor
