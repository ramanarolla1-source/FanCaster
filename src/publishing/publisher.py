"""
Publishing module.

Responsible for preparing AI-generated content for
different publishing platforms.
"""


class Publisher:
    def publish(self, content, platform):
        """Publish content to the selected platform."""
        return f"Publishing to {platform}"
