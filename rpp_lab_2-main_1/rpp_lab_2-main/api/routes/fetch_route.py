from flask import Blueprint, request, jsonify, abort

from api.dict import tax_dict

bp = Blueprint('fetch_route', __name__)


@bp.route("/v1/fetch/taxes", methods=['GET'])
def fetch_taxes():
    return jsonify(tax_dict), 200


@bp.route('/v1/fetch/tax', methods=['GET'])
def fetch_tax():
    code = request.args.get('code')
    if code in tax_dict:
        message = {"Tax": tax_dict[code]}
        return jsonify(message), 200
    else:
        abort(400)


@bp.route('/v1/fetch/calc', methods=['GET'])
def fetch_calc():
    code = request.args.get('code')
    cadastral_value = int(request.args.get('cadastral_value'))
    month_of_ownership = int(request.args.get('month_of_ownership'))
    if code in tax_dict:
        tax = int(tax_dict[code])
        tax_for_year = (cadastral_value * tax * month_of_ownership)/12
        message = {"Tax amount for the year": tax_for_year}
        return jsonify(message), 200
    else:
        abort(400)
