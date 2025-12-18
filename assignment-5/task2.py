# ...existing code...
import math
from typing import Dict, Tuple, List

def monthly_payment(loan_amount: float, annual_rate: float, years: int) -> float:
    if loan_amount == 0 or years == 0:
        return 0.0
    r = annual_rate / 12.0
    n = years * 12
    if r == 0:
        return loan_amount / n
    return loan_amount * r * (1 + r) ** n / ((1 + r) ** n - 1)

def score_applicant(app: Dict) -> Tuple[int, List[str]]:
    score = 0
    reasons = []

    age = app.get("age", 0)
    if age < 21 or age > 65:
        reasons.append(f"Age {age} outside 21-65 -> auto reject")
        return -999, reasons  # auto reject sentinel

    # Employment history
    emp_years = app.get("employment_years", 0)
    if emp_years >= 5:
        score += 20
    elif emp_years >= 1:
        score += 5
    else:
        score -= 20
        reasons.append(f"Low employment history: {emp_years} years")

    # Income
    income = app.get("annual_income", 0)
    if income >= 100_000:
        score += 40
    elif income >= 50_000:
        score += 20
    elif income >= 30_000:
        score += 5
    else:
        score -= 15
        reasons.append(f"Low income: ${income:,.0f}")

    # Credit score
    cs = app.get("credit_score", 600)
    if cs >= 780:
        score += 40
    elif cs >= 720:
        score += 25
    elif cs >= 660:
        score += 10
    elif cs >= 600:
        score -= 5
        reasons.append(f"Fair credit score: {cs}")
    else:
        score -= 25
        reasons.append(f"Poor credit score: {cs}")

    # Interest rate tier by credit score (used for payment calc)
    if cs >= 720:
        rate = 0.05
    elif cs >= 660:
        rate = 0.08
    elif cs >= 600:
        rate = 0.12
    else:
        rate = 0.18

    loan_amount = app.get("loan_amount", 0)
    term_years = app.get("term_years", 5)
    monthly_inc = income / 12.0 if income > 0 else 0.0
    monthly_debt = app.get("monthly_debt", 0)
    payment = monthly_payment(loan_amount, rate, term_years)
    dti = (monthly_debt + payment) / monthly_inc if monthly_inc > 0 else 1.0
    # DTI scoring
    if dti <= 0.35:
        score += 30
    elif dti <= 0.45:
        score += 10
    elif dti <= 0.5:
        score -= 5
        reasons.append(f"High DTI: {dti:.2f}")
    else:
        score -= 30
        reasons.append(f"Very high DTI: {dti:.2f}")
    # Loan-to-income ratio
    li_ratio = loan_amount / income if income > 0 else 10.0
    if li_ratio <= 0.5:
        score += 10
    else:
        score -= 10
        reasons.append(f"Loan/Income ratio high: {li_ratio:.2f}")
    # Final normalization
    return score, reasons
def decision_from_score(score: int) -> Tuple[str, str]:
    if score == -999:
        return "Rejected", "Automatic reject due to hard rule (age etc.)"
    if score >= 70:
        return "Approved", "Low risk"
    if score >= 35:
        return "Approved (with conditions)", "Medium risk — consider higher rate or collateral"
    if score >= 0:
        return "Manual review", "Borderline — request documents"
    return "Rejected", "High risk"
def analyze_applicant(app: Dict) -> Dict:
    score, reasons = score_applicant(app)
    decision, note = decision_from_score(score)
    # include calculation details
    income = app.get("annual_income", 0)
    loan_amount = app.get("loan_amount", 0)
    cs = app.get("credit_score", 0)
    term = app.get("term_years", 5)
    if score != -999:
        rate = 0.05 if cs >= 720 else 0.08 if cs >= 660 else 0.12 if cs >= 600 else 0.18
        payment = monthly_payment(loan_amount, rate, term)
        monthly_inc = income / 12.0 if income > 0 else 0.0
        dti = (app.get("monthly_debt", 0) + payment) / monthly_inc if monthly_inc > 0 else None
    else:
        payment = None
        dti = None
        rate = None
    return {
        "name": app.get("name"),
        "gender": app.get("gender"),
        "decision": decision,
        "decision_note": note,
        "score": score,
        "reasons": reasons,
        "monthly_payment": round(payment, 2) if payment is not None else None,
        "rate": rate,
        "dti": round(dti, 2) if dti is not None else None
    }
def sample_run():
    sample_applicants = [
        {"name":"Aisha Khan","gender":"F","age":29,"annual_income":120000,"employment_years":6,"credit_score":790,"loan_amount":20000,"term_years":5,"monthly_debt":200},
        {"name":"Raj Patel","gender":"M","age":34,"annual_income":48000,"employment_years":2,"credit_score":710,"loan_amount":15000,"term_years":4,"monthly_debt":300},
        {"name":"Taylor Morgan","gender":"Non-binary","age":22,"annual_income":32000,"employment_years":0.5,"credit_score":650,"loan_amount":10000,"term_years":3,"monthly_debt":150},
        {"name":"Li Wei","gender":"M","age":45,"annual_income":28000,"employment_years":8,"credit_score":590,"loan_amount":8000,"term_years":2,"monthly_debt":400},
        {"name":"Maria Garcia","gender":"F","age":66,"annual_income":90000,"employment_years":20,"credit_score":760,"loan_amount":30000,"term_years":7,"monthly_debt":100}
    ]
    results = [analyze_applicant(a) for a in sample_applicants]
    for r in results:
        print(f"{r['name']} ({r['gender']}): Decision={r['decision']} | Score={r['score']}")
        print(f"  Note: {r['decision_note']}")
        if r['reasons']:
            print(f"  Reasons: {', '.join(r['reasons'])}")
        print(f"  Rate={r['rate']}, Monthly payment={r['monthly_payment']}, DTI={r['dti']}")
        print("-" * 60)
def interactive_mode():
    print("Loan approval quick analysis. Press Enter to use default where shown.")
    name = input("Name: ").strip() or "Applicant"
    gender = input("Gender: ").strip() or "Unspecified"
    age = int(input("Age: ").strip() or "30")
    income = float(input("Annual income (numbers): ").strip() or "50000")
    emp = float(input("Employment years: ").strip() or "2")
    cs = int(input("Credit score (300-850): ").strip() or "700")
    loan = float(input("Loan amount requested: ").strip() or "10000")
    term = int(input("Term (years): ").strip() or "5")
    debt = float(input("Monthly other debt payments: ").strip() or "0")
    app = {
        "name": name, "gender": gender, "age": age, "annual_income": income,
        "employment_years": emp, "credit_score": cs, "loan_amount": loan,
        "term_years": term, "monthly_debt": debt
    }
    r = analyze_applicant(app)
    print("\nResult:")
    print(f"{r['name']} ({r['gender']}): Decision={r['decision']} | Score={r['score']}")
    print(f"  Note: {r['decision_note']}")
    if r['reasons']:
        print(f"  Reasons: {', '.join(r['reasons'])}")
    print(f"  Rate={r['rate']}, Monthly payment={r['monthly_payment']}, DTI={r['dti']}")
if __name__ == "__main__":
    print("1) Run sample applicants\n2) Interactive analyze\nChoose (1/2): ", end="")
    choice = input().strip()
    if choice == "2":
        interactive_mode()
    else:
        sample_run()
# ...existing code...