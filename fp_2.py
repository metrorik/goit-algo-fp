import turtle
import math


# Функція для відновлення позиції та напрямку
def restore_position(t, pos, heading):
    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()

# Функція для малювання дерева Піфагора
def draw_tree(t, branch_length, level):
    if level == 0:
        return

    # Малювання основної гілки
    t.forward(branch_length)
    
    # Збереження поточної позиції та напрямку
    current_pos = t.pos()
    current_heading = t.heading()
    
    # Розрахунок довжини нових гілок
    branch_length = branch_length * math.sqrt(2) / 2

    # Малювання правої гілки
    t.right(45)
    draw_tree(t, branch_length, level - 1)

    # Відновлення позиції та напрямку
    restore_position(t, current_pos, current_heading)

    # Малювання лівої гілки
    t.left(45)
    draw_tree(t, branch_length, level - 1)

    # Відновлення позиції та напрямку
    restore_position(t, current_pos, current_heading)


def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.setpos(0, -250)
    t.pendown()
    t.color("brown")

    # Визначення рівня рекурсії
    level = int(screen.numinput("Рівень рекурсії", "Введіть рівень рекурсії:", 8, minval=1, maxval=15))

    # Малювання дерева
    draw_tree(t, 100, level)

    turtle.done()

if __name__ == "__main__":
    main()
