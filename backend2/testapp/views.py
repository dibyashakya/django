from django.shortcuts import redirect, render
from django.http import Http404,HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

# # Create your views here.
# def index(request):
#     months = list(monthly_challenges.keys())
#     return render(request,'testapp/index.html',{
#         'months':months
#     })

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month.lower()]
#         return HttpResponse(f"<h1>{month} Challenge:{Challenge_text}</h1>")
#         # return render(request,'testapp/challenge.html',{
#         #     'text': challenge_text,
#         #     'month_name': month.capitalize()
#         # })
#     except:
#         return HttpResponseNotFound('<h1>This is not available</h1>')
#         # raise Http404()

# def monthly_challenge_by_num(request, month):
#     months = list(monthly_challenges.keys())
#     redirect_month = months[month - 1]
#     redirect_url=reverse('monthly_challenge',args=[redirect_month])
#     return redirect(redirect_url)

# def index(request):
#     list_items = ""
#     months = list(monthly_challenges.keys())

#     for month in months:
#         capitalized_month = month.capitalize()
#         month_path = reverse("month-challenge", args=[month])
#         list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

#     # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

#     response_data = f"<ul>{list_items}</ul>"
#     return HttpResponse(response_data)
#     # return HttpResponse("Welcome to the Challenges App!")

# # def january(request):
# #     return HttpResponse("January challenge:exercise daily")


# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month.lower()]
#         response_data = render_to_string("challenges/challenge.html")
#         return HttpResponse(response_data)
#         # return HttpResponse(response_data, status=200)  # Setting Status Codes
#     except:
#         return HttpResponseNotFound("<h1>This month is not supported!</h1>")

# # def monthly_challenge_by_number(request, month):
# #     months = list(monthly_challenges.keys())
# #     redirect_month = months[month - 1]
# #     # Using reverse with named URL
# #     redirect_url = reverse('monthly-challenge', args=[redirect_month])
# #     return redirect(redirect_url)

# def home(request):
#     return HttpResponse("Testapp is working 🚀")

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
    'december': 'Reflect on the year and plan goals for next year',
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
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def january(request):
    return HttpResponse("January Challenge: Exercise daily!!")

def february(request):
    return HttpResponse("February Challenge: Read a book")

def monthly_challenge(request, month):
    # try:
    #     challenge_text = monthly_challenges[month.lower()]
    #     # return HttpResponse(challenge_text)
    #     response_data = f"<h1>{challenge_text}</h1>"
    #     return HttpResponse(response_data)
    # except KeyError:
    #     return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    return HttpResponse(monthly_challenges.get(month, "Invalud month"))

def old_url(request):
    return HttpResponseRedirect('/testapp/january')

def monthly_challenge_by_number(request, month):
    months=list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponse("Invalid month",status=404)
    return redirect(f'/testapp/{months[month-1]}')
