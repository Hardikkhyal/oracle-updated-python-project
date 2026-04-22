from core.db import get_connection

def mark_attendance(emp_id, date, status):
    conn = get_connection()
    cur = conn.cursor()

    # Oracle uses date_col instead of date
    if conn.__class__.__module__.startswith("cx_Oracle"):
        cur.execute("INSERT INTO attendance (emp_id, date_col, status) VALUES (:1,:2,:3)",
                    (emp_id, date, status))
    else:
        cur.execute("INSERT INTO attendance (emp_id, date, status) VALUES (%s,%s,%s)",
                    (emp_id, date, status))

    conn.commit()
    conn.close()
    print("Attendance Marked.")

def count_absent(emp_id, month, year):
    conn = get_connection()
    cur = conn.cursor()

    if conn.__class__.__module__.startswith("cx_Oracle"):
        query = """
        SELECT COUNT(*) FROM attendance
        WHERE emp_id=:1 AND status='ABSENT'
        AND EXTRACT(MONTH FROM date_col)=:2 AND EXTRACT(YEAR FROM date_col)=:3
        """
        cur.execute(query, (emp_id, month, year))
    else:
        query = """
        SELECT COUNT(*) FROM attendance
        WHERE emp_id=%s AND status='ABSENT'
        AND MONTH(date)=%s AND YEAR(date)=%s
        """
        cur.execute(query, (emp_id, month, year))

    count = cur.fetchone()[0]
    conn.close()
    return count