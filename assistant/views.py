
# import base64
# import os
# from google import genai
# from google.genai import types
# from django.shortcuts import render
# from .forms import InterviewForm
# from .models import InterviewFeedback
# import google.generativeai as genai

# # Configure Gemini
# genai.configure(api_key="")  # Replace with your actual key

# def interview_view(request):
#     feedback = None

#     if request.method == 'POST':
#         form = InterviewForm(request.POST)
#         if form.is_valid():
#             question = form.cleaned_data['question']
#             answer = form.cleaned_data['answer']

#             prompt = f"You are an expert interview coach. Here's the candidate's response.\nQuestion: {question}\nAnswer: {answer}\nGive constructive feedback."

#             model = genai.GenerativeModel('gemini-2.5-pro')
#             response = model.generate_content(prompt)
#             feedback_text = response.text

#             feedback_instance = form.save(commit=False)
#             feedback_instance.feedback = feedback_text
#             feedback_instance.save()

#             feedback = feedback_text
#     else:
#         form = InterviewForm()

#     return render(request, 'assistant/index.html', {'form': form, 'feedback': feedback})
from django.shortcuts import render
from django.http import JsonResponse
import random
from .gemini_integration import evaluate_answer, generate_question  # hypothetical utilities

# Mock questions for fallback
default_questions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Describe a challenge you faced and how you handled it.",
    "Why do you want to work in this role?",
    "Where do you see yourself in 5 years?"
]

def interview_page(request):
    return render(request, "assistant/interview.html")


def get_next_question(request):
    # Use Gemini API or fallback to random
    question = generate_question() or random.choice(default_questions)
    return JsonResponse({"question": question})

def evaluate_user_answer(request):
    user_answer = request.POST.get("answer")
    feedback = evaluate_answer(user_answer)  # Returns AI feedback
    return JsonResponse({"feedback": feedback})
