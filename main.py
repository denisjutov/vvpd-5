import functions

def display_menu():
    """
    Отображает главное меню.
    """
    print("\nГлавное меню:")
    print("1. Вычислить экспоненту e^x")
    print("2. Вычислить гиперболический синус sh(x)")
    print("3. Вычислить гиперболический косинус ch(x)")
    print("4. Выйти")

def get_float_input(prompt):
    """
    Запрашивает у пользователя число с проверкой.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введите число.")

def get_positive_int_input(prompt):
    """
    Запрашивает у пользователя положительное целое число с проверкой.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: введите положительное целое число.")
        except ValueError:
            print("Ошибка: введите целое число.")

def main():
    """
    Главная функция для работы с меню.
    """
    while True:
        display_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            x = get_float_input("Введите значение x: ")
            n_terms = get_positive_int_input("Введите количество членов ряда: ")
            result = functions.exponential(x, n_terms)
            print(f"e^{x} = {result}")
        elif choice == "2":
            x = get_float_input("Введите значение x: ")
            n_terms = get_positive_int_input("Введите количество членов ряда: ")
            result = functions.hyperbolic_sine(x, n_terms)
            print(f"sh({x}) = {result}")
        elif choice == "3":
            x = get_float_input("Введите значение x: ")
            n_terms = get_positive_int_input("Введите количество членов ряда: ")
            result = functions.hyperbolic_cosine(x, n_terms)
            print(f"ch({x}) = {result}")
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
