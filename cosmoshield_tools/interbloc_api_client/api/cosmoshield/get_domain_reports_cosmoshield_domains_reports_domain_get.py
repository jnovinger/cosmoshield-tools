from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    domain: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/cosmoshield/domains/reports/{domain}".format(client.base_url, domain=domain)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    domain: str,
    *,
    client: Client,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Domain Reports

    Args:
        domain (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        domain=domain,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    domain: str,
    *,
    client: Client,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Domain Reports

    Args:
        domain (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        domain=domain,
        client=client,
    ).parsed


async def asyncio_detailed(
    domain: str,
    *,
    client: Client,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Domain Reports

    Args:
        domain (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        domain=domain,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    domain: str,
    *,
    client: Client,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Domain Reports

    Args:
        domain (str):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            domain=domain,
            client=client,
        )
    ).parsed
