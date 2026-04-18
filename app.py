import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def configure_logging() -> None:
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    app.logger.handlers.clear()
    app.logger.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s [%(filename)s:%(lineno)d] %(message)s"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(stream_handler)

    log_dir = os.getenv("LOG_DIR", "/var/log/webapp")
    try:
        os.makedirs(log_dir, exist_ok=True)
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, "application.log"),
            maxBytes=2 * 1024 * 1024,
            backupCount=5,
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)
    except Exception as exc:
        app.logger.warning("File logging could not be configured: %s", exc)

    app.logger.info("Logging initialized with level=%s", log_level)


configure_logging()


@app.before_request
def log_request_info():
    app.logger.info(
        "Incoming request method=%s path=%s remote_addr=%s",
        request.method,
        request.path,
        request.headers.get("X-Forwarded-For", request.remote_addr),
    )


@app.route("/")
def home():
    app.logger.info("Rendering home page")
    return render_template("index.html", app_name="Flask Elastic Beanstalk Demo")


@app.route("/health")
def health():
    app.logger.info("Health check requested")
    return jsonify({"status": "ok"}), 200


@app.route("/error")
def error_demo():
    app.logger.error("Intentional demo error triggered")
    return jsonify({"status": "error", "message": "intentional error for logging demo"}), 500


@app.errorhandler(Exception)
def handle_exception(exc):
    app.logger.exception("Unhandled exception: %s", exc)
    return jsonify({"status": "error", "message": "internal server error"}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
