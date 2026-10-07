"""
Question 2 - Bayes' Theorem (Two Clinics)
Run:  python q2_bayes_clinics.py
"""
# Clinic 1: 3 pediatric + 4 cardiology = 7 doctors
# Clinic 2: 6 pediatric + 2 cardiology = 8 doctors
p_c1 = p_c2 = 0.5                       # clinic chosen at random
p_card_c1 = 4 / 7                       # P(cardiologist | clinic 1)
p_card_c2 = 2 / 8                       # P(cardiologist | clinic 2)

joint_c1 = p_c1 * p_card_c1
joint_c2 = p_c2 * p_card_c2
p_card = joint_c1 + joint_c2            # total probability of evidence

p_c2_given_card = joint_c2 / p_card     # Bayes' rule

print("=" * 60)
print("QUESTION 2 - P(Clinic 2 | Doctor is a Cardiologist)")
print("=" * 60)
print(f"{'Clinic':<22}{'Prior':<10}{'P(Card|Clinic)':<16}{'Joint':<10}{'Posterior':<10}")
print("-" * 60)
print(f"{'Clinic 1 (3P + 4C)':<22}{p_c1:<10.2f}{p_card_c1:<16.4f}{joint_c1:<10.4f}{joint_c1/p_card:<10.4f}")
print(f"{'Clinic 2 (6P + 2C)':<22}{p_c2:<10.2f}{p_card_c2:<16.4f}{joint_c2:<10.4f}{joint_c2/p_card:<10.4f}")
print("-" * 60)
print(f"{'Total':<22}{'1.00':<10}{'-':<16}{p_card:<10.4f}{'1.00':<10}")
print()
print(f"ANSWER: P(Clinic 2 | Cardiology) = {p_c2_given_card:.4f}  (7/23, about {p_c2_given_card*100:.1f}%)")
