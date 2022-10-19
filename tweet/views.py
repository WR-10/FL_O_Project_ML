from django.shortcuts import render, redirect
from .models import Article
from machine_learning import machine_learning
from .models import Article, TweetComment
from django.contrib.auth.decorators import login_required


def write(request):
    # user = authenticate(request, username = username, password = password)
    # if user:
        
        if request.method == "GET":
            return render(request, 'write.html')
        elif request.method == "POST":
            article = Article()
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.image = request.FILES['image']
            
            article.save()
            
            #* 이 포스팅의 이미지로 Yolov5 돌려서 결과(tag) 출력

            # tag = machine_learning.ml_yolov5(article.image)

            # tag model(db) 저장

            # article.tag 저장
            

            # Article.objects.create(title = title, content = content, image = article.image)


def community(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-create_at')
        context = {
            'articles' : articles
        }

        
        return render(request, 'community.html', context)


def add(request, id):
    id_com = Article.objects.get(id = id) # get의 의미 db에 A필드에 B인걸 가지고 오겠따(where같은개념)  
    com = {
        'id_com' : id_com,
    }
    print(id_com.id) 
    return render(request, 'add.html', com) #render는 type는 반드시 딕셔너리만 가능하게끔 되어있다. 

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
        TC.tweet = current_tweet
        TC.save()
        
        return redirect('/write/'+str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/write/'+str(current_tweet))


def post_detail(request, id):
    if request.method == 'GET':
        #todo 여기에 게시글
        return render(request, 'post_detail.html')
    
@login_required
def post_like(request, id):
    me = request.user
    click_post = Article.objects.get(id=id) #클릭된 유저
    if me in click_post.likes.all(): #라이크 한 사람들 모두 가져옴
        click_post.likes.remove(request.user) # 그 사람중에 나를 뺌
    else:
        click_post.likes.add(request.user)
    return redirect('/')