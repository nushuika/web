import subprocess
import pytest

INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird'),
        ('120', 'Число должно быть в диапазоне от 1 до 100!')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['1000000000000','2'],['Числа должны быть в диапазоне от 1 до 10^10!'])
    ],
    'division': [
        (['10','5'],['2','2.0']),
        (['3','5'],['0','0.6']),
        (['0','2'],['0','0.0']),
        (['5','0'],['Деление на ноль невозможно'])
    ],
    'loops': [
        (['3'],['0','1','4']),
        (['5'],['0','1','4','9','16']),
        (['25'], ['Число должно быть в диапазоне от 1 до 20!']),
        (['1'],['0'])
    ],
    'print_function':[
        (['5'],['12345']),
        (['0'], ['Число должно быть в диапазоне от 1 до 20!']),
        (['25'], ['Число должно быть в диапазоне от 1 до 20!'])
    ],
    'second_score': [
        (['5','2 3 6 6 5'],['5']),
        (['2','7 3'],['3']),
        (['1','6'],['Количество участников должно быть больше одного!'])
    ],
    'nested_list': [
        (['5','Гарри','37.21','Берри','37.21','Тина','37.2','Акрити','41','Харш','39'],['Берри','Гарри']),
        (['6'],['Количество учащихся должно быть от 2 до 5.']),
        (['2','Гарри','3.4','Берри','3.4'],['Во вводимых данных всегда должен присутствовать хотя бы один учащийся со второй по величине оценкой.'])
    ],
    'lists': [
        (['12','insert 0 5','insert 1 10','insert 0 6','print','remove 6','append 9','append 1','sort','print','pop','reverse','print'],
         ['[6, 5, 10]','[1, 5, 9, 10]','[9, 5, 1]']),
        (['4','insert 0 9','print','remove 9','pop'],['[9]','Ошибка: нельзя выполнить pop на пустом списке']),
        (['2','insert 0 11','remove 9'],['Ошибка: элемент 9 отсутствует в списке']),
    ],
    'swap_case':[
        (['Www.MosPolytech.ru'],['wWW.mOSpOLYTECH.RU']),
        (['Pythonist 2'],['pYTHONIST 2']),
        (['ПривеТ, мИр'],['пРИВЕт, МиР'])
    ],
    'split_and_join':[
        (['this is a string'],['this-is-a-string']),
        (['100 programs in python'],['100-programs-in-python']),
        (['питон - это язык программирования'],['питон---это-язык-программирования'])
    ],
    'max_word':[
        (['example.txt'],['сосредоточенности']),
        (['example2.txt'],['привет','прощай','гудбай']),
        (['example3.txt'],['Файл пуст!'])
    ],
    'anagram':[
        (['listen','silent'],['YES']),
        (['vacationtime','iamnotactive'],['YES']),
        (['vacation time','i am not active'],['В строках не должно быть пробелов!'])
    ],
    'metro':[
        (['2','5 25','10 20','20'],['2']),
        (['2','10 15','25 30','20'],['0']),
        (['3','10 20','20 30','30 45','20'],['2'])
    ],
    'minion_game':[
        (['BANANA'],['Стюарт 12']),
        (['ORANGE'],['Кевин 11']),
        (['APPLE'*10**6],['Ошибка: длина строки должна быть от 1 до 10^6 символов.'])
    ],
    'is_leap':[
        (['2004'],['True']),
        (['2015'],['False']),
        (['1800'],['Ошибка: год должен быть в диапазоне от 1900 до 10^5.'])
    ],
    'happiness':[
        (['3 2','1 5 3','3 1','5 7'],['1']),
        (['10000000 6'],['Ошибка: n и m должны быть в диапазоне от 1 до 10^5.']),
        (['3 4','10000000000'],['Ошибка: элементы массива должны быть в диапазоне от 1 до 10^9.'])
    ],
    'pirate_ship':[
        (['50 3','золото 30 100','серебро 15 120','брюлики 10 250'],['брюлики 10.00 250.00','серебро 15.00 120.00','золото 25.00 83.33']),
        (['20 2','золото 15 50','кристаллы 1 500'],['кристаллы 1.00 500.00','золото 15.00 50.00'])
    ],
    'matrix_mult':[
        (['2','1 2','3 4','1 2','3 4'],['7 10','15 22']),
        (['0'],['Ошибка: размерность матрицы должна быть в диапазоне от 2 до 10.']),
        (['2','1 2 3'],['Ошибка: строка матрицы должна содержать ровно 2 чисел.'])
    ]
}

def test_hello_world():
    assert run_script('hello.py') == 'Hello, world!'

def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.90'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['max_word'])
def test_max_word(input_data, expected):
    assert run_script('max_word.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected