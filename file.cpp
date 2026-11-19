#include <iostream>
#include <vector>
#include <windows.h> // Для русского языка в консоли

using namespace std;

int main() {
    SetConsoleOutputCP(CP_UTF8);
    
    int n; // Количество чисел
    cout << "Введите количество чисел: ";
    
    // Защита от ввода букв и неправильного количества
    while (!(cin >> n) || n <= 0) {
        cout << "Ошибка! Введите корректные данные: ";
        cin.clear();
        cin.ignore(10000, '\n');
    }

    // Создаем массив нужного размера
    vector<long long> nums(n);
    cout << "Введите " << n << " чисел через пробел: ";
    
    // Вводим числа по одному в цикле
    for (int i = 0; i < n; i++) {
        while (!(cin >> nums[i])) {
            cout << "Ошибка! Введите число: ";
            cin.clear();
            cin.ignore(10000, '\n');
        }
    }

    // Ввод искомой суммы
    long long target;
    cout << "Искомая сумма: ";
    while (!(cin >> target)) {
        cout << "Ошибка! Введите число: ";
        cin.clear();
        cin.ignore(10000, '\n');
    }

    // Поиск пар 
    bool found = false;
    cout << "\nНайденные пары:\n";

    // Идем по всем числам, кроме последнего
    for (int i = 0; i < n - 1; i++) {
        // Для каждого i-го числа смотрим на числа после него
        for (int j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] == target) {
                cout << "  (" << nums[i] << ", " << nums[j] << ")\n";
                found = true;
            }
        }
    }

    // Если пары не нашлись
    if (!found) {
        cout << "Пар с такой суммой не найдено.\n";
    }
}