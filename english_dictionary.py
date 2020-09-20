import mysql.connector

con = mysql.connector.connect(
    user="cg77534_english",
    password="english123456",
    host="vh238.timeweb.ru",
    database="cg77534_english"
)
# Only for IP 77.138.227.4

cursor = con.cursor()

word = input("Enter the word: ")

query = cursor.execute("SELECT definition, wordtype FROM entries WHERE word = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(f'Description:{result[0]}\n Word type: {result[1]}')
else:
    print("No word found!")
