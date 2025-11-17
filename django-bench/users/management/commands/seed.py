from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from knox.models import get_token_model
from posts.models import Post
from faker import Faker


class Command(BaseCommand):
    help = "Seed the database with a test user and 1000 posts"

    def add_arguments(self, parser):
        parser.add_argument(
            "--posts",
            type=int,
            default=1000,
            help="Number of posts to create (default: 1000)",
        )

    def handle(self, *args, **options):
        num_posts = options["posts"]

        # Create or get the test user
        username = "testuser"
        email = "testuser@example.com"
        password = "testpass123"

        User = get_user_model()
        AuthToken = get_token_model()

        user, created = User.objects.get_or_create(
            username=username, defaults={"email": email}
        )

        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created user: {username}"))
        else:
            self.stdout.write(self.style.WARNING(f"User {username} already exists"))

        # Create authentication token
        instance, token = AuthToken.objects.create(user)
        self.stdout.write(self.style.SUCCESS(f"Created auth token: {token}"))

        # Create posts
        self.stdout.write(f"Creating {num_posts} posts...")

        fake = Faker()

        posts_to_create = []
        for i in range(num_posts):
            post = Post(text=fake.text(max_nb_chars=200), author=user)
            posts_to_create.append(post)

        # Bulk create in batches of 100 for better performance
        Post.objects.bulk_create(posts_to_create, batch_size=100)

        self.stdout.write(
            self.style.SUCCESS(f"\nSuccessfully created {num_posts} posts!")
        )
        self.stdout.write("\n" + "=" * 60)
        self.stdout.write("Seed data summary:")
        self.stdout.write(f"  Username: {username}")
        self.stdout.write(f"  Password: {password}")
        self.stdout.write(f"  Email: {email}")
        self.stdout.write(f"  Auth Token: {token}")
        self.stdout.write(f"  Posts Created: {num_posts}")
        self.stdout.write("=" * 60)
        self.stdout.write("\nYou can use this token in API requests:")
        self.stdout.write(f"  Authorization: Token {token}")
