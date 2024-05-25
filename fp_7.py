import random
import matplotlib.pyplot as plt


# Функція для кидка двох кубиків і повернення їхньої суми
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


# проведення симуляції методу Монте-Карло
def monte_carlo_simulation(num_simulations):
    sums = [0] * 11  # Список для підрахунку кількості випадків кожної суми (від 2 до 12)

    for _ in range(num_simulations):
        dice_sum = roll_dice()
        sums[dice_sum - 2] += 1

    probabilities = [count / num_simulations * 100 for count in sums]  # Розрахунок ймовірностей
    return probabilities


# побудова графіку ймовірностей сум
def plot_probabilities(probabilities):
    sums = list(range(2, 13))  # Можливі суми від 2 до 12
    plt.bar(sums, probabilities, color='skyblue', edgecolor='black')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.grid(True)
    plt.show()


# Кількість симуляцій
num_simulations = 100000


# Проведення симуляції
probabilities = monte_carlo_simulation(num_simulations)


# Виведення ймовірностей у табличному вигляді
print("Сума\tІмовірність (%)")
for i, prob in enumerate(probabilities, start=2):
    print(f"{i}\t{prob:.2f}%")


# Побудова графіку ймовірностей
plot_probabilities(probabilities)


# Аналітичні ймовірності
analytical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
print("\nАналітичні ймовірності:")
for i, prob in enumerate(analytical_probabilities, start=2):
    print(f"{i}\t{prob:.2f}%")
