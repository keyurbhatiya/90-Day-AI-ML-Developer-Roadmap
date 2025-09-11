# Day 5: Probability Basics & Bayes' Theorem
# -------------------------------------------
# In this tutorial, we will learn:
# 1. Probability Basics
# 2. Conditional Probability
# 3. Bayes' Theorem

import random

# -----------------------------
# 1. Probability Basics
# -----------------------------
# Probability = (Number of favorable outcomes) / (Total possible outcomes)

# Example: Rolling a dice
dice_outcomes = [1, 2, 3, 4, 5, 6]
favorable = [6]  # Probability of rolling a 6
prob_6 = len(favorable) / len(dice_outcomes)

print("🎲 Probability Basics")
print("Probability of rolling a 6:", prob_6)

# Another Example: Coin Toss
coin_outcomes = ["H", "T"]
prob_head = coin_outcomes.count("H") / len(coin_outcomes)

print("Probability of getting Head in a coin toss:", prob_head)

# -----------------------------
# 2. Conditional Probability
# -----------------------------
# P(A|B) = Probability of A happening given B has already happened

# Example: Deck of 52 cards (simplified for red & black)
red_cards = 26
black_cards = 26
total_cards = 52

# Probability of drawing a red card first
P_red = red_cards / total_cards

# Now, probability of drawing another red card given one red card is already drawn
P_red_given_red = (red_cards - 1) / (total_cards - 1)

print("\n🎴 Conditional Probability")
print("P(Red):", P_red)
print("P(Red | Red already drawn):", P_red_given_red)

# -----------------------------
# 3. Bayes' Theorem
# -----------------------------
# Formula:
# P(A|B) = [ P(B|A) * P(A) ] / P(B)

# Example: Medical Test
# - 1% of population has a disease (P(Disease) = 0.01)
# - Test is 99% accurate if person has disease (P(Positive|Disease) = 0.99)
# - Test gives false positive 5% of the time (P(Positive|No Disease) = 0.05)

P_D = 0.01          # Probability of Disease
P_not_D = 0.99      # Probability of No Disease
P_Pos_given_D = 0.99
P_Pos_given_not_D = 0.05

# Total Probability of Positive Test
P_Pos = (P_Pos_given_D * P_D) + (P_Pos_given_not_D * P_not_D)

# Applying Bayes’ theorem: P(Disease | Positive Test)
P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos

print("\n🧪 Bayes' Theorem Example")
print("Probability of Disease given Positive Test:", round(P_D_given_Pos, 4))


'''
Explanation

Probability = chance of an event happening.

Conditional Probability (P(A|B)) = probability of event A given B has already occurred.

Bayes’ Theorem helps update probability when new evidence is given:

𝑃(𝐴∣𝐵)=𝑃(𝐵∣𝐴)⋅𝑃(𝐴)𝑃(𝐵) P(A∣B)=P(B∣A)⋅P(A)P(B)


🔍 In the medical test example, even with a 99% accurate test, the actual probability of having the disease after testing positive is only 16.7% because the disease is rare.
'''
