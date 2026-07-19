"""
TxLINE client.

Handles communication with the TxLINE Sports Data API.
"""


class TxLineClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_live_events(self):
        """Retrieve live sports events."""
        return []

    def get_fixtures(self):
        """Retrieve upcoming fixtures."""
        return []

    def get_scores(self):
        """Retrieve latest scores."""
        return []
