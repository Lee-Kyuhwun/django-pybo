from django.db import models

# 질문과 답변을 하는 파이보 모델을 만든다.
# 질문과 답변에 해당하는 모델이다.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject # 이러면 shell에서 id값 대신 제목을 표시 할 수 있다.

#Question 모델은 제목과 내용그리고 작성일지로 이루어져있다.
# 제목은 최대 200자까지 가능하고 최대 길이를 200자로 설정하였다.
# 제목처럼 글자수의 길이가 제한된 텍스트는 CharField를 사용해야한다.
# 글자수 제한이 없는 텍스트는 TextField를 사용해야한다.
# 작성일지치럼 날짜와 시간에 관계된 속성은 DateTimeField를 사용한다.
class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
# 답변은 질문(Question) 모델을 속성으로 가져가야하므로
# 기존 모델을 속성으로 연결하기 위한 ForeignKey를 사용한다.
# ForiegnKey는 다른 모델과 연결하기 위해 사용한다.
# on_delete=models.CASCADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미이다.

