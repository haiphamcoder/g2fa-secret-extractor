import re
from urllib.parse import unquote

# Mẫu regex để nhận diện và tách phần dữ liệu base64
URI_REGEX = r"^otpauth-migration://offline\?data=([A-Za-z0-9\-_+/=]*)$"

def parse_uri(uri: str) -> str:
    """
    Chuẩn hóa và tách phần dữ liệu base64 từ URI Google Authenticator.
    """
    # Giải mã URL (URL decode)
    decoded_uri = unquote(uri)

    # Kiểm tra định dạng URI và tách phần dữ liệu base64
    match = re.match(URI_REGEX, decoded_uri)
    if not match:
        raise ValueError(f"URI không đúng định dạng: {decoded_uri}\n"
                         f"Vui lòng đảm bảo URI có dạng: otpauth-migration://offline?data=<base64>")
    
    # Trả về phần dữ liệu base64
    return match.group(1)
