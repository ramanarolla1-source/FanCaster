"""
FanCaster Application Entry Point.
"""

from txline.client import TxLineClient
from event_engine.processor import EventProcessor
from editorial.engine import EditorialEngine
from qvac.engine import QVACEngine
from publishing.publisher import Publisher


def main():
    print("Starting FanCaster...")

    txline = TxLineClient(api_key="YOUR_API_KEY")
    processor = EventProcessor()
    editorial = EditorialEngine()
    qvac = QVACEngine()
    publisher = Publisher()

    events = txline.get_live_events()

    for event in events:
        processed = processor.process(event)
        story = editorial.analyze(processed)
        content = qvac.generate_content(str(story))
        publisher.publish(content, "X")


if __name__ == "__main__":
    main()
