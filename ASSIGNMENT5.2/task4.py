def get_applicant_input():
    print("Enter applicant details:")
    education = input("Education (High School/Bachelor/Master/PhD): ").strip()
    try:
        experience = int(input("Years of Experience: "))
    except ValueError:
        print("Invalid input for experience. Setting to 0.")
        experience = 0
    gender = input("Gender (Male/Female/Other): ").strip()
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid input for age. Setting to 0.")
        age = 0
    return {
        "education": education,
        "experience": experience,
        "gender": gender,
        "age": age
    }

def score_applicant(applicant):
    # Scoring logic
    score = 0

    # Education scoring
    education_scores = {
        "High School": 10,
        "Bachelor": 20,
        "Master": 30,
        "PhD": 40
    }
    edu_score = education_scores.get(applicant["education"], 0)
    score += edu_score

    # Experience scoring (2 points per year, up to 20 years)
    exp_score = min(applicant["experience"], 20) * 2
    score += exp_score

    # Gender scoring (should be neutral, so 0 for all)
    gender_score = 0
    score += gender_score

    # Age scoring (prefer 22-60, penalize outside)
    if 22 <= applicant["age"] <= 60:
        age_score = 10
    else:
        age_score = -5
    score += age_score

    return score

def analyze_scoring_logic():
    print("\nScoring Logic Analysis:")
    print("- Education: Higher degrees get higher scores (High School:10, Bachelor:20, Master:30, PhD:40).")
    print("- Experience: 2 points per year, up to 20 years (max 40 points).")
    print("- Gender: No points given, so no bias here.")
    print("- Age: 10 points for ages 22-60, -5 otherwise (may disadvantage very young or older applicants).")
    print("\nPotential Biases/Unfair Weightings:")
    print("- Education: May disadvantage skilled applicants without formal degrees.")
    print("- Age: Penalizes applicants outside 22-60, which could be ageist.")
    print("- Gender: No explicit bias, but always review for indirect effects.")
    print("- Experience: Caps at 20 years, so very experienced applicants get no extra benefit.")

def main():
    applicant = get_applicant_input()
    score = score_applicant(applicant)
    print(f"\nApplicant Score: {score} (out of a possible 90)")
    analyze_scoring_logic()

if __name__ == "__main__":
    main()
