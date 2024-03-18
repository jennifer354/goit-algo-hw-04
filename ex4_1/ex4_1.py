from pathlib import Path

folder = Path('./ex4_1')

def total_salary(file_path):
    total = 0
    count = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0
        return total, average

    except OSError as err:
        print('Помилка доступу до файлу:', err)
    
    finally:
        file.close()

file_path = r"C:\MyREPO\goit-algo-hw-04\ex4_1\ex4_1.txt"
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
