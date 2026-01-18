from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

# creating pydantic base model
class Applicant(BaseModel):
    income: float
    age: int
    employment_status : str


# Defining the endpoints
@app.post('/loan-eligibility')

# creating route handler 
def check_eligibility(applicant: Applicant): 
# input expected is object of the applicant
# how to check? we can test it directly as we dont have 
# explicit logic function to run and check. we create the logic here itself
    if (applicant.income>= 50000) and (applicant.age>= 21) and (applicant.employment_status == 'employed'):
        return {'eligible': True}
    else:
        return {'eligible': False}
    

