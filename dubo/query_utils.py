import time
from typing import Union

from dubo.api_client import AuthenticatedClient, Client
from dubo.api_client.api.enterprise import (
    ask_dispatch_api_v1_dubo_query_generate_post,
    ask_poll_api_v1_dubo_query_retrieve_get,
)
from dubo.api_client.models import *
from dubo.common import DuboException

from dubo.config import get_dubo_key
from dubo.entities import DataResult


def dispatch_query(
        client: Union[AuthenticatedClient, Client],
        query: str,
        fast: bool = False) -> str:
    """
    Dispatch the query and get a tracking_id.
    """
    api_key = get_dubo_key()
    json_body = CreateApiQuery(
        query_text=query,
        fast=fast,
    )

    res = ask_dispatch_api_v1_dubo_query_generate_post.sync(
        client=client,
        x_dubo_key=api_key,
        json_body=json_body,
    )
    return res.id


def retrieve_result(
        client: Union[AuthenticatedClient, Client],
        tracking_id: str) -> DataResult:
    """
    Poll for the result using the provided tracking_id.
    """
    delay = 0.1
    max_delay = 10
    api_key = get_dubo_key()
    while True:
        res = ask_poll_api_v1_dubo_query_retrieve_get.sync(
            client=client,
            x_dubo_key=api_key,
            dispatch_id=tracking_id,
        )
        if res.status == QueryStatus.SUCCESS:
            return DataResult(
                id=res.id,
                query_text=res.query_text,
                status=res.status,
                results_set=[
                    item.additional_properties for item in res.results_set
                ],
                row_count=res.row_count,
            )
        elif res.status == QueryStatus.FAILED:
            raise DuboException(res["error"])
        else:
            time.sleep(delay)
            delay = min(delay * 2, max_delay)


def dispatch_and_retrieve(
        client: Union[AuthenticatedClient, Client],
        query: str,
        fast: bool = False) -> DataResult:
    """
    Convenience function to generate the query and retrieve the result.
    """
    tracking_id = dispatch_query(client, query, fast)
    return retrieve_result(client, tracking_id)
