import httpx
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from finding.models import Finding


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('target_id', nargs='?', type=str)

    def handle(self, *args, **options):
        url_to_scrape = settings.FINDINGS_API_URL + options['target_id']
        headers = {'Authorization': settings.FINDINGS_JWT_TOKEN}
        resp = httpx.get(url_to_scrape, headers=headers)

        finding_response = resp.json()["results"]
        finding = Finding(
            target_id=finding_response[0]["target"]["id"],
            definition_id=finding_response[0]["definition"]["id"],
            scans=finding_response[0]["scans"],
            url=finding_response[0]["url"],
            path=finding_response[0]["path"],
            method=finding_response[0]["method"],
        )
        finding.save()
