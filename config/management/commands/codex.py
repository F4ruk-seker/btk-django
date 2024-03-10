from django.core.management import BaseCommand
from django.core.management.commands import startapp


class Command(startapp.Command):
    def add_arguments(self, parser):
        ...
        # Positional arguments
        # parser.add_argument("poll_ids", nargs="+", type=int)

        # Named (optional) arguments
        # parser.add_argument(
        #     "--delete",
        #     action="store_true",
        #     help="Delete poll instead of closing it",
        # )

    def handle(self, *args, **options):
        super().handle(**options)
