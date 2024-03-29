import logging
from rich.logging import RichHandler
from rich.prompt import Prompt as prompt
from rich.prompt import Confirm as confirm
from rich.console import Console
import requests
import httpx

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(markup=True, rich_tracebacks=True)],
)

log = logging.getLogger("rich")
console = Console()
# Declare constants
DEFAULT_SALT = "cookie-session"
DEFAULT_COOKIE_NAME = "session"
DEFAULT_USER_AGENT = "Vial/1.0"
BUFFER = 4096
FETCHED_COOKIE = None
CONFIG = None
a_web_session = httpx.AsyncClient()
web_session = requests.Session()
