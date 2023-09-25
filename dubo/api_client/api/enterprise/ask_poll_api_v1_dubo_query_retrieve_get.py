from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ask_dispatch_response import AskDispatchResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    dispatch_id: str,
    x_dubo_key: str,
) -> Dict[str, Any]:
    headers = {}
    headers["x-dubo-key"] = x_dubo_key

    params: Dict[str, Any] = {}
    params["dispatch_id"] = dispatch_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v1/dubo/query/retrieve",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AskDispatchResponse, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AskDispatchResponse.from_dict(response.json())

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
) -> Response[Union[AskDispatchResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dispatch_id: str,
    x_dubo_key: str,
) -> Response[Union[AskDispatchResponse, HTTPValidationError]]:
    """Ask Poll

    Args:
        dispatch_id (str):
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AskDispatchResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        dispatch_id=dispatch_id,
        x_dubo_key=x_dubo_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    dispatch_id: str,
    x_dubo_key: str,
) -> Optional[Union[AskDispatchResponse, HTTPValidationError]]:
    """Ask Poll

    Args:
        dispatch_id (str):
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AskDispatchResponse, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        dispatch_id=dispatch_id,
        x_dubo_key=x_dubo_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dispatch_id: str,
    x_dubo_key: str,
) -> Response[Union[AskDispatchResponse, HTTPValidationError]]:
    """Ask Poll

    Args:
        dispatch_id (str):
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AskDispatchResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        dispatch_id=dispatch_id,
        x_dubo_key=x_dubo_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    dispatch_id: str,
    x_dubo_key: str,
) -> Optional[Union[AskDispatchResponse, HTTPValidationError]]:
    """Ask Poll

    Args:
        dispatch_id (str):
        x_dubo_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AskDispatchResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            dispatch_id=dispatch_id,
            x_dubo_key=x_dubo_key,
        )
    ).parsed
