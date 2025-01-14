from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dubo_chart_query import DuboChartQuery
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: DuboChartQuery,
    num_charts: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["num_charts"] = num_charts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v1/dubo/chart",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, List[Any]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[Any], response.json())

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
) -> Response[Union[HTTPValidationError, List[Any]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DuboChartQuery,
    num_charts: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, List[Any]]]:
    """Create Dubo Chart

    Args:
        num_charts (Union[Unset, int]): The number of charts to generate Default: 1.
        json_body (DuboChartQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[Any]]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        num_charts=num_charts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DuboChartQuery,
    num_charts: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, List[Any]]]:
    """Create Dubo Chart

    Args:
        num_charts (Union[Unset, int]): The number of charts to generate Default: 1.
        json_body (DuboChartQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[Any]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        num_charts=num_charts,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DuboChartQuery,
    num_charts: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, List[Any]]]:
    """Create Dubo Chart

    Args:
        num_charts (Union[Unset, int]): The number of charts to generate Default: 1.
        json_body (DuboChartQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[Any]]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        num_charts=num_charts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: DuboChartQuery,
    num_charts: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, List[Any]]]:
    """Create Dubo Chart

    Args:
        num_charts (Union[Unset, int]): The number of charts to generate Default: 1.
        json_body (DuboChartQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[Any]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            num_charts=num_charts,
        )
    ).parsed
