import random
import matplotlib.pyplot as plt

# Кількість кидків кубиків
num_simulations = 1000000

# Масив для зберігання кількості кожної суми
sum_counts = [0] * 13

# Симуляція кидків кубиків
for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    sum_counts[total] += 1

# Обчислення ймовірностей
probabilities = [count / num_simulations for count in sum_counts[2:]]

# Аналітичні ймовірності (з таблиці)
analytical_probabilities = [
    2.78 / 100, 5.56 / 100, 8.33 / 100, 11.11 / 100, 13.89 / 100,
    16.67 / 100, 13.89 / 100, 11.11 / 100, 8.33 / 100, 5.56 / 100, 2.78 / 100
]

# Виведення результатів
print("Ймовірності кожної суми (від 2 до 12):")
for i, prob in enumerate(probabilities, start=2):
    print(f"Сума {i}: {prob:.6f}")

print("Сума  Монте-Карло  Аналітичні  Відхилення")
print("-----------------------------------------")
for i, (mc_prob, an_prob) in enumerate(zip(probabilities, analytical_probabilities), start=2):
    deviation = abs(mc_prob - an_prob)
    print(f"{i:2d}  {mc_prob*100:10.4f}%  {an_prob*100:10.4f}%  {deviation*100:10.4f}%")

# Візуалізація результатів
plt.bar(range(2, 13), probabilities)
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум двох кубиків (метод Монте-Карло)')
plt.xticks(range(2, 13))
plt.show()