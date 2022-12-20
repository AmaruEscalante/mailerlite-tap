"""Stream type classes for mailerlite-tap."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from mailerlite_tap.client import mailerlitetapStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class SubscribersStream(mailerlitetapStream):
    """Subscribers stream class."""
    name = "subscribers"
    path = "/subscribers"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.data[*]"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("email", th.StringType),
        th.Property("status", th.StringType),
        th.Property("source", th.StringType),
        th.Property("sent", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property("clicks_count", th.IntegerType),
        th.Property("open_rate", th.IntegerType),
        th.Property("click_rate", th.IntegerType),
        th.Property("ip_address", th.StringType),
        th.Property("subscribed_at", th.DateTimeType),
        th.Property("unsubscribed_at", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("fields", th.ObjectType(
            th.Property("city", th.StringType),
            th.Property("company", th.StringType),
            th.Property("country", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("name", th.StringType),
            th.Property("phone", th.StringType),
            th.Property("state", th.StringType),
            th.Property("z_i_p", th.StringType),
        )),
        th.Property("groups", th.ArrayType(th.StringType)),
        th.Property("opted_in_at", th.DateTimeType),
        th.Property("optin_ip", th.StringType),
    ).to_dict()

class GroupsStream(mailerlitetapStream):
    """Define custom stream."""
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("active_count", th.IntegerType),
        th.Property("sent_count", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property("open_rate", th.ObjectType(
            th.Property("float", th.IntegerType),
            th.Property("string", th.StringType),
        )),
        th.Property("clicks_count", th.IntegerType),
        th.Property("click_rate", th.ObjectType(
            th.Property("float", th.IntegerType),
            th.Property("string", th.StringType),
        )),
        th.Property("unsubscribed_count", th.IntegerType),
        th.Property("unconfirmed_count", th.IntegerType),
        th.Property("bounced_count", th.IntegerType),
        th.Property("junk_count", th.IntegerType),
        th.Property("created_at", th.DateTimeType),
    ).to_dict()

class CampaignsStream(mailerlitetapStream):
    name = "campaigns"
    path = "/campaigns"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
    ).to_dict()