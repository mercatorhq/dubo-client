import time
from http import HTTPStatus

from dubo.api_client import AuthenticatedClient
from dubo.api_client.api.enterprise import (
    ask_dispatch_api_v1_dubo_query_generate_post,
    ask_poll_api_v1_dubo_query_retrieve_get,
)
from dubo.api_client.models import *
from dubo.common import DuboException
from dubo.config import RETRIEVE_RESULT_MAX_DELAY
from dubo.entities import DataResult


def dispatch_query(
    client: AuthenticatedClient, query: str, fast: bool = False
) -> str:
    """
    Dispatch the query and get a tracking_id.
    """

    json_body = CreateApiQuery(
        query_text=query,
        fast=fast,
    )

    res = ask_dispatch_api_v1_dubo_query_generate_post.sync_detailed(
        client=client,
        json_body=json_body,
    )
    if res.status_code != 200:
        raise DuboException(
            f"Failed to dispatch query, status code: {res.status_code}, content: {res.content.decode('utf-8')}"
        )
    res = res.parsed

    if not res or not res.id:
        raise DuboException("Failed to dispatch query.")
    return res.id


def retrieve_result(
    client: AuthenticatedClient, tracking_id: str
) -> DataResult:
    """
    Poll for the result using the provided tracking_id.
    """
    delay = 0.1
    max_delay = RETRIEVE_RESULT_MAX_DELAY
    while True:
        res = ask_poll_api_v1_dubo_query_retrieve_get.sync(
            client=client,
            dispatch_id=tracking_id,
        )
        if res.status == QueryStatus.SUCCESS:
            return DataResult(
                id=res.id,
                query_text=res.query_text,
                status=res.status,
                results_set=[item.additional_properties for item in res.results_set],
                row_count=res.row_count,
            )
        elif res.status == QueryStatus.FAILED:
            raise DuboException(res["error"])
        else:
            time.sleep(delay)
            delay = min(delay * 2, max_delay)


def dispatch_and_retrieve(
    client: AuthenticatedClient, query: str, fast: bool = False
) -> DataResult:
    """
    Convenience function to generate the query and retrieve the result.
    """
    tracking_id = dispatch_query(client, query, fast)
    return retrieve_result(client, tracking_id)
