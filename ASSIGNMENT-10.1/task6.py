def grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            if score >= 70:
                return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"
                # Cleaner logic using elif
                # Option 1: Using elif
                # Remove all nested else blocks and use elif for clarity

                # Option 1 implementation:
                # (Place this as the entire function body)

                if score >= 90:
                    return "A"
                elif score >= 80:
                    return "B"
                elif score >= 70:
                    return "C"
                elif score >= 60:
                    return "D"
                else:
                    return "F"
print(grade(55))  # Output: "F"
print(grade(95))  # Output: "A"
print(grade(85))  # Output: "B"
print(grade(75))  # Output: "C"
print(grade(65))  # Output: "D"
print(grade(55))  # Output: "F"

                # Option 2: Using dictionary mapping with ranges
                # (Alternative approach)

                # grades = {range(90, 101): "A", range(80, 90): "B", range(70, 80): "C", range(60, 70): "D"}
                # for r, grade_letter in grades.items():
                #     if score in r:
                #         return grade_letter
                # return "F"
                
                
                
