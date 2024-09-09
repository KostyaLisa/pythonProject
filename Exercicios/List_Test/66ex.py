# Create a home loan simulator
# simple and free of charge, requesting the name,
# year of birth, monthly income,
# monthly expenses, credit amount and
# term in years, keeping everything within a
# dictionary. Calculate by adding to
# dictionary, age, remainder after
# expenses, how much you should pay monthly
# for credit and whether the credit was approved
# whenever the remainder is greater than the
# monthly credit amount.


# Example usage:


# Create a dictionary for the loan application
loan_application = {
    "name": "John Doe",
    "year_of_birth": 1990,
    "monthly_income": 5000,
    "monthly_expenses": 3000,
    "credit_amount": 10000,
    "term_in_years": 3
}


# Calculate age
loan_application["age"] = 2023 - loan_application["year_of_birth"]


# Calculate remaining after expenses
loan_application["remaining_after_expenses"] = loan_application["monthly_income"] - loan_application["monthly_expenses"]


# Calculate monthly credit amount
loan_application["monthly_credit_amount"] = loan_application["credit_amount"] / (loan_application["term_in_years"] * 12)


# Calculate monthly payment
loan_application["monthly_payment"] = loan_application["remaining_after_expenses"] / (loan_application["term_in_years"] * 12)


# Check if credit was approved
if loan_application["remaining_after_expenses"] > loan_application["monthly_credit_amount"]:
    print(f"Credit was approved. Monthly payment: {loan_application['monthly_payment']:.2f}")
else:
    print("Credit was not approved.")

