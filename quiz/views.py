import random
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Question,UserSession

#  To Start a new session

def start_quiz(request):
    session = UserSession.objects.create()
    request.session['session_id'] = session.id
    first_question = random.choice(Question.objects.all())
    return redirect('get_question')

# To fetch a random Question

def get_question(request):
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('start_quiz')
    
    question = random.choice(Question.objects.all())
    return render(request,'quiz/question.html',{'question':question})

# To submit an answer

def submit_answer(request,question_id):
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('start_quiz')
    
    session = UserSession.objects.get(id=session_id)
    question = Question.objects.get(id=question_id)
    selected_answer = request.POST.get('answer')

    session.total_questions += 1
    if selected_answer == question.correct_answer:
        session.correct_answers += 1
    else:
        session.incorrect_answers += 1
    session.save()

    return redirect('get_results')

# To get the results

def get_results(request):
    session_id = request.session.get('session_id')
    if not session_id:
        return redirect('start_quiz')

    session = UserSession.objects.get(id=session_id)
    return render(request,'quiz/results.html', {'session': session})

    

