import time
import logging
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
def post_list(request):
    start_time = time.time()
    
    # Check if data is cached
    cached_posts = cache.get('all_posts')

    if cached_posts:
        end_time = time.time()
        logger.info(f"\nCache HIT - Time taken: {end_time - start_time:.4f} seconds\n")
        return Response(cached_posts)

    # If not cached, fetch from database
    posts = Post.objects.all().order_by('-published_date')
    serializer = PostSerializer(posts, many=True)
    cache.set('all_posts', serializer.data, timeout=60)  # Cache for 60 seconds

    end_time = time.time()
    logger.info(f"\nCache MISS - Query time: {end_time - start_time:.4f} seconds\n")
    return Response(serializer.data)
