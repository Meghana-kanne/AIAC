def collect_applicant_info():
    """
    Collects applicant information in a gender-neutral way.
    Returns a dictionary with the applicant's details.
    """
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    education = input("Enter your highest education qualification: ")
    experience = int(input("Enter your years of experience: "))
    # Gender-neutral: Do not ask for gender, or allow self-description
    gender_identity = input("Optionally, describe your gender identity (or press Enter to skip): ")
    applicant = {
        "name": name,
        "age": age,
        "education": education,
        "experience": experience,
        "gender_identity": gender_identity if gender_identity.strip() else "Not specified"
    }
    return applicant

def print_applicant_info(applicant):
    print("\nApplicant Information:")
    print(f"Name: {applicant['name']}")
    print(f"Age: {applicant['age']}")
    print(f"Education: {applicant['education']}")
    print(f"Experience: {applicant['experience']} years")
    print(f"Gender Identity: {applicant['gender_identity']}")

if __name__ == "__main__":
    applicant = collect_applicant_info()
    print_applicant_info(applicant)
