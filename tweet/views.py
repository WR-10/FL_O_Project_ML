from django.shortcuts import render, redirect
from .models import Article, Tag
from machine_learning import machine_learning
from .models import Article, TweetComment, Tag
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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
            return redirect('/tweet/community/')
                
                
                
                
                
                
                
                
                
                
                
                # for tn in Tag.objects.all(i): # Tag의 모든 것을 가져오고 그 중에 tn이 있다면
                #     tag = Tag.objects.get(tagname=tn) # tag를 가져오고 그렇지 않으면... 추가를 해줘야 하는데...
                # else: # 없으면??
                #     tag.objects.create(tagename=i) # 추가를 해주는 코드인데... 여기를 어떻게 써야되지
                #     # article.taghash.add(tag) # tag를 추가해라>???? 이게 맞나? object.create??
            
            
def search_result(request):
    if request.method == "POST":
        searchname = request.POST.get('search_button')
        tags = Tag.objects.filter(tagname=searchname) # 검색어가 필요함
        articles = Article.objects.filter(taghash__in = tags).order_by('-updated_at')
        
        return render(request, 'search_result.html', {'searchname':searchname, 'articles':articles})
    elif request.method == 'GET':
        print('search_result들어옴')
        return render(request, 'search_result.html')
        

def community(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-updated_at')
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


