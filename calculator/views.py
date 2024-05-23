# calculator/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'calculator/home.html')


def calculate(request):
    if request.method == 'POST':
        try:
            first_number = float(request.POST['first_number'])
            second_number = float(request.POST['second_number'])
            operation = request.POST['operation']
            result = None

            if operation == 'add':
                result = first_number + second_number
            elif operation == 'subtract':
                result = first_number - second_number
            elif operation == 'multiply':
                result = first_number * second_number
            elif operation == 'divide':
                result = first_number / second_number

            return render(request, 'calculator/home.html', {
                'result': result,
                'first_number': first_number,
                'second_number': second_number,
                'operation': operation
            })
        except (ValueError, ZeroDivisionError):
            return render(request, 'calculator/home.html', {
                'error': 'Некорректные данные. Пожалуйста, проверьте введенные значения и операцию.'
            })
    return render(request, 'calculator/home.html')
