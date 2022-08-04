from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ...'},
    {'id':2, 'title':'view', 'body':'View is ...'},
    {'id':3, 'title':'model', 'body':'Model is ...'}
]

def home(request):
    #topics를 전역변수로 선언
    global topics
    ol = ''
    #topics를 돌면서
    for topic in topics:
        #각 li태그(topic의 title)에 각각의 페이지(topic의 id와 관련된 read 페이지)를 연결
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome!</h2>
    </body>
    </html>
    ''')

def create(request):
    return HttpResponse('Create!')

def read(request, id):
    return HttpResponse('Read!' + id)