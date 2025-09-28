import functools
from loguru import logger

def deprecated(message: str):
    """Deprecated decorator - logs a warning with winlog on each call."""
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.warning(f"DEPRECATED: {func.__name__}() is deprecated. {message}")
            return func(*args, **kwargs)
        return wrapper
    
    return decorator