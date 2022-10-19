from re import T
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

            tag = machine_learning.ml_yolov5(str(article.image)) # 여기서 TypeError >> str로 변경해야된다.
            # tag list가 나올 준비 되있음 print(tag) 해본 결과 잘 나옴
            # 뭐 되는게 없네 
            # 여기부터 Tag 함수 작성을 한다.
            # 내가 db 저장해야 할 것들 리스트에 있는 tag잖아
            for i in tag: # 태그 리스트를 for문을 돌린다.
                
                # if '#' in i: # 만약 태그 중 '#'이 있다면 근데 #이 없는데?
                    # 태그를 테이블id에 저장해야한다??!?? >> tag_id?
                # tag = Tag()
                # tag.tagname = i
                tag = Tag.objects.get(tagname=i)
                # print(i) # person이라고 나옴...
                # tag.save() # 여기도 db 저장은 안됨 ??? 아 왜 안될까~~~용? 22:36 >> 여기서 문제나옴 쓰부럴 
                #todo 이거는 tag를 만드는거다.
        # tag model(db) 저장
                # article.taghash.set = Tag.objects.get(tagname=i) # pk? 또 이거보니깐 모르겠네 내 생각은 article에 있는 pk 임 게시글 몇 번째 id ?!?!? 여기문제인데 미치겠다.
                # article.save() # article.taghash NO!!
                article.taghash.add(tag) # 37 tag와 같은 타입이다.
                print(article.taghash) # 여기서는 ['person'] 이라고 나옴! << 안나옴 머신러닝.py에서 print되서 나오는거였음 ㅜㅜ
            return redirect('/tweet/community/')
            # tag를 80개를 넣어야 되는데 초기에 table을 만들 때 tagname을 넣어줄 수 있는가??
            # article.tag 저장
            #* article.taghash에 저장 하는 함수이다.
            
            
def search_result(request):
    if request.method == "POST":
        searchname = request.POST.get('search_button') # 검색 창에서 POST를 받는다.
        # tag = Tag.?? 태그 검색 해야하는데 이거는 그러면 걸러내야함? 아 tag 결과를 걸러내야함!
        tag = Tag.objects.filter(tagname=searchname) # 이게 태그 걸러내는용
        feed = Article.objects.filter(taghash__in = tag).order_by('-updated_at')
        
        # return render(request, 'search_result.html', {'tag':tag, 'feed':feed})
        return render(request, 'search_result.html') # 다시 한번 또 기억하자 동근아 / 뒤에 꼭 써라.... 뒤지기 싫으면...
    elif request.method == 'GET': # GET은 RENDER로
        print('search_result들어옴')
        return render(request, 'search_result.html') # 다시한번 기억하자 동근아 html은 /안쓴다!!!
        

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


