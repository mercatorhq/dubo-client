from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_documentation_api_v1_dubo_documentation_post import (
    BodyCreateDocumentationApiV1DuboDocumentationPost,
)
from ...models.data_source_document import DataSourceDocument
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    multipart_data: BodyCreateDocumentationApiV1DuboDocumentationPost,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
    x_dubo_key: str,
) -> Dict[str, Any]:
    headers = {}
    headers["x-dubo-key"] = x_dubo_key

    params: Dict[str, Any] = {}
    params["shingle_length"] = shingle_length

    params["step"] = step

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/api/v1/dubo/documentation",
        "files": multipart_multipart_data,
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DataSourceDocument, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataSourceDocument.from_dict(response.json())

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
) -> Response[Union[DataSourceDocument, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyCreateDocumentationApiV1DuboDocumentationPost,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
    x_dubo_key: str,
) -> Response[Union[DataSourceDocument, HTTPValidationError]]:
    """Create Documentation

    Args:
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        x_dubo_key (str):
        multipart_data (BodyCreateDocumentationApiV1DuboDocumentationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSourceDocument, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        shingle_length=shingle_length,
        step=step,
        x_dubo_key=x_dubo_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyCreateDocumentationApiV1DuboDocumentationPost,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
    x_dubo_key: str,
) -> Optional[Union[DataSourceDocument, HTTPValidationError]]:
    """Create Documentation

    Args:
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        x_dubo_key (str):
        multipart_data (BodyCreateDocumentationApiV1DuboDocumentationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataSourceDocument, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        shingle_length=shingle_length,
        step=step,
        x_dubo_key=x_dubo_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyCreateDocumentationApiV1DuboDocumentationPost,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
    x_dubo_key: str,
) -> Response[Union[DataSourceDocument, HTTPValidationError]]:
    """Create Documentation

    Args:
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        x_dubo_key (str):
        multipart_data (BodyCreateDocumentationApiV1DuboDocumentationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSourceDocument, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        shingle_length=shingle_length,
        step=step,
        x_dubo_key=x_dubo_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: BodyCreateDocumentationApiV1DuboDocumentationPost,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
    x_dubo_key: str,
) -> Optional[Union[DataSourceDocument, HTTPValidationError]]:
    """Create Documentation

    Args:
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        x_dubo_key (str):
        multipart_data (BodyCreateDocumentationApiV1DuboDocumentationPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataSourceDocument, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            shingle_length=shingle_length,
            step=step,
            x_dubo_key=x_dubo_key,
        )
    ).parsed
