import sentry_sdk
import time
import random

from django.http import HttpResponse, JsonResponse
from .models import BlogPost, Ingredient
from .serializers import BlogPostSerializer
from sentry_sdk import start_transaction


def index(request):
    return HttpResponse('Hi there! You\'re at the blog index.')


def blog_post_list(request):
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(posts, many=True, fields=['id', 'title'])
    return JsonResponse(serializer.data, safe=False)


def trivial_function():
    with sentry_sdk.start_span(op="wait", description="trivial wait function") as span:
        t = random.randint(0, 20)
        time.sleep(t/10)
        span.set_tag("wait.time", t)
        span.set_data("wait.otherdata", f"Sleep for {t} s")
    return


def blog_detail(request, pk):
    try:
        post = BlogPost.objects.get(id=pk)
    except Exception as err:
        sentry_sdk.capture_exception(err)
        return HttpResponse(status=404)

    with start_transaction(op="task", name="blog_post_serializer"):
        trivial_function()
        serializer = BlogPostSerializer(post)

    return JsonResponse(serializer.data)

