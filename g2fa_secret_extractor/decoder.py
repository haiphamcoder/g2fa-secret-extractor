import base64
from .protobuf.otpauth_migration_pb2 import Payload

def decode_data(data: str):
    """
    Giải mã dữ liệu base64 và phân tích cú pháp protobuf.
    """
    try:
        # Thêm padding nếu thiếu
        missing_padding = len(data) % 4
        if missing_padding:
            data += "=" * (4 - missing_padding)

        # Giải mã base64
        decoded_bytes = base64.b64decode(data)

        # Phân tích cú pháp protobuf
        payload = Payload()
        payload.ParseFromString(decoded_bytes)
        return payload
    except Exception as e:
        raise ValueError(f"Lỗi giải mã: {e}")
