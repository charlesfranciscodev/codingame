def suggestion_engine(question_prefix, num_questions, questions):
    matching_questions = [q for q in questions if q.startswith(question_prefix)]
    
    if matching_questions:
        for q in matching_questions:
            print(q)
    else:
        print("EMPTY")

# Input
question_prefix = input().strip()
num_questions = int(input().strip())
questions = [input().strip() for _ in range(num_questions)]

# Output
suggestion_engine(question_prefix, num_questions, questions)
