from datetime import timezone, timedelta
from flask import jsonify
from typing import Any

tw_zone = timezone(timedelta(hours=8))
def get_tw_zone():
    return tw_zone

def api_response(success:bool=True, message:str="Success", data:Any=None, code:int=200, errors:str|None=None):
    response: dict[str, Any] = {
        "success": success,
        "code": code,
        "message": message,
        "data": data if data is not None else {},
    }
    if errors:
        response["errors"] = errors
    
    return jsonify(response), code