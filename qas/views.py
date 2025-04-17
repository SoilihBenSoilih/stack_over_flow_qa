from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index_page(request):
    return render(request, 'index.html')

# @csrf_exempt
# def qa_view(request):
#     context = {
#         "tags": ["Python", "JavaScript", "Java"],
#         "question": None,
#         "answer_markdown": None,
#         "is_loading": False,
#         "disable_submit": False,
#         "selected_tags": ["Java"],
#     }

#     if request.method == "POST":
#         question = request.POST.get("question")
#         selected_tags = request.POST.getlist("tags")
#         context["question"] = question
#         context["selected_tags"] = selected_tags

#         if question and selected_tags:
#             context["is_loading"] = True
#             context["disable_submit"] = True

#             # Simulation
#             context["is_loading"] = False
#             context["answer_markdown"] = f"**Bonne question !**\n\nVous avez demandé : _{question}_\n\n_Tags sélectionnés_ : `{', '.join(selected_tags)}`"

#     return render(request, "index.html", {
#         "question": request.POST.get("question", ""),
#         "tags": ["Python", "JavaScript", "Java"],
#         "selected_tags": request.POST.getlist("tags"),
#         "is_loading": False,  # ou True selon la logique
#         "answer_markdown": "### test"  # si tu as une réponse
#     })