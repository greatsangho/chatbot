
import requests
from django.shortcuts import render
from .models import Chat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        try:            
            if "안녕" in question:
                answer = '저도 반가워요. 즐거운 하루 되세요'
            else:
                answer = "잘 모르겠습니다. 다시 입력해주세요";

            # DB에 질문과 답변 저장
            chat = Chat(question=question, answer=answer)
            chat.save()
        except Exception as e:
            answer = "답변을 생성할 수 없습니다. 오류: " + str(e)

        # JsonResponse로 반환
        return JsonResponse({'question': question, 'answer': answer})

    return render(request, 'chatbot/index.html')
