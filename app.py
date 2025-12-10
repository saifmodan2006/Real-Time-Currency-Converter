from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://open.er-api.com/v6/latest/"  # no API key required


def get_rates(base="USD"):
    """
    Fetch latest rates for a base currency.
    Returns dict of rates or None on error.
    """
    try:
        res = requests.get(API_URL + base, timeout=5)
        data = res.json()
        if data.get("result") == "success":
            return data.get("rates", {})
        else:
            return None
    except Exception as e:
        print("Error fetching rates:", e)
        return None


@app.route("/", methods=["GET"])
def index():
    # Get list of available currencies (keys of 'rates')
    rates = get_rates("USD") or {}
    currencies = sorted(rates.keys())
    # Pass to template
    return render_template(
        "index.html",
        currencies=currencies,
        default_from="USD",
        default_to="INR"
    )


@app.route("/convert", methods=["POST"])
def convert():
    """
    AJAX endpoint for real-time conversion.
    Expects JSON: {from_currency, to_currency, amount}
    """
    data = request.get_json()
    from_cur = data.get("from_currency")
    to_cur = data.get("to_currency")
    amount = data.get("amount")

    # Basic validation
    try:
        amount = float(amount)
        if amount < 0:
            return jsonify({"error": "Amount must be positive."}), 400
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid amount."}), 400

    # Get rates for base = from_cur
    rates = get_rates(from_cur)
    if not rates:
        return jsonify({"error": "Failed to fetch rates. Try again later."}), 500

    if to_cur not in rates:
        return jsonify({"error": "Invalid target currency."}), 400

    rate = rates[to_cur]
    converted = amount * rate

    return jsonify({
        "from_currency": from_cur,
        "to_currency": to_cur,
        "amount": amount,
        "rate": rate,
        "converted_amount": converted
    })


if __name__ == "__main__":
    app.run(debug=True)
