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
        response_time = (time.time() - start_time) * 1000  # in milliseconds
        logger.info(f"\nCache HIT - Time taken: {response_time:.2f} ms\n")
        return Response(cached_posts)

    # If not cached, fetch from database
    posts = Post.objects.all().order_by('-published_date')
    serializer = PostSerializer(posts, many=True)
    cache.set('all_posts', serializer.data, timeout=60)  # Cache for 60 seconds

    response_time = (time.time() - start_time) * 1000  # in milliseconds
    logger.info(f"\nCache MISS - Query time: {response_time:.2f} ms\n")
    return Response(serializer.data)
