import sentry_sdk

from django.http import HttpResponse, JsonResponse
from .models import BlogPost
from .serializers import BlogPostSerializer


def index(request):
    return HttpResponse('Hello, world. You\'re at the blog index.')


def blog_post_list(request):
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


def blog_detail(request, pk):
    try:
        post = BlogPost.objects.get(id=pk)
    except Exception as err:
        sentry_sdk.capture_exception(err)
        return HttpResponse(status=404)

    serializer = BlogPostSerializer(post)
    return JsonResponse(serializer.data)

