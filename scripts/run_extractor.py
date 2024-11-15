import sys
from g2fa_secret_extractor.extractor import extract_secret_key

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_extractor.py <uri>")
        sys.exit(1)

    uri = sys.argv[1]
    try:
        secret_key = extract_secret_key(uri)
        print(f"Secret Key: {secret_key}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
