from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_document_api_v1_dubo_documentation_put import BodyUpdateDocumentApiV1DuboDocumentationPut
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    multipart_data: BodyUpdateDocumentApiV1DuboDocumentationPut,
    data_source_documentation_id: str,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["data_source_documentation_id"] = data_source_documentation_id

    params["shingle_length"] = shingle_length

    params["step"] = step

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "put",
        "url": "/api/v1/dubo/documentation",
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, bool]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(bool, response.json())
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
) -> Response[Union[HTTPValidationError, bool]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: BodyUpdateDocumentApiV1DuboDocumentationPut,
    data_source_documentation_id: str,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
) -> Response[Union[HTTPValidationError, bool]]:
    """Update Document

    Args:
        data_source_documentation_id (str):
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        multipart_data (BodyUpdateDocumentApiV1DuboDocumentationPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, bool]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        data_source_documentation_id=data_source_documentation_id,
        shingle_length=shingle_length,
        step=step,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: BodyUpdateDocumentApiV1DuboDocumentationPut,
    data_source_documentation_id: str,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
) -> Optional[Union[HTTPValidationError, bool]]:
    """Update Document

    Args:
        data_source_documentation_id (str):
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        multipart_data (BodyUpdateDocumentApiV1DuboDocumentationPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, bool]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        data_source_documentation_id=data_source_documentation_id,
        shingle_length=shingle_length,
        step=step,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: BodyUpdateDocumentApiV1DuboDocumentationPut,
    data_source_documentation_id: str,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
) -> Response[Union[HTTPValidationError, bool]]:
    """Update Document

    Args:
        data_source_documentation_id (str):
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        multipart_data (BodyUpdateDocumentApiV1DuboDocumentationPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, bool]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        data_source_documentation_id=data_source_documentation_id,
        shingle_length=shingle_length,
        step=step,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: BodyUpdateDocumentApiV1DuboDocumentationPut,
    data_source_documentation_id: str,
    shingle_length: Union[Unset, int] = 1000,
    step: Union[Unset, int] = 500,
) -> Optional[Union[HTTPValidationError, bool]]:
    """Update Document

    Args:
        data_source_documentation_id (str):
        shingle_length (Union[Unset, int]):  Default: 1000.
        step (Union[Unset, int]):  Default: 500.
        multipart_data (BodyUpdateDocumentApiV1DuboDocumentationPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, bool]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            data_source_documentation_id=data_source_documentation_id,
            shingle_length=shingle_length,
            step=step,
        )
    ).parsed
