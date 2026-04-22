import mysql.connector
import cx_Oracle
from config import DB_TYPE, MYSQL_CONFIG, ORACLE_CONFIG

def get_connection():
    if DB_TYPE == "mysql":
        return mysql.connector.connect(**MYSQL_CONFIG)
    elif DB_TYPE == "oracle":
        return cx_Oracle.connect(
            ORACLE_CONFIG["user"],
            ORACLE_CONFIG["password"],
            ORACLE_CONFIG["dsn"]
        )
    else:
        raise Exception("Invalid DB_TYPE in .env")