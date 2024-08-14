def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    ratio_items = [(name, item['calories'] / item['cost']) for name, item in items.items()]
    # Сортуємо страви за співвідношенням калорій до вартості (у порядку спадання)
    ratio_items.sort(key=lambda x: x[1], reverse=True)
    
    selected_items = []
    total_calories = 0
    remaining_budget = budget
    
    # Вибираємо страви, максимізуючи співвідношення калорій до вартості
    for name, _ in ratio_items:
        cost = items[name]['cost']
        calories = items[name]['calories']
        if remaining_budget >= cost:
            selected_items.append(name)
            total_calories += calories
            remaining_budget -= cost
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]
    
    for name, item in items.items():
        cost = item['cost']
        calories = item['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b] < dp[b - cost] + calories:
                dp[b] = dp[b - cost] + calories
                selected_items[b] = selected_items[b - cost] + [name]
    
    return selected_items[budget], dp[budget]

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Жадібний алгоритм
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: Вибрані страви: {selected_items_greedy}, Сумарна калорійність: {total_calories_greedy}")

# Алгоритм динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print(f"Алгоритм динамічного програмування: Вибрані страви: {selected_items_dp}, Сумарна калорійність: {total_calories_dp}")