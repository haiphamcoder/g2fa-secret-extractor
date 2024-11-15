from base64 import b32encode
from .decoder import decode_data
from .utils import parse_uri

def extract_secret_key(uri: str):
    """
    Trích xuất và hiển thị secret key từ URI Google Authenticator.
    """
    # Tách phần dữ liệu base64 từ URI
    data = parse_uri(uri)

    # Giải mã dữ liệu base64
    payload = decode_data(data)

    # Hiển thị thông tin
    for otp in payload.otp_parameters:
        # Chuyển đổi secret key sang base32
        secret_key = b32encode(otp.secret).decode("utf-8").replace("=", "")
        name = otp.name
        issuer = otp.issuer
        algorithm = otp.algorithm
        digits = otp.digits
        otp_type = otp.type
        counter = otp.counter
        
        print(f"Issuer: {issuer}")
        print(f"Name: {name}")
        print(f"Secret Key: {secret_key}")
        print(f"Algorithm: {algorithm}")
        print(f"Digits: {digits}")
        print(f"Type: {otp_type}")
        print(f"Counter: {counter}")
        print()
