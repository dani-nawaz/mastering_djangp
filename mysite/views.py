from django.shortcuts import render
import MySQLdb
def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb',  passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request, 'book_list.html', {'names': names})