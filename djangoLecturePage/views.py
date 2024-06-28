from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

redirect_page = 'main'


class LecturePageView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'user': request.user,
        }
        return render(request=request, template_name="lecture/lecture.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_page)

        return render(request=request, template_name="lecture/lecture.html",
                      context={"error": "Пайдаланушы атыңыз және/немесе құпия сөзіңіз дұрыс емес.",
                               'user': request.user})


class PrintInputView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture1-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput1TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput2TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput3TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput4TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput5TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput6TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-6.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput7TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class PrintInput8TaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task1/task1-8.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElseView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture2-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-2.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-3.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-4.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-5.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-6.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-7.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse8View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-8.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse9View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-9.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse10View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-10.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse11View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-11.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse12View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-12.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class IfElse13View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task2/task2-13.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class CalculationsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture3-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-1.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-2.html')
    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations8View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-8.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations9View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-9.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations10View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-10.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations11View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-11.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations12View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-12.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations13View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-13.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations14View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-14.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations15View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-15.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Calculations16View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task3/task3-16.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoopView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture4-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop8View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-8.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop9View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-9.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop10View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-10.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ForLoop11View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task4/task4-11.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class StrView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture5-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str8View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-8.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str9View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-9.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str10View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-10.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str11View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-11.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Str12View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task5/task5-12.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoopView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture6-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop8View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-8.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop9View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-9.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop10View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-10.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop11View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-11.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop12View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-12.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop13View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-13.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop14View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-14.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop15View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-15.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop16View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-16.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class WhileLoop17View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task6/task6-17.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture7-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class List1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request,'task/task7/task7-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class List2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task7/task7-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class List3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task7/task7-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class List4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task7/task7-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class List5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task7/task7-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class List6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task7/task7-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class List7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task7/task7-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class FunctionView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture8-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Function1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task8/task8-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Function2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task8/task8-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Function3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task8/task8-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Function4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task8/task8-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Function5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task8/task8-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Function6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task8/task8-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Function7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task8/task8-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class ArrayView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture9-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Array1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task9/task9-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Array2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task9/task9-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Array3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task9/task9-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Array4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task9/task9-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Array5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task9/task9-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Array6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task9/task9-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class SetsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture10-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets8View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-8.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets9View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-9.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Sets10View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task10/task10-10.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class DictionaryView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'lecture/lecture11-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary1View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-1.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary2View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-2.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary3View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-3.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary4View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-4.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary5View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-5.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary6View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-6.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary7View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-7.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary8View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-8.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary9View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-9.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary10View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-10.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary11View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-11.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary12View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-12.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)


class Dictionary13View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'task/task11/task11-13.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(redirect_page)
