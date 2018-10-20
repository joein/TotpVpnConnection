import pyotp
import subprocess
import time

from config import Config


def connect(str_qr_code, static_password, auth_file, username, ovpn_file):
    otp = pyotp.TOTP(str_qr_code).now()
    password = static_password + str(otp)
    with open(auth_file, 'w') as auth_f:
        auth_f.write(f'{username}\n')
        auth_f.write(password)
    subprocess.Popen(['nohup', 'sudo', '-S', 'openvpn', '--config', ovpn_file])

    time.sleep(30)


connect(Config.ExternalConnection.STR_QR_CODE,
        Config.ExternalConnection.PASSWORD,
        Config.ExternalConnection.AUTH_FILE,
        Config.ExternalConnection.USERNAME,
        Config.ExternalConnection.OVPN_FILE)


connect(Config.InternalConnection.STR_QR_CODE,
        Config.InternalConnection.PASSWORD,
        Config.InternalConnection.AUTH_FILE,
        Config.InternalConnection.USERNAME,
        Config.InternalConnection.OVPN_FILE)
