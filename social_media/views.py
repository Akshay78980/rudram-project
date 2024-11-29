from django.shortcuts import render

# Create your views here.


from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Max

from .models import Post, Comment
from .serializers import PostSerializer

# class RecentCommentFilter(OrderingFilter):
#     def filter_queryset(self, request, queryset, value):
#         if value == 'recent_comments':
#             return queryset.annotate(latest_comment=models.Max('comments__publication_date')).order_by('-latest_comment')
#         return super().filter_queryset(request, queryset, value)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('comments')
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_at','latest_comment_date']

    def get_queryset(self):
        queryset = self.queryset
        title = self.request.query_params.get('title')
        if title == 'None':
            queryset = queryset.filter(title__isnull=True)

        ordering_param_val = self.request.query_params.get('ordering')
        if ordering_param_val in ['latest_comment_date','-latest_comment_date']:
            queryset = queryset.filter(title__isnull=False).annotate(
                latest_comment_date=Max('comments__publication_date')
            )
        
        return queryset

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        if not post.comments.exists():
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Cannot delete post with comments'}, status=status.HTTP_400_BAD_REQUEST)