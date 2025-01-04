from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post
from django.core.cache import cache
import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=Post)
@receiver(post_delete, sender=Post)
def clear_post_cache(sender, **kwargs):
    cache.delete('all_posts')
    logger.info("\nCache has been cleared!\n")
