import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagorean_tree(t, length, level):
    if level == 0:
        return
    
    # Малюємо горизонтальну лінію (гілку)
    t.forward(length)
    
    # Повертаємо вправо на 45 градусів для лівого дочірнього дерева
    t.right(45)
    draw_pythagorean_tree(t, length / math.sqrt(2), level - 1)
    
    # Повертаємо на 90 градусів для правого дочірнього дерева
    t.left(90)
    draw_pythagorean_tree(t, length / math.sqrt(2), level - 1)
    
    # Повертаємо на 45 градусів, щоб відновити напрямок
    t.right(45)
    t.backward(length)

def main():
    # Налаштування вікна turtle
    screen = turtle.Screen()
    screen.title("Фрактал Дерево Піфагора")
    screen.bgcolor("white")
    
    # Налаштування черепахи
    t = turtle.Turtle()
    t.speed(0)  # Найшвидший малюнок
    
    # Отримання рівня рекурсії від користувача
    level = int(screen.textinput("Введіть рівень", "Введіть рівень рекурсії (наприклад, 4):"))

    # Переміщення черепахи на початкову позицію
    t.penup()
    t.goto(0, -200)  # Розміщення черепахи внизу екрана
    t.pendown()
    t.left(90)  # Початкова орієнтація черепахи

    # Малювання дерева Піфагора
    draw_pythagorean_tree(t, 200, level)

    # Завершення роботи
    screen.mainloop()

if __name__ == "__main__":
    main()
