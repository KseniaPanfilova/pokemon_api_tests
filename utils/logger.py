import logging
import json
import requests
import allure


def decode_body(body):
    """Безопасно декодирует тело запроса/ответа."""
    if body is None:
        return None
    if isinstance(body, bytes):
        try:
            return body.decode('utf-8')
        except UnicodeDecodeError:
            return "<binary body>"
    return str(body)


def safe_json_pretty(response: requests.Response):
    """Пытается красиво отформатировать JSON, иначе возвращает текст."""
    try:
        parsed = response.json()
        return json.dumps(parsed, indent=4, ensure_ascii=False)
    except ValueError:
        return response.text


def log_response(response: requests.Response, attach_to_allure: bool = True):
    """Логирует HTTP запрос и ответ, добавляет в Allure вложение."""

    method = response.request.method
    url = response.request.url
    status = response.status_code
    req_body = decode_body(getattr(response.request, "body", None))
    formatted_response = safe_json_pretty(response)

    # Логирование запроса
    logging.info(f'➡️ Request: {method} {url}')
    if method in {"POST", "PUT", "PATCH"} and req_body:
        logging.debug(f'📤 Request body: {req_body}')

    # Логирование ответа с уровнем в зависимости от статуса
    if status < 400:
        logging.info(f'⬅️ Status Code: {status}')
        logging.debug(f'📥 Response body:\n{formatted_response}')
    elif status < 500:
        logging.warning(f'⚠️ Client error: {status}')
        logging.debug(f'⚠️ Response body:\n{formatted_response}')
    else:
        logging.error(f'❌ Server error: {status}')
        logging.debug(f'❌ Response body:\n{formatted_response}')

    # Вложение в Allure
    if attach_to_allure:
        try:
            allure.attach(
                body=(
                    f"{method} {url}\n\n"
                    f"Request body:\n{req_body}\n\n"
                    f"Status code: {status}\n\n"
                    f"Response body:\n{formatted_response}"
                ),
                name="HTTP exchange",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception as e:
            logging.warning(f"⚠️ Failed to attach HTTP exchange to Allure: {e}")
