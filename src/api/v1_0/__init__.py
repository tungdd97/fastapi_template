from src.api import app
from src.api.v1_0.check_services import check_services_router

api_prefix = "/api/v1.0"

app.include_router(router=check_services_router, prefix=api_prefix)

