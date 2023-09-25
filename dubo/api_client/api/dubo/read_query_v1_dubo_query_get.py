from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_read_query_v1_dubo_query_get import BodyReadQueryV1DuboQueryGet
from ...models.query_response import QueryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: BodyReadQueryV1DuboQueryGet,
    query: Union[Unset, None, str] = UNSET,
    user_query: Union[Unset, None, str] = UNSET,
    schemas: Union[Unset, None, List[str]] = UNSET,
    descriptions: Union[Unset, None, List[str]] = UNSET,
    data_header: Union[Unset, None, List[str]] = UNSET,
    macros: Union[Unset, None, bool] = False,
    fast: Union[Unset, None, bool] = False,
    model: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["query"] = query

    params["user_query"] = user_query

    json_schemas: Union[Unset, None, List[str]] = UNSET
    if not isinstance(schemas, Unset):
        if schemas is None:
            json_schemas = None
        else:
            json_schemas = schemas

    params["schemas"] = json_schemas

    json_descriptions: Union[Unset, None, List[str]] = UNSET
    if not isinstance(descriptions, Unset):
        if descriptions is None:
            json_descriptions = None
        else:
            json_descriptions = descriptions

    params["descriptions"] = json_descriptions

    json_data_header: Union[Unset, None, List[str]] = UNSET
    if not isinstance(data_header, Unset):
        if data_header is None:
            json_data_header = None
        else:
            json_data_header = data_header

    params["data_header"] = json_data_header

    params["macros"] = macros

    params["fast"] = fast

    params["model"] = model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "get",
        "url": "/v1/dubo/query",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, QueryResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, QueryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BodyReadQueryV1DuboQueryGet,
    query: Union[Unset, None, str] = UNSET,
    user_query: Union[Unset, None, str] = UNSET,
    schemas: Union[Unset, None, List[str]] = UNSET,
    descriptions: Union[Unset, None, List[str]] = UNSET,
    data_header: Union[Unset, None, List[str]] = UNSET,
    macros: Union[Unset, None, bool] = False,
    fast: Union[Unset, None, bool] = False,
    model: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, QueryResponse]]:
    """Convert text to SQL

    Args:
        query (Union[Unset, None, str]): The question to answer
        user_query (Union[Unset, None, str]): The question to answer
        schemas (Union[Unset, None, List[str]]): The table schema(s) to use
        descriptions (Union[Unset, None, List[str]]): The table description(s) to use
        data_header (Union[Unset, None, List[str]]): The data header to use
        macros (Union[Unset, None, bool]): Enable or disable macros
        fast (Union[Unset, None, bool]): Use faster less accurate model
        model (Union[Unset, None, str]): Model to use
        json_body (BodyReadQueryV1DuboQueryGet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueryResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        query=query,
        user_query=user_query,
        schemas=schemas,
        descriptions=descriptions,
        data_header=data_header,
        macros=macros,
        fast=fast,
        model=model,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BodyReadQueryV1DuboQueryGet,
    query: Union[Unset, None, str] = UNSET,
    user_query: Union[Unset, None, str] = UNSET,
    schemas: Union[Unset, None, List[str]] = UNSET,
    descriptions: Union[Unset, None, List[str]] = UNSET,
    data_header: Union[Unset, None, List[str]] = UNSET,
    macros: Union[Unset, None, bool] = False,
    fast: Union[Unset, None, bool] = False,
    model: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, QueryResponse]]:
    """Convert text to SQL

    Args:
        query (Union[Unset, None, str]): The question to answer
        user_query (Union[Unset, None, str]): The question to answer
        schemas (Union[Unset, None, List[str]]): The table schema(s) to use
        descriptions (Union[Unset, None, List[str]]): The table description(s) to use
        data_header (Union[Unset, None, List[str]]): The data header to use
        macros (Union[Unset, None, bool]): Enable or disable macros
        fast (Union[Unset, None, bool]): Use faster less accurate model
        model (Union[Unset, None, str]): Model to use
        json_body (BodyReadQueryV1DuboQueryGet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueryResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        query=query,
        user_query=user_query,
        schemas=schemas,
        descriptions=descriptions,
        data_header=data_header,
        macros=macros,
        fast=fast,
        model=model,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BodyReadQueryV1DuboQueryGet,
    query: Union[Unset, None, str] = UNSET,
    user_query: Union[Unset, None, str] = UNSET,
    schemas: Union[Unset, None, List[str]] = UNSET,
    descriptions: Union[Unset, None, List[str]] = UNSET,
    data_header: Union[Unset, None, List[str]] = UNSET,
    macros: Union[Unset, None, bool] = False,
    fast: Union[Unset, None, bool] = False,
    model: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, QueryResponse]]:
    """Convert text to SQL

    Args:
        query (Union[Unset, None, str]): The question to answer
        user_query (Union[Unset, None, str]): The question to answer
        schemas (Union[Unset, None, List[str]]): The table schema(s) to use
        descriptions (Union[Unset, None, List[str]]): The table description(s) to use
        data_header (Union[Unset, None, List[str]]): The data header to use
        macros (Union[Unset, None, bool]): Enable or disable macros
        fast (Union[Unset, None, bool]): Use faster less accurate model
        model (Union[Unset, None, str]): Model to use
        json_body (BodyReadQueryV1DuboQueryGet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueryResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        query=query,
        user_query=user_query,
        schemas=schemas,
        descriptions=descriptions,
        data_header=data_header,
        macros=macros,
        fast=fast,
        model=model,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: BodyReadQueryV1DuboQueryGet,
    query: Union[Unset, None, str] = UNSET,
    user_query: Union[Unset, None, str] = UNSET,
    schemas: Union[Unset, None, List[str]] = UNSET,
    descriptions: Union[Unset, None, List[str]] = UNSET,
    data_header: Union[Unset, None, List[str]] = UNSET,
    macros: Union[Unset, None, bool] = False,
    fast: Union[Unset, None, bool] = False,
    model: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, QueryResponse]]:
    """Convert text to SQL

    Args:
        query (Union[Unset, None, str]): The question to answer
        user_query (Union[Unset, None, str]): The question to answer
        schemas (Union[Unset, None, List[str]]): The table schema(s) to use
        descriptions (Union[Unset, None, List[str]]): The table description(s) to use
        data_header (Union[Unset, None, List[str]]): The data header to use
        macros (Union[Unset, None, bool]): Enable or disable macros
        fast (Union[Unset, None, bool]): Use faster less accurate model
        model (Union[Unset, None, str]): Model to use
        json_body (BodyReadQueryV1DuboQueryGet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            query=query,
            user_query=user_query,
            schemas=schemas,
            descriptions=descriptions,
            data_header=data_header,
            macros=macros,
            fast=fast,
            model=model,
        )
    ).parsed
