import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def draw_plot(func, x_min, x_max):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = func(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(x_min, x_max)
    iy = func(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(x_min) + ' до ' + str(x_max))
    plt.grid()
    plt.show()


def monte_carlo_integrate(func, x_min, x_max, num_points ):
    max_y = func(x_max)
    x_random = np.random.uniform(x_min, x_max, num_points)
    y_random = np.random.uniform(0, max_y, num_points)

    hits = np.sum(y_random <= func(x_random))

    integral_approx = (x_max - x_min) * max_y * (hits / num_points)

    return integral_approx


#draw_plot(f, a, b)

result_mc = monte_carlo_integrate(f, a, b, 100000)
print("Integral Monte Carlo(100000): ", result_mc)
result_mc = monte_carlo_integrate(f, a, b, 1000)
print("Integral Monte Carlo(1000): ", result_mc)
result_mc = monte_carlo_integrate(f, a, b, 100)
print("Integral Monte Carlo(100): ", result_mc)


result_scipy, _ = spi.quad(f, a, b)
print("Інтеграл: ", result_scipy)