import pyotp
import subprocess
import time

from config import Config


def connect(str_qr_code, static_password, auth_file, username, ovpn_file, utun):
    otp = pyotp.TOTP(str_qr_code).now()
    password = static_password + str(otp)
    with open(auth_file, 'w') as auth_f:
        auth_f.write(f'{username}\n')
        auth_f.write(password)
    if vpn_not_connected(utun):
        subprocess.Popen(['sudo', 'openvpn', '--config', ovpn_file])
        print(f'sudo openvpn --config {ovpn_file}')
    wait_vpn_connection(utun)


def vpn_not_connected(utun):
    try:
        subprocess.check_call(['ifconfig', utun])
        print(f'{utun} is already connected')
        return False
    except subprocess.CalledProcessError:
        return True


def wait_vpn_connection(utun):
    connected = False
    begin = time.time()
    while not connected and (time.time() - begin) < 60:
        try:
            subprocess.check_call(['ifconfig', utun])
            connected = True
        except subprocess.CalledProcessError:
            time.sleep(1)
    if not connected:
        raise Exception(f'Connection timeout {utun}')
    print(f'{utun} connected successfully')
    time.sleep(2)
    return True


def kill_zombie_process(ovpn_filename):
    try:
        pids = subprocess.check_output(['pgrep', 'openvpn'])
        pids_list = [pid for pid in pids.decode().split('\n') if pid != '']
        for pid in pids_list:
            ps_info = subprocess.check_output(['ps', '-p', pid])
            ps_info_list = ps_info.decode().split('\n')
            for process_info in ps_info_list:
                if ovpn_filename in process_info:
                    subprocess.check_call(['sudo', 'kill', pid])
                    print(f'{pid} has been successfully removed')
    except subprocess.CalledProcessError:
        print("can't kill zombie process")
        return False
    return True


def disconnect_zombie_vpn(utun1, utun2, internal_ovpn_file):
    try:
        subprocess.check_call(['ifconfig', utun1])
    except subprocess.CalledProcessError:
        try:
            subprocess.check_call(['ifconfig', utun2])
            kill_zombie_process(internal_ovpn_file)
        except subprocess.CalledProcessError:
            return False
    return True


if __name__ == '__main__':

    disconnect_zombie_vpn(Config.ExternalConnection.UTUN,
                          Config.InternalConnection.UTUN,
                          Config.InternalConnection.OVPN_FILE)

    connect(Config.ExternalConnection.STR_QR_CODE,
            Config.ExternalConnection.PASSWORD,
            Config.ExternalConnection.AUTH_FILE,
            Config.ExternalConnection.USERNAME,
            Config.ExternalConnection.OVPN_FILE,
            Config.ExternalConnection.UTUN)

    connect(Config.InternalConnection.STR_QR_CODE,
            Config.InternalConnection.PASSWORD,
            Config.InternalConnection.AUTH_FILE,
            Config.InternalConnection.USERNAME,
            Config.InternalConnection.OVPN_FILE,
            Config.InternalConnection.UTUN)

