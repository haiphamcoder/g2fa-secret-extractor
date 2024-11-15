from setuptools import setup, find_packages

setup(
    name="g2fa-secret-extractor",
    version="0.0.1",
    description="A tool to extract and decode secret keys from Google Authenticator's otpauth-migration URIs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Hai Pham Ngoc",
    author_email="ngochai285nd@gmail.com",
    url="https://github.com/haiphamcoder/g2fa-secret-extractor",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "protobuf"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "g2fa-extract=scripts.run_extractor:main",
        ],
    },
)
