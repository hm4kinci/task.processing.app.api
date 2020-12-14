import asyncio
import aiohttp
from copy import  deepcopy


async def fetch(session, base_url, request, fields):
    params = [(key, request.get(key,'')) for key in fields]
    async with session.get(base_url, params=params) as response:
        response = await response.json()
        result = deepcopy(request)
        if response.get('success'):
            result['response'] = response.get('data')
        else:
            result['response'] = []
        return result


async def fetch_all(base_url, requests, fields):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for request in requests:
            tasks.append(
                fetch(
                    session,
                    base_url,
                    request,
                    fields
                )
            )

        responses = await asyncio.gather(*tasks, return_exceptions=False)
        return responses


def run(base_url, requests, fields):
    responses = asyncio.run(fetch_all(base_url, requests, fields))
    return responses
