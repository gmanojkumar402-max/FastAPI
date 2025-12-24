from fastapi import FastAPI, HTTPException
from models_val import Employee

employees_db: list[Employee] = []  # in-memory "DB"

app = FastAPI()

# Read all employees
@app.get("/employees", response_model=list[Employee])
def get_employees():
    return employees_db

# Read specific employee
@app.get("/employee/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for employee in employees_db:
        if employee.id == emp_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee Not Found")

# Add an Employee
@app.post("/employees", response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee already exists")
    employees_db.append(new_emp)
    return new_emp

# Update an employee
@app.put("/update_employee/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    # Optional safety check (recommended)
    if updated_employee.id != emp_id:
        raise HTTPException(status_code=400, detail="Employee ID in body must match emp_id in path")

    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee

    raise HTTPException(status_code=404, detail="Employee Not Found")

# Delete an employee
@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {"message": "Employee deleted successfully"}

    raise HTTPException(status_code=404, detail="Employee Not Found")
