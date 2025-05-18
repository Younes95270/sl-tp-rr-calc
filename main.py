from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signal', methods=['POST'])
def generate_signal():
    data = request.get_json()

    entry = float(data.get("entry"))
    atr = float(data.get("atr"))
    ema20 = float(data.get("ema20"))
    ema50 = float(data.get("ema50"))
    ema200 = float(data.get("ema200"))
    macd_histogram = float(data.get("macd_histogram"))

    sl = round(entry - (atr * 1.5), 2)
    tp = round(entry + (atr * 2.5), 2)
    rr = round((tp - entry) / (entry - sl), 2)

    if ema20 > ema50 > ema200 and macd_histogram > 0:
        trend = "Bullish"
    elif ema20 < ema50 < ema200 and macd_histogram < 0:
        trend = "Bearish"
    else:
        trend = "Neutral"

    return jsonify({
        "sl": sl,
        "tp": tp,
        "rr": rr,
        "trend": trend
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
