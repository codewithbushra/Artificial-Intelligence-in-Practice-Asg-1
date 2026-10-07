"""
Question 1 - Bayes' Theorem (Hospital / Rehabilitation Program)
Run:  python q1_bayes_hospital.py
"""
p_recover = 0.5                     # prior: 50% of patients recover
p_prog_given_recover = 0.4          # 40% of recovered patients followed the program
p_prog_given_not_recover = 0.1      # 10% of non-recovered patients followed the program

# Joint probabilities
joint_recover = p_recover * p_prog_given_recover
joint_not_recover = (1 - p_recover) * p_prog_given_not_recover

# Total probability of the evidence (following the program)
p_prog = joint_recover + joint_not_recover

# Bayes' rule: posterior probability
p_recover_given_prog = joint_recover / p_prog

print("=" * 55)
print("QUESTION 1 - P(Recover | Followed Program)")
print("=" * 55)
print(f"{'Event':<15}{'Prior':<10}{'Conditional':<13}{'Joint':<10}{'Posterior':<10}")
print("-" * 55)
print(f"{'Recover':<15}{p_recover:<10.2f}{p_prog_given_recover:<13.2f}{joint_recover:<10.2f}{joint_recover/p_prog:<10.2f}")
print(f"{'Not recover':<15}{1-p_recover:<10.2f}{p_prog_given_not_recover:<13.2f}{joint_not_recover:<10.2f}{joint_not_recover/p_prog:<10.2f}")
print("-" * 55)
print(f"{'Total':<15}{'1.00':<10}{'-':<13}{p_prog:<10.2f}{'1.00':<10}")
print()
print(f"ANSWER: P(Recover | Program) = {p_recover_given_prog:.2f}  ({p_recover_given_prog*100:.0f}%)")
