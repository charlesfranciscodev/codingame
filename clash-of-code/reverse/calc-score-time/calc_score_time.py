def calculate_score(time_str):
    hours, minutes = map(int, time_str.split(':'))
    score = hours * 60 + minutes
    return score

duration = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(calculate_score(duration))
