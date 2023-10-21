from api.tax import tax_dict
from flask import Blueprint, request, jsonify, abort

bp = Blueprint('update_route', __name__)


@bp.route("/v1/update/tax", methods=['POST'])
def update_tax():
    data = request.get_json()
    code = data['code']
    tax = data['tax']
    if code in tax_dict:
        tax_dict[code] = tax
        message = {'message': f'Tax with code updated'}
        return jsonify(message), 201
    else:
        abort(400)
