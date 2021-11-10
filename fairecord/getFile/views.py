from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,Http404
from django.template import loader
from .models import File

#request 인자 받고 httpresposne를 반환함
#client로 부터 request를 받으면 여러가지 정보를 받게 될 것임
#data 추출 저장 파일 다운로드 등..
def index(request):
    latest_file_list = File.objects.order_by('-down_date')[:5]
    template = loader.get_template('getFile/index.html')
    context = {
        'latest_file_list': latest_file_list,
    }
    return render(request, 'getFile/index.html', context)

def detail(request, file_id):
    #1
    # return HttpResponse("You're looking at question %s." % file_id)

    #2
    # try:
        # question = Question.objects.get(pk=file_id)
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")
    #3
    filecontent = get_object_or_404(File, pk=file_id)
        
    return render(request, 'getFile/index.html', {'filecontent': filecontent})

# def results(request, file_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % file_id)

# def vote(request, file_id):
#     return HttpResponse("You're voting on question %s." % file_id)

