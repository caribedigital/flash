from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})



def suma(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']

        if not answer: #si no hay respuesta en el input y se hace push en el boton, carga de nuevo la pagina con nuevos valores
            my_answer = "hey Olvidaste introducir una respuesta!!"
            color = 'warning'
            return render(request, 'division.html', {
            'color':color,
            'my_answer':my_answer,    
            'answer':answer,
            'num_1':num_1,
            'num_2':num_2,
            })
            
        #ejecutor de suma y comparador
        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Respuesta Correcta!! " + old_num1 + " + " + old_num2 + " = " + answer
            color = "success"
        else:
            my_answer = "Respuesta Incorrecta!! " + old_num1 + " + " + old_num2 + " no es " + answer + " es " + str(correct_answer)
            color = "danger"

        return render(request, 'suma.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color, 
            })

    return render(request, 'suma.html', {
        'num_1':num_1,
        'num_2':num_2,
        })

        

def resta(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']

        if not answer: #si no hay respuesta en el input y se hace push en el boton, carga de nuevo la pagina con nuevos valores
            my_answer = "hey Olvidaste introducir una respuesta!!"
            color = 'warning'
            return render(request, 'division.html', {
            'color':color,
            'my_answer':my_answer,    
            'answer':answer,
            'num_1':num_1,
            'num_2':num_2,
            })

        #ejecutor de suma y comparador
        correct_answer = int(old_num1) - int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Respuesta Correcta!! " + old_num1 + " - " + old_num2 + " = " + answer
            color = "success"
        else:
            my_answer = "Respuesta Incorrecta!! " + old_num1 + " - " + old_num2 + " no es " + answer + " es " + str(correct_answer)
            color = "danger"

        return render(request, 'resta.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color, 
            })

    return render(request, 'resta.html', {
        'num_1':num_1,
        'num_2':num_2,
        })



def multiplicacion(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']

        if not answer: #si no hay respuesta en el input y se hace push en el boton, carga de nuevo la pagina con nuevos valores
            my_answer = "hey Olvidaste introducir una respuesta!!"
            color = 'warning'
            return render(request, 'division.html', {
            'color':color,
            'my_answer':my_answer,    
            'answer':answer,
            'num_1':num_1,
            'num_2':num_2,
            })


        #ejecutor de multiplicacion y comparador
        correct_answer = int(old_num1) * int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Respuesta Correcta!! " + old_num1 + " x " + old_num2 + " = " + answer
            color = "success"
        else:
            my_answer = "Respuesta Incorrecta!! " + old_num1 + " x " + old_num2 + " no es " + answer + " es " + str(correct_answer)
            color = "danger"

        return render(request, 'multiplicacion.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color, 
            })

    return render(request, 'multiplicacion.html', {
        'num_1':num_1,
        'num_2':num_2,
        })



def division(request):
    from random import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']

        if not answer: #si no hay respuesta en el input y se hace push en el boton, carga de nuevo la pagina con nuevos valores
            my_answer = "hey Olvidaste introducir una respuesta!!"
            color = 'warning'
            return render(request, 'division.html', {
            'color':color,
            'my_answer':my_answer,    
            'answer':answer,
            'num_1':num_1,
            'num_2':num_2,
            })

        #ejecutor de division y comparador
        correct_answer = int(old_num1) / int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Respuesta Correcta!! " + old_num1 + " / " + old_num2 + " = " + answer
            color = "success"
        else:
            my_answer = "Respuesta Incorrecta!! " + old_num1 + " / " + old_num2 + " no es " + answer + " es " + str(correct_answer)
            color = "danger"

        return render(request, 'division.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color':color, 
            })

    return render(request, 'division.html', {
        'num_1':num_1,
        'num_2':num_2,
        })