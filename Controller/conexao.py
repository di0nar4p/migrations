import psycopg2
import getpass as psw

def connect():
    try:
        conn = psycopg2.connect(database = "estudos",
                           host = "localhost",
                           user = "postgres",
                           password = 'root',
                           port = 5432)
    except Exception as error:
        raise error('Deu ruim')
    else:
        
        print('Sucessfully connected')
        return conn
    



