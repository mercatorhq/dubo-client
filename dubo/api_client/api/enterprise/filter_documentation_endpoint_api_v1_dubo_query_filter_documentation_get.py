from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.page import Page
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_query: str,
    page_number: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
    x_dubo_key: str,
) -> Dict[str, Any]:
    headers = {}
    headers["x-dubo-key"] = x_dubo_key

    params: Dict[str, Any] = {}
    params["user_query"] = user_query

    params["page_number"] = page_number

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v1/dubo/query/filter-documentation",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Page]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Page.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Page]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    user_query: str,
    page_number: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
    x_dubo_key: str,
) -> Response[Union[HTTPValidationError, Page]]:
    """Filter Documentation Endpoint

    Args:
        user_query (str):
        page_number (Union[Unset, None, int]): Page number Default: 1.
        page_size (Union[Unset, None, int]): Page size Default: 25.
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Page]]
    """

    kwargs = _get_kwargs(
        user_query=user_query,
        page_number=page_number,
        page_size=page_size,
        x_dubo_key=x_dubo_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    user_query: str,
    page_number: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
    x_dubo_key: str,
) -> Optional[Union[HTTPValidationError, Page]]:
    """Filter Documentation Endpoint

    Args:
        user_query (str):
        page_number (Union[Unset, None, int]): Page number Default: 1.
        page_size (Union[Unset, None, int]): Page size Default: 25.
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Page]
    """

    return sync_detailed(
        client=client,
        user_query=user_query,
        page_number=page_number,
        page_size=page_size,
        x_dubo_key=x_dubo_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    user_query: str,
    page_number: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
    x_dubo_key: str,
) -> Response[Union[HTTPValidationError, Page]]:
    """Filter Documentation Endpoint

    Args:
        user_query (str):
        page_number (Union[Unset, None, int]): Page number Default: 1.
        page_size (Union[Unset, None, int]): Page size Default: 25.
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Page]]
    """

    kwargs = _get_kwargs(
        user_query=user_query,
        page_number=page_number,
        page_size=page_size,
        x_dubo_key=x_dubo_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    user_query: str,
    page_number: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = 25,
    x_dubo_key: str,
) -> Optional[Union[HTTPValidationError, Page]]:
    """Filter Documentation Endpoint

    Args:
        user_query (str):
        page_number (Union[Unset, None, int]): Page number Default: 1.
        page_size (Union[Unset, None, int]): Page size Default: 25.
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Page]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_query=user_query,
            page_number=page_number,
            page_size=page_size,
            x_dubo_key=x_dubo_key,
        )
    ).parsed