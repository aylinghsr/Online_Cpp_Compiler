from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import todo
from backend import compile_source

def createtodo(request):
    print(request.method)
    if request.method == "GET":
        return render(request, 'todo/createtodo.html', {'form':TodoForm()})
    elif request.method == "POST":
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        
        output , error = compile_source(newtodo.title)

        print("#########################")
        print('1', output)
        print('2', error)

        color = "white"
        if error:
            output = error
            color = "danger"

        context = {
            "code": newtodo.title,
            "output": output,
            'form': TodoForm(),
            "color": color
        }

        return render(request, 'todo/createtodo.html', context)