
import requests
from django.shortcuts import render
from .models import Chat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 외부 API URL
url = "https://4e56-34-125-107-166.ngrok-free.app/qa/"

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        try:
            # 외부 API에 전달할 데이터 구성
            data = {
                'question': question,
                'context': '''
                    인공지능은 인간의 학습능력, 추론능력, 지각능력을 인공적으로 구현시키는 컴퓨터과학의 하위 분야입니다.
                    컴퓨터는 과거의 유사한 행동 사례를 통해 얻은 광범위한 데이터를 사용하여 인간의 행동을 '모방'하도록 프로그래밍됩니다.
                    인공지능의 목표는 인간의 삶을 개선하고 생산성을 향상하는 것입니다. 업무 현장에서 인간 사용자의 능력을 확장하고 효율성, 생산성 및 만족도를 높이는 기술로서 활용되고 있습니다.
                '''
            }
            
            # 외부 API 호출 (POST 요청)
            response = requests.post(url, json=data)

            # API 응답이 성공적일 경우, 답변을 받아옴
            if response.status_code == 200:
                answer = response.json().get('answer')
            else:
                answer = "API 호출에 실패했습니다.  " + str(response.status_code)

            # DB에 질문과 답변 저장
            chat = Chat(question=question, answer=answer)
            chat.save()

        except Exception as e:
            answer = "답변을 생성할 수 없습니다. 오류: " + str(e)

        # JsonResponse로 반환
        return JsonResponse({'question': question, 'answer': answer})

    return render(request, 'chatbot/index.html')
