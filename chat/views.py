from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Theme,Message
from .forms import Form_theme,Form_message
import openai
openai.api_key=""

def frontpage(request):
    themes = Theme.objects.all()
    if request.method == "POST":
        form_theme = Form_theme(request.POST)
        if form_theme.is_valid():
            comment = form_theme.save(commit=False)
            comment.theme = themes
            comment.save()

            #return redirect("frontpage")
    else:
        form_theme = Form_theme()
    context = {
        'themes': themes,
        'form_theme':form_theme
    }
    return render(request, 'frontpage.html', context)

def chatpage(request, slug):
    theme = Theme.objects.get(slug=slug)
    messages_db = Message.objects.filter(Theme=theme)
    themes = Theme.objects.all()
    history=[]
    
    if not Message.objects.filter(role='system', Theme=theme).exists():
        history = [{"role": "system", "content": "You are a helpful assistant."}]
        Message.objects.create(Theme=theme, role="system", message="You are a helpful assistant.")

    message_history = list(Message.objects.filter(Theme=theme).values('role', 'message'))
    # メッセージの履歴を `history` リストに追加
    history = [{"role": item['role'], "content": item['message']} for item in message_history]
    
    if request.method == "POST":
        form_message = Form_message(request.POST)
        if form_message.is_valid():
            comment = form_message.save(commit=False)
            comment.Theme = theme
            comment.save()
            message = form_message.cleaned_data.get('message')  # フォームからメッセージを取得
        else:
            comment = None
            message = ''  # フォームが無効な場合は空のメッセージを作成
    else:
        form_message = Form_message()
        message = ''  # POST メソッド以外の場合は空のメッセージを作成
        
    if not message == '':
        history.append({"role": "user", "content": message})
        converted_history = [history[0]] +[
            {"role": "user", "content": item["content"]} if item["role"] == "system" else item
            for item in history[1:]
        ]
        
        # ChatGPT による返信を取得
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=converted_history,
            max_tokens=100
        )
        res_content = res["choices"][0]["message"]["content"]

        # ChatGPT の返信を保存
        Message.objects.create(Theme=theme, role='assistant', message=res_content)
    
    context = {
        'theme': theme,
        'themes': themes,
        'messages': messages_db,
        'form_message': form_message,
    }

    return render(request, 'chatpage.html', context)
    
def back_to_page(request):
    return render(request,'frontpage')

def my_view(test):
    # 処理
    messages.success(test, '処理が完了しました。')
    return redirect('chatpage')
