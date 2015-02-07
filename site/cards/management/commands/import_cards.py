from optparse import make_option

from django.core.management.base import BaseCommand

from cards.models import Card, CardContent


class Command(BaseCommand):
    help = 'Import cards from a text file.'
    option_list = BaseCommand.option_list + (
        make_option('-i', '--input'),
    )

    def handle(self, *args, **options):
        file = open(options['input']).read()
        parts = (x.strip() for x in file.split('###'))
        parts = filter(lambda x: len(x) > 0 and x != '===', parts)
        parts = map(lambda x: map(lambda y: y.strip(), x.split('===')), parts)

        for part in parts:
            card = Card.objects.create()
            card.save()
            card_content = CardContent.objects.create(
                card=card,
                front=part[0],
                back=part[1],
            )
            card_content.save()
