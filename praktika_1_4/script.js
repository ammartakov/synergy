// Получаем ссылки на DOM-элементы
const inputA = document.getElementById('inputA');
const inputB = document.getElementById('inputB');
const resultDisplay = document.getElementById('resultDisplay');

// ----- 4 чистые функции для математических операций -----
function sum(a, b) {
    return a + b;
}

function difference(a, b) {
    return a - b;
}

function product(a, b) {
    return a * b;
}

function division(a, b) {
    if (b === 0) {
        throw new Error('Деление на ноль невозможно');
    }
    return a / b;
}

/**
 * Основная функция-обработчик для любой математической операции.
 * Парсит значения из инпутов, проверяет валидность чисел,
 * вызывает соответствующую операцию и обновляет окно результата.
 * @param {Function} operation - функция (a, b) => number | может выбросить ошибку
 */
function computeAndDisplay(operation) {
    // Получаем сырые строки из полей ввода и удаляем лишние пробелы
    const rawValueA = inputA.value.trim();
    const rawValueB = inputB.value.trim();

    // Проверка на пустые поля
    if (rawValueA === '' || rawValueB === '') {
        resultDisplay.textContent = '❌ Ошибка: оба поля должны быть заполнены';
        resultDisplay.classList.add('error-message');
        return;
    }

    // Строгая проверка на валидность чисел
    const isValidNumber = (str) => {
        if (str === '') return false;
        // Проверяем наличие недопустимых символов
        if (/[^0-9.-]/.test(str)) return false;
        // Запрещаем несколько точек
        if ((str.match(/\./g) || []).length > 1) return false;
        // Запрещаем несколько минусов
        if ((str.match(/-/g) || []).length > 1) return false;
        // Минус только в начале
        if (str.includes('-') && str.indexOf('-') !== 0) return false;
        // Проверяем, что после всех проверок получается валидное число
        const num = Number(str);
        return !isNaN(num);
    };

    if (!isValidNumber(rawValueA) || !isValidNumber(rawValueB)) {
        resultDisplay.textContent = '⚠️ Ошибка: введите корректные числа (цифры, допускается минус и точка)';
        resultDisplay.classList.add('error-message');
        return;
    }

    // Парсим числа с плавающей точкой
    const numA = parseFloat(rawValueA);
    const numB = parseFloat(rawValueB);

    if (isNaN(numA) || isNaN(numB)) {
        resultDisplay.textContent = '❌ Ошибка: введите числа в оба поля';
        resultDisplay.classList.add('error-message');
        return;
    }

    try {
        // Выполняем переданную операцию
        let result = operation(numA, numB);
        
        // Обработка особых случаев: для деления результат может быть дробным
        if (typeof result === 'number' && !Number.isInteger(result)) {
            // Ограничиваем до 8 знаков после запятой для читаемости
            result = parseFloat(result.toFixed(8));
        }
        
        // Избегаем -0
        if (Object.is(result, -0)) result = 0;
        
        resultDisplay.textContent = String(result);
        resultDisplay.classList.remove('error-message');
    } catch (error) {
        // Перехватываем ошибки (например, деление на ноль)
        resultDisplay.textContent = `⚠️ Ошибка: ${error.message}`;
        resultDisplay.classList.add('error-message');
    }
}

// ----- Привязываем обработчики событий к каждой кнопке -----
document.getElementById('btnSum').addEventListener('click', () => {
    computeAndDisplay(sum);
});

document.getElementById('btnDiff').addEventListener('click', () => {
    computeAndDisplay(difference);
});

document.getElementById('btnProd').addEventListener('click', () => {
    computeAndDisplay(product);
});

document.getElementById('btnDiv').addEventListener('click', () => {
    computeAndDisplay(division);
});

// Дополнительная функция: запоминаем последнюю операцию для удобства
let lastOperation = sum;

// Обновляем lastOperation при каждом нажатии
const updateLastOperation = (operation) => {
    lastOperation = operation;
};

// Переопределяем обработчики с сохранением последней операции
document.getElementById('btnSum').onclick = () => {
    computeAndDisplay(sum);
    lastOperation = sum;
};
document.getElementById('btnDiff').onclick = () => {
    computeAndDisplay(difference);
    lastOperation = difference;
};
document.getElementById('btnProd').onclick = () => {
    computeAndDisplay(product);
    lastOperation = product;
};
document.getElementById('btnDiv').onclick = () => {
    computeAndDisplay(division);
    lastOperation = division;
};

// Добавляем возможность повторить последнее действие по Enter
const handleEnterPress = (e) => {
    if (e.key === 'Enter') {
        if (lastOperation) {
            computeAndDisplay(lastOperation);
        } else {
            computeAndDisplay(sum);
        }
    }
};

inputA.addEventListener('keypress', handleEnterPress);
inputB.addEventListener('keypress', handleEnterPress);

// Инициализация: при загрузке страницы показываем сумму начальных значений
window.addEventListener('DOMContentLoaded', () => {
    computeAndDisplay(sum);
    lastOperation = sum;
});