from fastapi import APIRouter

from src.api import try_except_response, build_message_susccess
from src.api.uri import URI

check_services_router = APIRouter()


@check_services_router.get(URI.PING)
@try_except_response
def check_services():
    return build_message_susccess("request full successes!!!")
