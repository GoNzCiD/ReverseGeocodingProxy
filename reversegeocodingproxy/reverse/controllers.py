import os

import requests
from flask import jsonify, request, Blueprint, current_app

from reversegeocodingproxy.cache import cache

reverse = Blueprint('reverse', __name__)


@reverse.route("/", methods=['GET'])
@cache.cached(timeout=3600, query_string=True)
def balance():
    local_server = os.getenv("LOCAL_SERVER", current_app.config.get('LOCAL_SERVER'))
    remote_server = os.getenv("REMOTE_SERVER", current_app.config.get('REMOTE_SERVER'))
    parameters = request.args

    # Try local geocoding server
    try:
        local_response = requests.get(url=local_server, params=parameters).json()
        result = local_response
    except Exception as local_ex:
        local_response = {"error": str(local_ex)}

    # If error on local, use remote geocoding server
    if local_response.get("error"):
        try:
            result = requests.get(url=remote_server, params=parameters).json()
        except Exception as remote_ex:
            error_message = "Local: '{}' - Remote: '{}'".format(local_response.get("error"), remote_ex)
            result = jsonify({"error": error_message})

    return result
