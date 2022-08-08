from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ...'},
    {'id': 2, 'title': 'view', 'body': 'View is ...'},
    {'id': 3, 'title': 'model', 'body': 'Model is ...'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href = "/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href = "/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href = "/create">create</a></li>
        </ul>
    </body>
    </html>
    '''

def home(request):
    article = '''
    <h2>Welcome</h2>
    Welcome to django world!
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic["id"] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

#제출버튼을 클릭했을 때, title과 body에 담겨 있는 데이터를 서버에 원하는 path로 전송하기 위해서는
#코드들을 form 태그로 감싸주어야 한다.
#action - 현재 create 페이지로 전송하겠다.
#request method를 따로 지정하지 않으면 GET 방식으로
#POST 방식을 사용하면 헤더라는 것 안에 데이터를 포함해서 눈에 보이지 않게 보냄
#CSRF verification failed. => 장고가 가지는 보안기능
#=> 우회
#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt

@csrf_exempt
def create(request):
    global nextId
    #GET 방식으로 받은 데이터라면
    if request.method == 'GET':
        article = '''
            <form action = "/create/" method = "post"> 
                <p><input type = "text" name = "title" placeholder = "title"></p>
                <p><textarea name = "body" placeholder = "body"></textarea></p>
                <p><input type = "submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    #POST 방식으로 받은 데이터라면
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body}
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        topics.append(newTopic)
        return redirect(url)