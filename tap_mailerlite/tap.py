"""mailerlitetap tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_mailerlite.streams import (
    mailerlitetapStream,
    SubscribersStream,
    GroupsStream,
    CampaignsStream,
)

STREAM_TYPES = [
    SubscribersStream,
    GroupsStream,
    CampaignsStream,
]


class Tapmailerlitetap(Tap):
    """mailerlitetap tap class."""
    name = "tap-mailerlite"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]

if __name__ == "__main__":
    Tapmailerlitetap.cli()
