from django.shortcuts import render

# Create your views here.


from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Max

from .models import Post, Comment
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('comments')
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_at','commented_date']

    def get_queryset(self):
        queryset = self.queryset
        title = self.request.query_params.get('title')
        if title == 'None':
            queryset = queryset.filter(title__isnull=True)

        ordering_param_val = self.request.query_params.get('ordering')
        if ordering_param_val in ['commented_date','-commented_date']:
            queryset = queryset.filter(title__isnull=False).annotate(
                commented_date=Max('comments__publication_date')
            )
        
        return queryset

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        if not post.comments.exists():
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Cannot delete post with comments'}, status=status.HTTP_400_BAD_REQUEST)