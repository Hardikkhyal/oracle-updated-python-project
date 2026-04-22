# HR Payroll Management System (Python Backend)

## 1. Project Info
This is a simple student-level backend system for managing HR payroll using Python + SQL + Oracle.

## 2. Features
- Add / update / list employees
- Mark attendance
- Generate payroll
- Monthly payroll report
- Salary slip

## 3. Requirements
- Python 3.9+
- MySQL OR Oracle
- pip install requirements

## 4. Setup Steps

### Step 1: Create Database
#### MySQL:
```sql
CREATE DATABASE payroll_db;
```

#### Oracle:
Create a user and grant permissions.

### Step 2: Create Tables
Run schema file:
- db/mysql_schema.sql (MySQL)
- db/oracle_schema.sql (Oracle)

### Step 3: Install Python Requirements
```bash
pip install -r requirements.txt
```

### Step 4: Configure .env
Copy .env.example to .env and update values.

### Step 5: Run Project
```bash
python run.py
```

## 5. Optional: Insert Sample Data
```bash
python sample_data.py
```