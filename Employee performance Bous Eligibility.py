employees = { "Ravi": 92, "Anita": 88, "Kiran": 92, "Suresh": 85}
max_score = max(employees.values())
top_performers = [name for name, score in employees.items() if score == max_score]
print("Top Performers Eligible for Bonus:", ", ".join(top_performers), f"(Score: {max_score})")