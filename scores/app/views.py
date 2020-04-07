from django.shortcuts import render
from django.http import HttpResponse
from app.models import userScore
from django.db.utils import IntegrityError

# Create your views here.


def index(request):

    """首页展示"""

    return HttpResponse("123")


def submit(request):

    """提交分数"""
    name = request.GET.get('name', None)
    score = request.GET.get('score', None)
    print(name, score)

    dic = {'name': name, 'score': score}

    obj = userScore(**dic)
    try:
        obj.save()
    except IntegrityError as err:
        print(err)
        userScore.objects.filter(name=name).update(score=score)
    return HttpResponse("提交成功")  


def ranking(request):

    """查询排行榜"""

    start = request.GET.get('start', None)
    end = request.GET.get('end', None)

    users = userScore.objects.filter().order_by('-score')
    sorting = []
    ranking = 1
    for i in users:
        i = i.to_dict()
        i["ranking"] = ranking
        sorting.append(i)
        ranking += 1

    try:
        sorting = sorting[int(start) - 1:int(end)]
    except:
        pass

    return render(request, "sorting.html", {"list": sorting})