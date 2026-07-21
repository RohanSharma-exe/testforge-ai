from loguru import logger

from config.settings import LOG_DIR

logger.remove()

logger.add(
    LOG_DIR / "testforge.log",
    level="INFO",
    rotation="5 MB",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)

log = logger