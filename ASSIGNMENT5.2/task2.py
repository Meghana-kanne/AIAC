def approve_loan(applicant):
    """
    Dummy loan approval logic.
    For demonstration, let's say the code (incorrectly) uses the name to infer gender and biases approval.
    """
    male_names = ['John', 'Ali']
    female_names = ['Priya', 'Meena']
    if applicant['name'] in male_names:
        gender = 'male'
    elif applicant['name'] in female_names:
        gender = 'female'
    else:
        gender = 'unknown'
    if gender == 'male' and applicant['experience'] >= 2:
        return True
    elif gender == 'female' and applicant['experience'] >= 4:
        return True
    elif applicant['experience'] >= 5:
        return True
    else:
        return False
test_applicants = [
    {'name': 'John', 'age': 30, 'education': 'Masters', 'experience': 3, 'gender_identity': 'Not specified'},
    {'name': 'Priya', 'age': 28, 'education': 'Masters', 'experience': 3, 'gender_identity': 'Not specified'},
    {'name': 'Ali', 'age': 35, 'education': 'Bachelors', 'experience': 3, 'gender_identity': 'Not specified'},
    {'name': 'Meena', 'age': 32, 'education': 'PhD', 'experience': 3, 'gender_identity': 'Not specified'},
]

print("Testing loan approval with potentially biased logic:")
for applicant in test_applicants:
    result = approve_loan(applicant)
    print(f"Applicant: {applicant['name']}, Experience: {applicant['experience']} -> Approved: {result}")

print("\n---\n")
def approve_loan_unbiased(applicant):
    """
    Unbiased loan approval logic: Only considers experience (and possibly education), not name/gender.
    """
    if applicant['experience'] >= 3:
        return True
    else:
        return False

print("Testing loan approval with unbiased logic:")
for applicant in test_applicants:
    result = approve_loan_unbiased(applicant)
    print(f"Applicant: {applicant['name']}, Experience: {applicant['experience']} -> Approved: {result}")
