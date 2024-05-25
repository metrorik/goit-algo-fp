items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Сортуємо елементи за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return chosen_items, total_cost, total_calories


def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю DP
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.items())

    # Заповнюємо таблицю DP
    for i in range(1, len(item_list) + 1):
        item, info = item_list[i - 1]
        for w in range(1, budget + 1):
            if info['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - info['cost']] + info['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлюємо вибір елементів
    total_calories = dp[len(item_list)][budget]
    w = budget
    chosen_items = []

    for i in range(len(item_list), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, info = item_list[i - 1]
            chosen_items.append(item)
            w -= info['cost']

    total_cost = sum(items[item]['cost'] for item in chosen_items)
    
    return chosen_items, total_cost, total_calories



# Приклад використання
budget = 100

# Жадібний алгоритм
greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_items)
print("Загальна вартість:", greedy_cost)
print("Загальна калорійність:", greedy_calories)

# Динамічне програмування
dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Обрані страви:", dp_items)
print("Загальна вартість:", dp_cost)
print("Загальна калорійність:", dp_calories)
