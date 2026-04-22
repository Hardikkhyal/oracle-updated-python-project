from core.db import get_connection
from core.attendance import count_absent
from core.db_helpers import is_oracle, param

def generate_payroll(emp_id, month, year):
    conn = get_connection()
    cur = conn.cursor()
    oracle = is_oracle(conn)

    if oracle:
        cur.execute("SELECT base_salary FROM employees WHERE emp_id=:1", (emp_id,))
    else:
        cur.execute("SELECT base_salary FROM employees WHERE emp_id=%s", (emp_id,))

    salary = cur.fetchone()[0]

    absent_days = count_absent(emp_id, month, year)
    per_day = salary / 30
    tax = salary * 0.05
    deductions = (absent_days * per_day) + tax
    net = salary - deductions

    placeholders = param(6, oracle)
    sql = f"INSERT INTO payroll (emp_id, month, year, gross, deductions, net) VALUES ({placeholders})"
    cur.execute(sql, (emp_id, month, year, salary, deductions, net))

    conn.commit()
    conn.close()
    print("Payroll Generated.")