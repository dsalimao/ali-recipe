import queue
import pymysql
from config import Config


class ConnectionPool:

    def __init__(self, maxsize=10):
        self._queue = queue.Queue(maxsize=maxsize)

        for i in range(maxsize):
            self._put(self._create())

    def _create(self):
        config = Config()
        conn = pymysql.connect(host=config.mysql_host,
                               user=config.mysql_user,
                               passwd=config.mysql_passwd,
                               db=config.mysql_db,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        return conn

    def _put(self, conn):
        self._queue.put(conn)

    def _get(self):
        conn = self._queue.get()
        if conn is None:
            return self._create()

        return conn

    def execute(self, sql, args=None, exec_many=False, return_one=False):
        """
        execute
        :param sql: sql
        :param args: parameters
        :param exec_many: if use `cur.executemany(sql, args)`
        :param return_one: true: `cur.fetchone()`, false: 'cur.fetchall()'
        """
        conn = self._get()
        try:
            with conn as cur:
                if exec_many:
                    cur.executemany(sql, args)
                else:
                    cur.execute(sql, args)
                return cur.fetchone() if return_one else cur.fetchall()

        except Exception as e:
            raise e

        finally:
            self._queue.put(conn)

    def __del__(self):
        while not self._queue.empty():
            conn = self._queue.get_nowait()
            if conn:
                conn.close()


mysql_pool = ConnectionPool()