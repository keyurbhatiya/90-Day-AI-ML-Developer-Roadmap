'''

# 📘 Day 1 – Introduction to AI & Machine Learning

## 1. What is **Artificial Intelligence (AI)?**

* AI = Making computers **think and act like humans**.
* Example: ChatGPT, Siri, Google Maps, Self-driving cars.

---

## 2. What is **Machine Learning (ML)?**

* ML = A subset of AI where machines **learn patterns from data** instead of being explicitly programmed.
* Example:

  * Spam filter learns from past emails.
  * Netflix learns what movies you like and recommends.

👉 **AI is the goal. ML is one way to achieve AI.**

---

## 3. Types of Machine Learning

### 🔹 1. **Supervised Learning**

* Learn from **labeled data** (input → output).
* Model maps input → correct output.
* Example:

  * Email spam detection (`spam` / `not spam`).
  * Predicting house prices (input = size, location → output = price).
* Algorithms: Linear Regression, Logistic Regression, Decision Trees, SVM.

---

### 🔹 2. **Unsupervised Learning**

* Learn from **unlabeled data** (only input, no output).
* Model finds **hidden patterns**.
* Example:

  * Customer segmentation in marketing.
  * Grouping news articles by topics.
* Algorithms: K-Means, Hierarchical Clustering, PCA.

---

### 🔹 3. **Reinforcement Learning (RL)**

* Learn by **interacting with an environment**.
* Model gets **rewards/punishments** and learns best actions.
* Example:

  * AlphaGo (AI that beat humans in the Go game).
  * Self-driving cars (reward = safe driving, penalty = accidents).
* Algorithms: Q-Learning, Deep Q-Networks (DQN).

---

## 4. Comparison

| Type              | Data Needed            | Output         | Example             |
| ----------------- | ---------------------- | -------------- | ------------------- |
| **Supervised**    | Labeled                | Predict output | Predict house price |
| **Unsupervised**  | Unlabeled              | Find structure | Group customers     |
| **Reinforcement** | Environment + Feedback | Best action    | Self-driving car    |

---

## 5. Quick Visualization

* **Supervised** → “Teacher shows correct answers.”
* **Unsupervised** → “No teacher, group things yourself.”
* **Reinforcement** → “Learn by trial and error.”

---

## ✅ Mini Task for You (Day 1 Practice)

1. Make a list of **5 real-world examples** and classify them as supervised, unsupervised, or reinforcement.
   Example:

   * Predicting stock price → **Supervised**
   * Spotify song recommendations → **Unsupervised**
   * Playing chess → **Reinforcement**
   * Predicting car price → **Supervised**
   * Grouping news articles by topics → **Unsupervised**
   * Start driving a car → **Reinforcement**
   * human can learn by mistake -> **Reinforcement**


2. Install **scikit-learn**:

```bash
pip install scikit-learn
```

This will prepare you for Day 2 (NumPy, Pandas, etc).

---
'''