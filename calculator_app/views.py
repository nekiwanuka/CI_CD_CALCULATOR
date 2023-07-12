
from django.shortcuts import render, redirect
from .models import Calculation

def calculator(request):
    calculation_history = Calculation.objects.order_by('-id')[:5]

    if request.method == 'POST':
        num1 = int(request.POST.get('num1', '0'))
        num2 = int(request.POST.get('num2', '0'))
        operator = request.POST.get('operator')

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero"
        else:
            result = "Invalid operator"

        # Save current calculation to the database
        calculation = Calculation(expression=f"{num1} {operator} {num2}", result=result)
        calculation.save()

        return redirect('calculator')

    return render(request, 'calculator.html', {'history': calculation_history})
