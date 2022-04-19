from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from blog.models import Post


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_detail_post(request, pk):
    post = Post.objects.get(id=pk)
    comment = post.comments.filter(level_nesting__lte=3)
    serializer = PostSerializer(post)
    serializer_comments = CommentSerializer(comment, many=True)
    return Response((serializer.data, {'comments': serializer_comments.data}))


@api_view(['GET'])
def get_lvl_comment(request, pk, lvl):
    post = Post.objects.get(id=pk)
    comment = post.comments.filter(level_nesting=lvl)
    serializer = PostSerializer(post)
    serializer_comments = CommentSerializer(comment, many=True)
    return Response((serializer.data, {'comments': serializer_comments.data}))
