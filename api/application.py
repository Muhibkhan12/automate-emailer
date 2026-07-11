from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    age: int
    income: float
    income_years: float
    employment_year: int

@app.post("/loan_approval")
def salary_approval(application: LoanApplication):

    if application.age > 25 and application.employment_year > 5:
        decision = "Eligible for loan"
    else:
        decision = "Not eligible for loan"

    return {
        "message": decision,
        "application_age": application.age,
    }