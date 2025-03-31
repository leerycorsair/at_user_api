#!/bin/bash

# alembic upgrade head

uvicorn at_user_api.application:app --host 0.0.0.0 --port $SERVER_PORT
