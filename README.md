"""
Практическая работа №10: Модуль для нахождения числа из последовательности Эйлера
"""

import math
from typing import List, Tuple, Optional, Generator
import numpy as np
import matplotlib.pyplot as plt
from sympy import primerange, isprime, factorint
from functools import lru_cache

class EulerSequence:
    """
    Класс для работы с последовательностью Эйлера
    Последовательность Эйлера: A000364 в OEIS
    """
    
    def __init__(self):
        self.cache = {}
        self.primes_cache = list(primerange(2, 10000))
        
    def euler_totient(self, n: int) -> int:
        """
        Вычисление функции Эйлера φ(n)
        φ(n) - количество натуральных чисел ≤ n, взаимно простых с n
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
            
        if n in self.cache:
            return self.cache[n]
            
        # Разложение на простые множители
        factors = factorint(n)
        result = n
        
        for p in factors:
            result = result // p * (p - 1)
            
        self.cache[n] = result
        return result
        
    def euler_sequence_recursive(self, n: int) -> int:
        """
        Рекурсивное вычисление чисел Эйлера
        E(n) = n! * Σ(1/k) для k от 1 до n
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
            
        factorial = math.factorial(n)
        harmonic_sum = sum(1.0 / k for k in range(1, n + 1))
        
        return int(round(factorial * harmonic_sum))
        
    def euler_sequence_iterative(self, n: int) -> int:
        """
        Итеративное вычисление чисел Эйлера
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
            
        factorial = 1
        harmonic_sum = 0.0
        
        for k in range(1, n + 1):
            factorial *= k
            harmonic_sum += 1.0 / k
            
        return int(round(factorial * harmonic_sum))
        
    def euler_sequence_optimized(self, n: int) -> int:
        """
        Оптимизированное вычисление чисел Эйлера с кэшированием
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
            
        # Используем рекуррентную формулу
        # E(n) = n * E(n-1) + (n-1)!
        if n not in self.cache:
            if n == 1:
                self.cache[1] = 1
            else:
                prev_euler = self.euler_sequence_optimized(n - 1)
                prev_factorial = math.factorial(n - 1)
                self.cache[n] = n * prev_euler + prev_factorial
                
        return self.cache[n]
        
    def generate_euler_sequence(self, limit: int) -> List[int]:
        """
        Генерация последовательности Эйлера до указанного предела
        """
        sequence = []
        for i in range(1, limit + 1):
            sequence.append(self.euler_sequence_optimized(i))
        return sequence
        
    def find_euler_number(self, target: int, max_search: int = 100) -> Optional[int]:
        """
        Поиск номера n для которого E(n) = target
        """
        for n in range(1, max_search + 1):
            if self.euler_sequence_optimized(n) == target:
                return n
        return None
        
    def find_euler_numbers_in_range(self, start: int, end: int) -> List[Tuple[int, int]]:
        """
        Поиск всех чисел Эйлера в указанном диапазоне
        Возвращает список кортежей (n, E(n))
        """
        results = []
        for n in range(1, end + 1):
            euler_num = self.euler_sequence_optimized(n)
            if start <= euler_num <= end:
                results.append((n, euler_num))
        return results
        
    def euler_totient_sequence(self, limit: int) -> List[int]:
        """
        Генерация последовательности значений функции Эйлера φ(n)
        """
        return [self.euler_totient(i) for i in range(1, limit + 1)]
        
    def find_perfect_numbers(self, limit: int) -> List[int]:
        """
        Поиск совершенных чисел с использованием функции Эйлера
        Число является совершенным, если φ(n) = n/2
        """
        perfect_numbers = []
        for n in range(2, limit + 1):
            if self.euler_totient(n) == n // 2:
                perfect_numbers.append(n)
        return perfect_numbers
        
    def analyze_euler_properties(self, n: int) -> dict:
        """
        Анализ свойств числа Эйлера E(n)
        """
        euler_num = self.euler_sequence_optimized(n)
        
        properties = {
            'n': n,
            'euler_number': euler_num,
            'is_prime': isprime(euler_num),
            'factors': factorint(euler_num),
            'divisors_count': len(self.get_divisors(euler_num)),
            'sum_of_divisors': sum(self.get_divisors(euler_num)),
            'is_perfect': sum(self.get_divisors(euler_num)) == 2 * euler_num,
            'phi_of_euler': self.euler_totient(euler_num),
            'digits': len(str(euler_num)),
            'digital_root': self.digital_root(euler_num)
        }
        
        return properties
        
    def get_divisors(self, n: int) -> List[int]:
        """
        Получение всех делителей числа n
        """
        divisors = set()
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return sorted(divisors)
        
    def digital_root(self, n: int) -> int:
        """
        Вычисление цифрового корня числа
        """
        if n == 0:
            return 0
        return 1 + (n - 1) % 9
        
    def plot_euler_sequence(self, limit: int = 20, save_path: Optional[str] = None):
        """
        Визуализация последовательности Эйлера
        """
        sequence = self.generate_euler_sequence(limit)
        n_values = list(range(1, limit + 1))
        
        plt.figure(figsize=(12, 8))
        
        # Основной график
        plt.subplot(2, 2, 1)
        plt.plot(n_values, sequence, 'b-o', linewidth=2, markersize=6)
        plt.title('Последовательность Эйлера')
        plt.xlabel('n')
        plt.ylabel('E(n)')
        plt.grid(True, alpha=0.3)
        
        # Логарифмический масштаб
        plt.subplot(2, 2, 2)
        plt.semilogy(n_values, sequence, 'r-o', linewidth=2, markersize=6)
        plt.title('Последовательность Эйлера (лог. масштаб)')
        plt.xlabel('n')
        plt.ylabel('E(n)')
        plt.grid(True, alpha=0.3)
        
        # Отношение к факториалу
        plt.subplot(2, 2, 3)
        ratios = [sequence[i-1] / math.factorial(i) for i in n_values]
        plt.plot(n_values, ratios, 'g-o', linewidth=2, markersize=6)
        plt.title('E(n) / n!')
        plt.xlabel('n')
        plt.ylabel('E(n) / n!')
        plt.grid(True, alpha=0.3)
        
        # Разности
        plt.subplot(2, 2, 4)
        differences = [sequence[i] - sequence[i-1] if i > 0 else sequence[0] for i in range(len(sequence))]
        plt.plot(n_values, differences, 'm-o', linewidth=2, markersize=6)
        plt.title('Разности E(n) - E(n-1)')
        plt.xlabel('n')
        plt.ylabel('Разность')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def plot_totient_comparison(self, limit: int = 100, save_path: Optional[str] = None):
        """
        Сравнение функции Эйлера и последовательности Эйлера
        """
        euler_seq = self.generate_euler_sequence(min(limit, 20))  # Ограничиваем из-за быстрого роста
        totient_seq = self.euler_totient_sequence(limit)
        
        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        n_euler = list(range(1, len(euler_seq) + 1))
        plt.plot(n_euler, euler_seq, 'b-o', label='E(n)', linewidth=2, markersize=6)
        plt.title('Последовательность Эйлера')
        plt.xlabel('n')
        plt.ylabel('E(n)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.subplot(1, 2, 2)
        n_totient = list(range(1, len(totient_seq) + 1))
        plt.plot(n_totient, totient_seq, 'r-o', label='φ(n)', linewidth=2, markersize=6)
        plt.title('Функция Эйлера')
        plt.xlabel('n')
        plt.ylabel('φ(n)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def find_euler_patterns(self, limit: int = 20) -> dict:
        """
        Поиск паттернов в последовательности Эйлера
        """
        sequence = self.generate_euler_sequence(limit)
        
        patterns = {
            'primes_in_sequence': [],
            'composite_numbers': [],
            'even_odd_ratio': 0,
            'growth_rate': [],
            'divisible_by_3': [],
            'digital_roots': {}
        }
        
        even_count = 0
        odd_count = 0
        
        for i, num in enumerate(sequence, 1):
            # Простые числа
            if isprime(num):
                patterns['primes_in_sequence'].append((i, num))
            else:
                patterns['composite_numbers'].append((i, num))
                
            # Четные/нечетные
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
            # Темп роста
            if i > 1:
                growth_rate = num / sequence[i-2]
                patterns['growth_rate'].append(growth_rate)
                
            # Делимость на 3
            if num % 3 == 0:
                patterns['divisible_by_3'].append((i, num))
                
            # Цифровые корни
            dr = self.digital_root(num)
            if dr not in patterns['digital_roots']:
                patterns['digital_roots'][dr] = []
            patterns['digital_roots'][dr].append((i, num))
                
        patterns['even_odd_ratio'] = even_count / (even_count + odd_count) if (even_count + odd_count) > 0 else 0
        
        return patterns
        
    def euler_number_statistics(self, limit: int = 20) -> dict:
        """
        Статистический анализ чисел Эйлера
        """
        sequence = self.generate_euler_sequence(limit)
        
        stats = {
            'count': len(sequence),
            'min': min(sequence),
            'max': max(sequence),
            'mean': np.mean(sequence),
            'median': np.median(sequence),
            'std': np.std(sequence),
            'sum': sum(sequence),
            'prime_count': sum(1 for num in sequence if isprime(num)),
            'composite_count': sum(1 for num in sequence if not isprime(num) and num > 1)
        }
        
        return stats

def demonstrate_euler_sequence():
    """
    Демонстрация работы с последовательностью Эйлера
    """
    print("🔢 Практическая работа №10: Последовательность Эйлера")
    print("=" * 50)
    
    # Создание экземпляра класса
    euler = EulerSequence()
    
    # Генерация последовательности
    print("\n📊 Первые 15 чисел Эйлера:")
    sequence = euler.generate_euler_sequence(15)
    for i, num in enumerate(sequence, 1):
        print(f"E({i}) = {num:,}")
        
    # Поиск конкретного числа
    target = 87
    position = euler.find_euler_number(target, max_search=20)
    print(f"\n🔍 Поиск числа {target}:")
    if position:
        print(f"E({position}) = {target}")
    else:
        print(f"Число {target} не найдено в первых 20 числах Эйлера")
        
    # Анализ свойств
    print(f"\n📈 Анализ E(10):")
    properties = euler.analyze_euler_properties(10)
    for key, value in properties.items():
        print(f"{key}: {value}")
        
    # Поиск в диапазоне
    print(f"\n🔎 Числа Эйлера в диапазоне [50, 500]:")
    range_results = euler.find_euler_numbers_in_range(50, 500)
    for n, euler_num in range_results:
        print(f"E({n}) = {euler_num}")
        
    # Совершенные числа
    print(f"\n💎 Совершенные числа до 1000:")
    perfect_numbers = euler.find_perfect_numbers(1000)
    print(perfect_numbers)
    
    # Паттерны
    print(f"\n🔍 Паттерны в последовательности Эйлера (первые 15 чисел):")
    patterns = euler.find_euler_patterns(15)
    print(f"Простые числа: {patterns['primes_in_sequence']}")
    print(f"Четные/нечетные соотношение: {patterns['even_odd_ratio']:.2f}")
    print(f"Делятся на 3: {patterns['divisible_by_3']}")
    
    # Статистика
    print(f"\n📊 Статистика первых 15 чисел Эйлера:")
    stats = euler.euler_number_statistics(15)
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")
            
    # Визуализация
    print(f"\n📈 Построение графиков...")
    euler.plot_euler_sequence(15)
    euler.plot_totient_comparison(50)
    
    return euler

def interactive_euler_calculator():
    """
    Интерактивный калькулятор чисел Эйлера
    """
    euler = EulerSequence()
    
    print("\n🔢 Интерактивный калькулятор чисел Эйлера")
    print("=" * 40)
    
    while True:
        print("\nВыберите действие:")
        print("1. Вычислить E(n)")
        print("2. Найти позицию числа")
        print("3. Поиск в диапазоне")
        print("4. Анализ свойств")
        print("5. Визуализация")
        print("6. Выход")
        
        choice = input("\nВаш выбор (1-6): ").strip()
        
        if choice == '1':
            try:
                n = int(input("Введите n: "))
                result = euler.euler_sequence_optimized(n)
                print(f"E({n}) = {result:,}")
            except ValueError:
                print("Ошибка: введите целое число")
                
        elif choice == '2':
            try:
                target = int(input("Введите число для поиска: "))
                max_search = int(input("Максимальная позиция поиска (по умолчанию 100): ") or "100")
                position = euler.find_euler_number(target, max_search)
                if position:
                    print(f"E({position}) = {target}")
                else:
                    print(f"Число {target} не найдено в первых {max_search} числах Эйлера")
            except ValueError:
                print("Ошибка: введите целое число")
                
        elif choice == '3':
            try:
                start = int(input("Начало диапазона: "))
                end = int(input("Конец диапазона: "))
                results = euler.find_euler_numbers_in_range(start, end)
                if results:
                    print(f"Найдено {len(results)} чисел Эйлера:")
                    for n, euler_num in results:
                        print(f"E({n}) = {euler_num}")
                else:
                    print(f"Числа Эйлера в диапазоне [{start}, {end}] не найдены")
            except ValueError:
                print("Ошибка: введите целые числа")
                
        elif choice == '4':
            try:
                n = int(input("Введите n для анализа: "))
                properties = euler.analyze_euler_properties(n)
                print(f"\nАнализ E({n}):")
                for key, value in properties.items():
                    print(f"{key}: {value}")
            except ValueError:
                print("Ошибка: введите целое число")
                
        elif choice == '5':
            try:
                limit = int(input("Лимит для визуализации (по умолчанию 20): ") or "20")
                euler.plot_euler_sequence(limit)
                euler.plot_totient_comparison(min(limit * 5, 100))
            except ValueError:
                print("Ошибка: введите целое число")
                
        elif choice == '6':
            print("Выход из калькулятора")
            break
            
        else:
            print("Неверный выбор. Попробуйте снова.")

if__name__ == "__main__":
    # Демонстрация
    euler = demonstrate_euler_sequence()
    
    # Интерактивный режим
    interactive_euler_calculator()
