from celery import Celery
import pymysql
pymysql.install_as_MySQLdb()

broker_url = 'sqla+mysql://temp_user:pass1234@localhost:3306/temp'
backend_url =  'db+mysql://temp_user:pass1234@localhost:3306/temp'


# define app
app = Celery('tasks', broker=broker_url, backend=backend_url)

# create task
@app.task
def add(x, y):
    return x+y
