import random
from django.core.management.base import BaseCommand
from blog.models import Post
from faker import Faker

class Command(BaseCommand):
    help = 'Generate and load a large number of posts into the database for testing caching.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=1000,
            help='Number of posts to create (default: 1000)',
        )

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        self.stdout.write(f"Generating {count} posts...")

        posts = [
            Post(
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=10),
                published_date=fake.date_time_this_year()
            )
            for _ in range(count)
        ]

        Post.objects.bulk_create(posts)
        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} posts."))
