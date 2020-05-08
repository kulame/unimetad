from aiohttp import ClientSession
from loguru import logger

CLIENT_SESSION: ClientSession


async def setup_session() -> None:
    global CLIENT_SESSION
    logger.info("Setting up global aiohttp.ClientSession.")
    CLIENT_SESSION = ClientSession()


async def teardown_session() -> None:
    global CLIENT_SESSION
    logger.info("Closing global aiohttp.ClientSession.")
    await CLIENT_SESSION.close()
