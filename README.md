# TotpVpnConnection
Automate VPN Connect to 2 networks with otp tokens. <br>
Solution is temporary. <br>
I used https://zxing.org/w/decode.jspx for decoding of my QR code (nice works with photo of QR code). <br>
You should add  `name_of_file.txt` to option `auth-user-pass` of your .ovpn config for connection. <br>
username - username of vpn client <br>
password - password for vpn client <br>
str_qr_code - string from QR_CODE photo <br>
auth_file - file with username and full password (static part + otp) <br>
ovpn_file - client's openvpn config <br>
utun - name of expected vpn-interface <br>

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
