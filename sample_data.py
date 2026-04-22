from core.employee import add_employee
from core.attendance import mark_attendance

add_employee(1, "Amit", "HR", "Manager", "2023-06-01", 40000, "Active")
add_employee(2, "Neha", "IT", "Developer", "2022-01-15", 50000, "Active")

mark_attendance(1, "2026-04-01", "PRESENT")
mark_attendance(1, "2026-04-02", "ABSENT")
mark_attendance(2, "2026-04-01", "PRESENT")
