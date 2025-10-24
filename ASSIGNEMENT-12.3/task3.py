# Maximize 6*A + 5*B
# subject to:
#   1*A + 1*B <= 5          (Milk constraint)
#   3*A + 2*B <= 12         (Choco constraint)
#   A >= 0, B >= 0, integers

def maximize_chocolates():
    max_profit = -1
    best_A, best_B = 0, 0

    # A and B must be >= 0 and integer; try all possibilities within milk and choco limits
    for A in range(0, 6):  # Max 5 units of milk, so A <= 5
        for B in range(0, 6):  # same bound for B
            milk_used = A + B
            choco_used = 3*A + 2*B
            if milk_used <= 5 and choco_used <= 12:
                profit = 6*A + 5*B
                if profit > max_profit:
                    max_profit = profit
                    best_A = A
                    best_B = B
    print(f"Maximum profit is Rs {max_profit}")
    print(f"Produce {best_A} units of Chocolate A and {best_B} units of Chocolate B.")

if __name__ == "__main__":
    maximize_chocolates()
