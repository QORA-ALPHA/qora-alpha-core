from loguru import logger

logger.add("qora_alpha.log", rotation="10 MB", retention="10 days", level="INFO")
