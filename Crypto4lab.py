import random, math, itertools

# Реалізація монобітного тесту
def monobit_test(sequence):
    ones_count = sequence.count('1')     # Підраховує кількість одиниць у строці
    result = 9654 < ones_count < 10346     # Результат згідно тесту монобіта повинен варіювати між значеннями    
    return result                        # повертає результат

# Реалізація тесту покера
def poker_test(sequence):
    subsequence_length = 4        # Задається довжина біта
    subsequence_count = len(sequence) // subsequence_length     # Вираховується коєфіціент
    subsequence_frequencies = {}                                 # Зберігає частоти різних підпослідовностей

    for i in range(subsequence_count):        # Відповідно до формул тесту Покера вираховується коеєфіціент кожного бінарного значення по бітам та вноситься в список
        subsequence = sequence[i * subsequence_length: (i + 1) * subsequence_length]
        subsequence_frequencies[subsequence] = subsequence_frequencies.get(subsequence, 0) + 1
        
# Вираховується середне значення коєфіціенту і порівнюється відповідно до значень тесту покеру
    sum_squared_frequencies = sum(freq ** 2 for freq in subsequence_frequencies.values())
    poker_chi_square = (16 / 5000) * sum_squared_frequencies - 5000
    result = 1.03 < poker_chi_square < 57.4
    return result

def runs_test(sequence):     # Записуєм наше бінарне значення в список по символьно 
    runs = [list(g) for k, g in itertools.groupby(sequence)] 
    run_count = len(runs)        # Розраховуєм довжину списку
    pi = 2.0 / 3.0                # Задаєм вірогідність повторюванності одиниці
    tau = 5.0 / 6.0                # Задаєм критичне значення повторюваності одиниць
    vobs = sum(len(run) for run in runs)     # Вираховується кількість одиниць і порівнюється з значення tau
    vexp = 2.0 * len(sequence) / run_count
    runs_test_statistic = abs(vobs - vexp) / math.sqrt(2.0 * len(sequence) * (2.0 * len(sequence) - 1.0) / run_count)
    result = runs_test_statistic <= tau
    return result

def long_run_test(sequence):    # Вираховується кількість нулів або одиниць які йдуть підряд, за цим тестом кількість не повинна перевищувати 42
    max_run_length = max(len(list(g)) for k, g in itertools.groupby(sequence))
    result = max_run_length <= 42
    return result

# Функція запуску тестів та запису результату змін
def fips_140_test(sequence):
    monobit_result = monobit_test(sequence)
    poker_result = poker_test(sequence)
    runs_result = runs_test(sequence)
    long_run_result = long_run_test(sequence)

    if monobit_result and poker_result and runs_result and long_run_result:
        print("Всі тести пройдено!")
        return True
    else:
        num = 0
        arr=[]
        if not monobit_result:
            num+=1
            arr.append("monobit_result_test")
        if not poker_result:
            num+=1
            arr.append("poker_result_test")
        if not runs_result:
            num+=1
            arr.append("runs_result_test")
        if not long_run_result:
            num+=1
            arr.append("long_run_result_test")
        print(f"Не продено тестів:{num}\n Не продено такий тест:{arr}") 
        return False

# Функція прийому та передачі даних між користувачем та алгоритмами тестів
def random_test(): 
        binarian = input("байтова строка:")
        result = fips_140_test(binarian)
        if result:
            print("Послідовність проходить тест FIPS-140-3: вона є достатньою випадковою.")
        else:
            print("Послідовність не проходить тест FIPS-140-3: вона не є достатньою випадковою.")

# Виклик функції для тестування
random_test()
