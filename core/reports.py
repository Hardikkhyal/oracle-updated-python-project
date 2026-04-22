from core.db import get_connection
from core.db_helpers import is_oracle

def monthly_report(month, year):
    conn = get_connection()
    cur = conn.cursor()
    oracle = is_oracle(conn)

    if oracle:
        cur.execute("SELECT * FROM payroll WHERE month=:1 AND year=:2", (month, year))
    else:
        cur.execute("SELECT * FROM payroll WHERE month=%s AND year=%s", (month, year))

    rows = cur.fetchall()
    conn.close()
    for r in rows:
        print(r)

def salary_slip(emp_id, month, year):
    conn = get_connection()
    cur = conn.cursor()
    oracle = is_oracle(conn)

    if oracle:
        cur.execute("SELECT * FROM payroll WHERE emp_id=:1 AND month=:2 AND year=:3",
                    (emp_id, month, year))
    else:
        cur.execute("SELECT * FROM payroll WHERE emp_id=%s AND month=%s AND year=%s",
                    (emp_id, month, year))

    row = cur.fetchone()
    conn.close()
    print("Salary Slip:", row)