"""
Test checks that there are no duplicated roles in the body of message
"""


from django.test import TestCase
from campaign.services.wave_wizard import wave_wizard
from campaign.models.campaign import Campaign
from campaign.models.activity import Activity


class TestWaveWizard(TestCase):
    fixtures = ['campaign/tests/fixtures/testdata.json']

    def test_wave_wizard(self):
        campaign: object = Campaign.objects.first()

        self.assertIsNotNone(campaign)
        wave_wizard(None, campaign)

        activities = list(Activity.objects.filter(campaign=campaign))
        self.assertEqual(len(list(activities)), 3)
        for activity in activities:
            lines_with_roles = list(line for line in activity.body.split("\n") if line.startswith("  - ") is True)
            self.assertEqual(len(set(lines_with_roles)), len(lines_with_roles))



