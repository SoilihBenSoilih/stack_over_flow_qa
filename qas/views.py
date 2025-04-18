from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
import json

def index_page(request):
    return render(request, 'index.html')


@require_http_methods(["POST"])
@csrf_protect
def qa(request):
    if request.content_type != 'application/json':
        return JsonResponse("Le contenu doit être au format JSON.")

    try:
        data = json.loads(request.body)
        question = data.get("question", "").strip()
        tags = data.get("tags", [])

        if not question:
            return JsonResponse("Le champ 'question' est requis.", status=400)

        if not isinstance(tags, list):
            return JsonResponse("Le champ 'tags' doit être une liste.", status=400)

        # Simuler une réponse
        dummy_answer = f"Réponse générée pour : « {question} » avec les tags {tags}"
        return JsonResponse({"answer": dummy_answer})

    except json.JSONDecodeError:
        return JsonResponse("Format JSON invalide.")

    except Exception as e:
        return JsonResponse({"error": "Une erreur interne s'est produite."}, status=500)
