from django.shortcuts import redirect, render
from django.http import Http404,HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    'january': 'Exercise daily for 30 minutes',
    'february': 'Read one book',
    'march': 'Learn something new each day',
    'april': 'Drink at least 2 liters of water daily',
    'may': 'Wake up early every day',
    'june': 'Practice a new skill for 20 minutes daily',
    'july': 'Avoid junk food for the entire month',
    'august': 'Write a daily journal entry',
    'september': 'Learn and revise one topic each day',
    'october': 'Limit social media usage to 30 minutes per day',
    'november': 'Express gratitude by writing one thankful note daily',
    'december': '',
}

def index(request):
    # return HttpResponse("Welcome to the Challenges App!!")
    # html_content = """
    # <html>
    #     <head><title>Challenges</title></head>
    #     <body>
    #         <h1>Monthly Challenges</h1>
    #         <ul>
    #             <li><a href="/testapp/january/">January</a></li>
    #             <li><a href="/testapp/february/">February</a></li>
    #         </ul>
    #     </body>
    # </html>
    # """
    # return HttpResponse(html_content)
    
    
    # list_items = ""
    months = list(monthly_challenges.keys())
    
    months=list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("testapp:monthly_challenge", args=[month])
        # list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "testapp/index.html",{
        "months": months
    })

def january(request):
    return HttpResponse("January Challenge: Exercise daily!!")

def february(request):
    return HttpResponse("February Challenge: Read a book")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        # return HttpResponse(challenge_text)
        # response_data = render_to_string(" testapp/testapp.html")
        # return HttpResponse(response_data)
        return render(request, 'testapp/challenge.html',{
            "text" : challenge_text,
            "month_name" : month
        })
    except KeyError:
        # raise Http404()
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        # return HttpResponse(monthly_challenges.get(month, "Invalid month"))

def old_url(request):
    return HttpResponseRedirect('/testapp/january')

def monthly_challenge_by_number(request, month):
    months=list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponse("Invalid month",status=404)
    return redirect(f'/testapp/{months[month-1]}')
