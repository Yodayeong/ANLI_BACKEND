from django.shortcuts import render, HttpResponse

topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ...'},
    {'id': 2, 'title': 'view', 'body': 'View is ...'},
    {'id': 3, 'title': 'model', 'body': 'Model is ...'}
]

#여러번 재활용 해서 쓸 수 있는 HTMLTemplate을 만들어준다.
#이때, 본문의 내용은 페이지 별로 다르게 하기 위해서, 본문의 내용은 articleTage 인자로 받는다.
def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href = "/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href = "/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>
    </html>
    '''

#home에서 나올 본문의 내용을 article에 담아준다.
def home(request):
    article = '''
    <h2>Welcome</h2>
    Welcome to django world!
    '''
    return HttpResponse(HTMLTemplate(article))

#topic의 id별로 다른 본문의 내용이 나오도록 for문을 사용해서 article에 담아준다.
def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic["id"] == int(id):
            article = f'{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('Create!')