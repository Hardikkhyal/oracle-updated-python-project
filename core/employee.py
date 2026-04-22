from core.db import get_connection
from core.db_helpers import is_oracle, param

def add_employee(emp_id, name, dept, desig, join_date, salary, status):
    conn = get_connection()
    cur = conn.cursor()
    oracle = is_oracle(conn)

    placeholders = param(7, oracle)
    sql = f"INSERT INTO employees VALUES ({placeholders})"

    cur.execute(sql, (emp_id, name, dept, desig, join_date, salary, status))
    conn.commit()
    conn.close()
    print("Employee Added.")

def list_employees():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        print(r)

def update_status(emp_id, status):
    conn = get_connection()
    cur = conn.cursor()
    oracle = is_oracle(conn)

    if oracle:
        cur.execute("UPDATE employees SET status=:1 WHERE emp_id=:2", (status, emp_id))
    else:
        cur.execute("UPDATE employees SET status=%s WHERE emp_id=%s", (status, emp_id))

    conn.commit()
    conn.close()
    print("Status Updated.")