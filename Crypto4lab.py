import random, math, itertools

# 1. Реалізація монобітного тесту 
def test1_monobita(sequence):
    ones_count = sequence.count('1')     # Підраховує кількість одиниць у строці
    result = 9654 < ones_count < 10346     # Результат згідно тесту монобіта повинен варіювати між значеннями    
    return result                        # повертає результат
    
# 2. Реалізація тесту Максимальної довжини серії
def test2_max_lengh(sequence):     # Записуєм наше бінарне значення в список по символьно 
    runs = [list(g) for k, g in itertools.groupby(sequence)] 
    run_count = len(runs)        # Розраховуєм довжину списку
    prob = 2.0 / 3.0                # Задаєм вірогідність повторюванності одиниці
    critical_value = 5.0 / 6.0                # Задаєм критичне значення повторюваності одиниць
    value_compare = sum(len(run) for run in runs)     # Вираховується кількість одиниць і порівнюється з значення critical_value
    value_prob = 2.0 * len(sequence) / run_count
    runs_test_statistic = abs(value_compare - value_prob) / math.sqrt(2.0 * len(sequence) * (2.0 * len(sequence) - 1.0) / run_count)
    result = runs_test_statistic <= critical_value
    return result
    
# 3. Реалізація тесту покера
def test3_pokera(sequence):
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

# 4. Реалізація тесту Довжин серій
def test4_lengh(sequence):    # Вираховується кількість нулів або одиниць які йдуть підряд, за цим тестом кількість не повинна перевищувати 42
    max_run_length = max(len(list(g)) for k, g in itertools.groupby(sequence))
    result = max_run_length <= 42
    return result

# Функція запуску тестів та запису результату змін
def fips_140_test(sequence):
    monobit_result = test1_monobita(sequence)
    max_lengh_result = test2_max_lengh(sequence) 
    poker_result = test3_pokera(sequence)
    lengh_result = test4_lengh(sequence)

    if monobit_result and  max_lengh_result and poker_result and lengh_result:
        print("Всі тести пройдено!")
        return True
    else:
        num = 0
        arr=[]
        if not monobit_result:
            num+=1
            arr.append("monobit_result_test")
        if not max_lengh_result:
            num+=1
            arr.append("max_lengh_result_test")
        if not poker_result:
            num+=1
            arr.append("poker_result_test")
        if not lengh_result:
            num+=1
            arr.append("lengh_result_test")
        print(f"Не пройдено тестів:{num}\n Не пройдено такий тест:{arr}") 
        return False

# Функція прийому та передачі даних між користувачем та алгоритмами тестів
def random_test(): 
        binarian = input("Ввод бінарного значення:")
        result = fips_140_test(binarian)
        if result:
            print("Послідовність проходить тест FIPS-140-3: вона є достатньою випадковою.")
        else:
            print("Послідовність не проходить тест FIPS-140-3: вона не є достатньою випадковою.")

# Виклик функції для тестування
random_test()
