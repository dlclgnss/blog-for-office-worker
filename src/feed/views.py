from django.shortcuts import render
from .models import Article,Comment,Hashtag


def index(request):

    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = Hashtag.objects.all()
    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category = category)
    else:
        article_list = Article.objects.filter(hashtag__name = hashtag) #model에 hashtag의name을 가져와서 집어넣는다.


    # category_list = set([])
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # 같은 내용인데 문법으로 짧게코딩 ↓#
    category_list = set([
    (article.category,article.get_category_display()) #튜플모양으로 전달, get_category_displays는 'dv','ps'를 뜻함
    for article in article_list
    ])

    ctx = {
        "article_list":article_list,
        "hashtag_list":hashtag_list,
        "category_list":category_list
    }
    return render(request,'index.html',ctx)


def detail(request,article_id):
    article = Article.objects.get(id = article_id )
    hashtag_list = Hashtag.objects.all()
    ctx={
        'article':article,
        "hashtag_list":hashtag_list,
    }
    return render(request,'detail.html',ctx)


# def about(request):
#     pass
