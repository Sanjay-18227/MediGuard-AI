from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Root endpoint that returns a short status and attempts to detect local modules."""
    info = {
        "project": "MediGuard-AI",
        "status": "ok",
        "message": "This is a placeholder Flask app added to make the repository runnable. Replace with your real entrypoint.",
    }

    # Try to detect local project modules to help with incremental restores
    try:
        import components  # noqa: F401
        info["components"] = "found"
    except Exception as e:
        info["components"] = f"not found: {e.__class__.__name__}"

    try:
        import services  # noqa: F401
        info["services"] = "found"
    except Exception as e:
        info["services"] = f"not found: {e.__class__.__name__}"

    return jsonify(info)


@app.route('/health')
def health():
    return jsonify({"status": "healthy"})


if __name__ == '__main__':
    # Use a sensible default port; change as needed.
    app.run(host='0.0.0.0', port=5000, debug=True)
