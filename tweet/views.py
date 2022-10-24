from django.shortcuts import render, redirect
from .models import Article, Tag
from machine_learning import machine_learning
from .models import Article, TweetComment, Tag
from django.contrib.auth.decorators import login_required
from user.models import Users


def write(request):
    our = request.user.is_authenticated
    if our:
        if request.method == "POST":
            article = Article()
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.image = request.FILES['image']
            article.user = request.user
            
            article.save()
            
            tags = machine_learning.ml_yolov5(str(article.image))
            exist_tags = Tag.objects.all()
            tag_list = []
            for exist_tag in exist_tags:
                tag_list.append(exist_tag.tagname)
            for tag in tags:
                if tag in tag_list:
                    pass
                else:
                    Tag.objects.create(tagname=tag)
                tagman =Tag.objects.get(tagname=tag)
                article.taghash.add(tagman)
          
            return redirect('/')
    else: 
        return redirect('/accounts/login/')        

def search_result(request):
    if request.method == "POST":
        searchname = request.POST.get('search_button')
        tags = Tag.objects.filter(tagname=searchname)
        articles = Article.objects.filter(taghash__in = tags, user_id=request.user.id).order_by('-updated_at')
        return render(request, 'search_result.html', {'searchname':searchname, 'articles':articles})
    elif request.method == 'GET':
        return render(request, 'search_result.html')

def search_target_result(request,id):
    if request.method == "POST":
        searchname = request.POST.get('search_button')
        tags = Tag.objects.filter(tagname=searchname)
        articles = Article.objects.filter(taghash__in = tags, user_id=id).order_by('-updated_at')
        target_user = Users.objects.get(id = id)
        return render(request, 'serve.html', {'searchname':searchname, 'articles':articles,'target_user': target_user})
    elif request.method == 'GET':
        return render(request, 'search_result.html')
        
def add(request, id):
    id_com = Article.objects.get(id = id) 
    com = {
        'id_com' : id_com,
    }
    return render(request, 'add.html', com)

def mod(request, id):
    if request.method == 'GET':
        id_sa = Article.objects.get(id = id)
        b = {
            'id_sa' : id_sa,
        }
        return render(request, 'mod.html', b)

    elif request.method == 'POST':
        id_sa = Article.objects.get(id = id)
        id_sa.title = request.POST.get('title')
        id_sa.content = request.POST.get('content')
        id_sa.save()
        
        return redirect('/tweet/community/')        
        

@login_required
def write_comment(request, id): # 댓글 작성
    if request.method =='POST':
        comment = request.POST.get('comment','')
        current_tweet = Article.objects.get(id = id)
        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.article = current_tweet
        TC.save()
        return redirect('/tweet/post-detail/'+str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/post-detail/comment/'+str(current_tweet))

def post_detail(request, id):
    if request.method == 'GET':
        my_article = Article.objects.get(id=id)
        tweet_comment = TweetComment.objects.filter(article_id=id).order_by('-created_at')
        return render(request,'post_detail.html',{'article':my_article,'comments':tweet_comment})

    
@login_required
def post_like(request, id):
    me = request.user
    click_post = Article.objects.get(id=id)
    if me in click_post.likes.all():
        click_post.likes.remove(request.user)
    else:
        click_post.likes.add(request.user)
    return redirect('/')
