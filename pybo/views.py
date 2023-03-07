from django.shortcuts import redirect, render, get_object_or_404
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .form import QuestionForm,AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page','1') # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)
"""
page = request.GET.get('page', '1')은 http://localhost:8000/pybo/?page=1 처럼 GET 방식으로 호출된 URL에서 page값을 가져올 때 사용한다. 
만약 http://localhost:8000/pybo/ 처럼 page값 없이 호출된 경우에는 디폴트로 1이라는 값을 설정한다.
qeustion_list는 게시물 전체를 의미하는 데이터이고 두번째 파라미터 10은 페이지당 보여줄 게시물의 개수이다.
paginator를 이용하여 요청된 페이지에 해당되는 페이징객체(page_obj)를 생성했다. 이렇게 하면 장고 내부적으로 데이터 전체를 조회하지않고 해당 페이지의 데이터만 조회하도록 쿼리
가 변경된다.
"""

# Question.objects.order_by('-create_date') -> 질문 목록 받기
# render로 파이썬 테이터를 템플릿에 적용해서 html로 반환한다.
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question_id)


# answer_create 함수의 매개변수 question_id는 url 매핑에 의해
# 그 값을 전달한다
"""
http://locahost:8000/pybo/answer/create/2/ 라는 페이지를 요청하면 매개변수 question_id에는 2라는 값이 전달될 것이다.
그리고 답변 등록시 텍스트창에 입력한 내용은 answer_create함수의 첫번째 매개변수인 request 객체를 통해
읽을 수 있다. 즉, request.POST.get('content')로 텍스트창에 입력한 내용을 읽을 수 있다. request.POST.get('content')는 POST로 전송된 폼(form) 데이터 항목 중 content 값을 의미한다.
그리고 답변을 생성하기 위해 question.asnswer_set.create 를 사용하였다. question.answer_set은 질문의 답변을 의미한다. Question과 Answer 모델은 
서로 ForeignKey 로 연결되어 있기때문에 이처럼 사용할 수 있다.
"""


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # request.POST를 인수로 QuestionForm을 생성할 경우
        # request.POST에 담긴    값이   QuestionForm의    subject, content    속성에    자동으로    저장되어   객체가생성된다.
        if form.is_valid(): # 폼이 유효하다면
            question = form.save(commit=False) #임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            question.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


"""
POST GET에 따라서 다르게 처리된다. 질문 목록 화면에서 질문등록하기 버튼을 클릭할 경우에는 /pybo/question/create가 get으로 요청되고
question_create함수가 실해오딘다. 왜냐하면 <a href="{% url 'pybo:question_create' %}" class="btn btn-primary">질문 등록하기</a>
처럼 링크를 통해 페이지를 요청하면 무조건 get이기 때문이다. 따라서 이 경우에는 request.method값이 get이 되어서 else 구문을 타고 질문을 등록하는 화면으로 간다.




question_create는 QuestionForm를 사용한다. render 함수에 전달한 {'form': form}은 템플리세엇 질문 등록시 사용할 폼 엘리먼트를 생성할때 사용된다.
"""
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)