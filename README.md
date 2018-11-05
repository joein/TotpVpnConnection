# TotpVpnConnection
Automate VPN Connect to 2 networks with otp tokens.
Solution is temporary.
I used https://zxing.org/w/decode.jspx for decoding of my QR code (nice works with photo of QR code).
You should add  `name_of_file.txt` to option `auth-user-pass` of your .ovpn config for connection.
username - username of vpn client
password - password for vpn client
str_qr_code - string from QR_CODE photo
auth_file - file with username and full password (static part + otp)
ovpn_file - client's openvpn config
utun - name of expected vpn-interface

Config.py format

    class Config:

        class ExternalConnection:
            USERNAME = "your_username"
            PASSWORD = "first_part_of_password"
            STR_QR_CODE = "str_qr_code"
            AUTH_FILE = 'your_auth_file.txt'
            OVPN_FILE = 'your_ovpn_file.ovpn'
            UTUN = 'utunX'
            
        class InternalConnection:
            USERNAME = "your_username"
            PASSWORD = "first_part_of_password"
            STR_QR_CODE = "str_qr_code"
            AUTH_FILE = 'your_auth_file.txt'
            OVPN_FILE = 'your_ovpn_file.ovpn'
            UTUN = 'utunY'
