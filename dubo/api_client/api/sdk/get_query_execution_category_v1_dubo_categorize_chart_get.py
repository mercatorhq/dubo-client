from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    text_input: Union[Unset, str] = UNSET,
    column_names: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["text_input"] = text_input

    json_column_names: Union[Unset, List[str]] = UNSET
    if not isinstance(column_names, Unset):
        json_column_names = column_names

    params["column_names"] = json_column_names

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/dubo/categorize-chart",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
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
) -> Response[Union[HTTPValidationError, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    text_input: Union[Unset, str] = UNSET,
    column_names: Union[Unset, List[str]] = UNSET,
) -> Response[Union[HTTPValidationError, str]]:
    """Get Query Execution Category

    Args:
        text_input (Union[Unset, str]): Text input to categorize
        column_names (Union[Unset, List[str]]): Column names to use for categorization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        text_input=text_input,
        column_names=column_names,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    text_input: Union[Unset, str] = UNSET,
    column_names: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[HTTPValidationError, str]]:
    """Get Query Execution Category

    Args:
        text_input (Union[Unset, str]): Text input to categorize
        column_names (Union[Unset, List[str]]): Column names to use for categorization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, str]
    """

    return sync_detailed(
        client=client,
        text_input=text_input,
        column_names=column_names,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    text_input: Union[Unset, str] = UNSET,
    column_names: Union[Unset, List[str]] = UNSET,
) -> Response[Union[HTTPValidationError, str]]:
    """Get Query Execution Category

    Args:
        text_input (Union[Unset, str]): Text input to categorize
        column_names (Union[Unset, List[str]]): Column names to use for categorization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        text_input=text_input,
        column_names=column_names,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    text_input: Union[Unset, str] = UNSET,
    column_names: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[HTTPValidationError, str]]:
    """Get Query Execution Category

    Args:
        text_input (Union[Unset, str]): Text input to categorize
        column_names (Union[Unset, List[str]]): Column names to use for categorization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            text_input=text_input,
            column_names=column_names,
        )
    ).parsed
