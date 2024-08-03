import math

def compound_interest(P, r, n, t):
    return P * (1 + r / n) ** (n * t)

def loan_payment(P, r, n):
    if r == 0:
        return P / n
    monthly_rate = r / 12
    return P * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)

def investment_return(PV, r, t):
    return PV * (1 + r) ** t

def simple_interest(P, r, t):
    return P * r * t

def annuity_payment(PV, r, n):
    if r == 0:
        return PV / n
    return PV * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

financial_calculations = {
    'compound_interest': compound_interest,
    'loan_payment': loan_payment,
    'investment_return': investment_return,
    'simple_interest': simple_interest,
    'annuity_payment': annuity_payment
}

def financial_calculator(operation, **kwargs):
    if operation in financial_calculations:
        return financial_calculations[operation](**kwargs)
    else:
        return f"Operation '{operation}' is not supported."

# Example usage
print(financial_calculator('compound_interest', P=1000, r=0.05, n=12, t=10))  # Compound interest
print(financial_calculator('loan_payment', P=50000, r=0.05, n=60))            # Loan payment
print(financial_calculator('investment_return', PV=1000, r=0.07, t=5))        # Investment return
print(financial_calculator('simple_interest', P=1000, r=0.05, t=10))          # Simple interest
print(financial_calculator('annuity_payment', PV=10000, r=0.05, n=10))        # Annuity payment
