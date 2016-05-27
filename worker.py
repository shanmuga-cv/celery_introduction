from celery import Celery
from celery.bin.worker import worker

import my_celery

import pymysql
pymysql.install_as_MySQLdb()


if __name__ == '__main__':
    app = my_celery.app
    app_worker = worker(app=app)
    app_worker.run(loglevel='INFO')
