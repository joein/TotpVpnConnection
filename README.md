# TotpVpnConnection
Automate VPN Connect to 2 networks with otp tokens.
Solution is temporary.
I used https://zxing.org/w/decode.jspx for decoding of my QR code (nice works with photo of QR code).
You should add  `name_of_file.txt` to option `auth-user-pass` of your .ovpn config for connection.

Config.py format

    class Config:

        class ExternalConnection:
            USERNAME = "your_username"
            PASSWORD = "first_part_of_password"
            STR_QR_CODE = "str_qr_code"
            AUTH_FILE = 'your_auth_file.txt'
            OVPN_FILE = 'your_ovpn_file.ovpn'

        class InternalConnection:
            USERNAME = "your_username"
            PASSWORD = "first_part_of_password"
            STR_QR_CODE = "str_qr_code"
            AUTH_FILE = 'your_auth_file.txt'
            OVPN_FILE = 'your_ovpn_file.ovpn'
