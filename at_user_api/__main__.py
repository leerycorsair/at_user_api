import asyncio
from contextlib import asynccontextmanager

import uvicorn
from at_queue.core.session import ConnectionParameters
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from at_user_api.config.cli_args import parse_args
from at_user_api.config.rabbitmq import RabbitMQStore
from at_user_api.config.server import ServerConfigurator
from at_user_api.delivery.router import setup_routes
from at_user_api.providers.user import get_user_service
from at_user_api.worker.worker import AuthWorker


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_routes(app)

    rabbitmq_config = RabbitMQStore.get_rabbitmq_config()
    connection_parameters = ConnectionParameters(rabbitmq_config.url)

    auth_worker = AuthWorker(
        connection_parameters=connection_parameters,
        user_service=Depends(get_user_service),
    )

    await auth_worker.initialize()
    await auth_worker.register()

    task = asyncio.create_task(auth_worker.start())

    try:
        yield
    finally:
        task.cancel()


app = FastAPI(title="AT_USER", version="1.0.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    parse_args()
    server_config = ServerConfigurator().get_server_config()
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=server_config.port,
    )
