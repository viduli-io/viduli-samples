from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from knox.models import AuthToken


class Command(BaseCommand):
    help = "Create an authentication token for a user"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="Username to create token for")

    def handle(self, *args, **options):
        username = options["username"]

        User = get_user_model()

        try:
            user = User.objects.get(username=username)
            instance, token = AuthToken.objects.create(user)

            self.stdout.write(self.style.SUCCESS(f"Token created for user: {username}"))
            self.stdout.write(f"Token: {token}")
            self.stdout.write(
                f"Use this token in the Authorization header as: Token {token}"
            )
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User "{username}" does not exist'))
            self.stdout.write("Create a user first or use the seed command")
