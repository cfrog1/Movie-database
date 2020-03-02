import mysql.connector

HOST='localhost'
USER='YOUR-MYSQL-USER'
PASSWORD='YOUR-MYSQL-PASSWORD'
DATABASE='YOUR-MYSQL-SCHEMA'


def connect():
    #Ensures table of movies exists
    conn = mysql.connector.connect(HOST,USER,PASSWORD,DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (Title VARCHAR(255) PRIMARY KEY, Year YEAR, \
        RT_rating TINYINT, Director VARCHAR(255))")
    conn.commit()
    conn.close()

def insert(title, year, rating, director):
    #Inserts a new row in movies
    conn = mysql.connector.connect(HOST,USER,PASSWORD,DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT IGNORE INTO movies VALUES (%s, %s, %s, %s)", (title, year, rating, director))
    conn.commit()
    conn.close()

def view():
    #Returns all movies
    conn = mysql.connector.connect(HOST,USER,PASSWORD,DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    results = cursor.fetchall()
    conn.close()
    return results

def search(title='', year='', rating='', director=''):
    #Returns all rows that match search criteria
    conn = mysql.connector.connect(HOST,USER,PASSWORD,DATABASE)
    cursor = conn.cursor()

    #Replaces blank search terms with wildcards for SQL
    search_terms = (title if title != '' else '%', year if year != '' else '%',
     rating if rating != '' else '%', director if director != '' else '%')

    cursor.execute("SELECT * FROM movies WHERE Title LIKE %s AND Year LIKE %s AND \
        RT_rating LIKE %s AND Director LIKE %s", search_terms)
    results = cursor.fetchall()
    conn.close()
    return results

def delete(title):
    #Deletes record from movies
    conn = mysql.connector.connect(HOST,USER,PASSWORD,DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE title=%s", (title,))
    conn.commit()
    conn.close()

def update(title, year, RT_rating, director):
    #Updates given movie with new details
    conn = mysql.connector.connect(HOST,USER,PASSWORD,DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET Year=%s, RT_rating=%s, Director=%s WHERE Title=%s", 
    (year,RT_rating,director,title))
    conn.commit()
    conn.close()

