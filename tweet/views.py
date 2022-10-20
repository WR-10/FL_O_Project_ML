from django.shortcuts import render, redirect
from .models import Article, Tag
from machine_learning import machine_learning
from .models import Article, TweetComment, Tag
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def write(request):
    our = request.user.is_authenticated
    if our:
        if request.method == "POST":
            article = Article()
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.image = request.FILES['image']
            article.user = request.user
            
            print(request.user.id) # 웹에서 request안에 로그인의 사용자가 들어있는데 그걸 가져올때는 request.user 안에 usermodel안에 정보가 들어있다. 
            article.save()
            
            tags = machine_learning.ml_yolov5(str(article.image))
            exist_tags = Tag.objects.all() # tag list 형태로 담긴다. ex) person, teddy bear
            tag_list = []
            for exist_tag in exist_tags:
                tag_list.append(exist_tag.tagname) # tagname만 나온다. 내가 잘 판단할 수 있게 단순화 한 for문... 안으로 이중포문을 안돌리고 이중포문 돌렸더니 이중포문 실행안되었음
            for tag in tags: # tags for문 돌리기
                if tag in tag_list:
                    pass
                else:
                    Tag.objects.create(tagname=tag)
                ### 여기까지가 태그 저장 기능 함수
                tagman =Tag.objects.get(tagname=tag) # tagname get
                article.taghash.add(tagman) # 가져온거 추가 
          
            return redirect('/')
    else: 
        return redirect('/accounts/login/')        
      
            #* 이 포스팅의 이미지로 Yolov5 돌려서 결과(tag) 출력

def search_result(request):
    if request.method == "POST":
        searchname = request.POST.get('search_button')
        tags = Tag.objects.filter(tagname=searchname) # 검색어가 필요함
        articles = Article.objects.filter(taghash__in = tags, user_id=request.user.id).order_by('-updated_at')
        
        return render(request, 'search_result.html', {'searchname':searchname, 'articles':articles})
    elif request.method == 'GET':
        print('search_result들어옴')
        return render(request, 'search_result.html')
        



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
        my_article = Article.objects.get(id=id) #아티클 id 담아
        tweet_comment = TweetComment.objects.filter(article_id=id).order_by('-created_at') #
        return render(request,'post_detail.html',{'article':my_article,'comments':tweet_comment})

    
@login_required
def post_like(request, id):
    me = request.user
    click_post = Article.objects.get(id=id) #클릭된 유저
    if me in click_post.likes.all(): #라이크 한 사람들 모두 가져옴
        click_post.likes.remove(request.user) # 그 사람중에 나를 뺌
    else:
        click_post.likes.add(request.user)
    return redirect('/')


# def post_detail(request, id):

#     id_com = Article.objects.get(id = id) # get의 의미 db에 A필드에 B인걸 가지고 오겠따(where같은개념)  
#     com = {
#         'id_com' : id_com,
#     }
#     return render(request,'post_detail.html',com)
