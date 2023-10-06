from flask import Blueprint, request, jsonify, abort

from api.dict import tax_dict

bp = Blueprint('add_route', __name__)


@bp.route("/v1/add/tax", methods=['POST'])
def add_tax():
    data = request.get_json()
    code = data['code']
    tax = data['tax']
    if code in tax_dict:
        abort(400)
    else:
        tax_dict[code] = tax
        message = {'message': 'Tax with code added'}
        return jsonify(message), 201
