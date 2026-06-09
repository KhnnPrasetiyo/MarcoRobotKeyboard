"""TODO: module documentation"""

import os
import re
import subprocess
import threading
import urllib.request
import zipfile


def detect_connected_chips():
    """
    Scans the system using PowerShell Get-PnpDevice to find connected USB-Serial chips
    (CH340, FTDI, CP2102). Returns a list of dictionaries with chip info.
    Uses PowerShell instead of deprecated wmic to avoid console-handle blocking issues
    in PyInstaller noconsole builds.
    """
    chips = []
    if os.name != "nt":
        return chips

    try:
        # Use PowerShell Get-PnpDevice — modern, non-blocking, no console handle issues
        # CREATE_NO_WINDOW prevents any console window from appearing
        creation_flags = 0x08000000  # CREATE_NO_WINDOW
        ps_cmd = (
            "Get-PnpDevice -PresentOnly | "
            "Where-Object { $_.InstanceId -match 'VID_1A86|VID_0403|VID_10C4' } | "
            "Select-Object -Property FriendlyName,InstanceId,Status | "
            "ConvertTo-Csv -NoTypeInformation"
        )
        cmd = ["powershell", "-NonInteractive", "-NoProfile", "-Command", ps_cmd]
        out = subprocess.check_output(
            cmd,
            stdin=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=creation_flags,
            timeout=8,
        ).decode("utf-8", errors="ignore")

        # Chip signature mapping
        signatures = {
            "VID_1A86": "CH340",  # WCH CH340 / CH341
            "VID_0403": "FTDI",  # FTDI FT232R
            "VID_10C4": "CP2102",  # Silicon Labs CP210x
        }

        import csv
        import io

        seen_ids = set()
        reader = csv.DictReader(io.StringIO(out))
        for row in reader:
            caption = row.get("FriendlyName", "").strip().strip('"')
            device_id = row.get("InstanceId", "").strip().strip('"')
            status = row.get("Status", "").strip().strip('"')

            if not device_id or device_id in seen_ids:
                continue
            seen_ids.add(device_id)

            matched_signature = None
            for sig, chip_type in signatures.items():
                if sig in device_id.upper():
                    matched_signature = chip_type
                    break

            if not matched_signature:
                continue

            port_match = re.search(r"\(COM(\d+)\)", caption)
            port = f"COM{port_match.group(1)}" if port_match else None
            has_driver = status.upper() == "OK" and port is not None

            chips.append(
                {
                    "chip_type": matched_signature,
                    "device_id": device_id,
                    "caption": caption,
                    "status": status,
                    "has_driver": has_driver,
                    "port": port,
                }
            )
    except Exception as e:
        print("Error occurred")
        pass

    return chips


# Driver Download Links
DRIVER_LINKS = {
    "CH340": "https://cdn.sparkfun.com/assets/learn_resources/8/4/4/CH341SER.EXE",
    "FTDI": "https://ftdichip.com/wp-content/uploads/2023/09/CDM-v2.12.36.4-WHQL-Certified.zip",
}


def download_and_install_driver(chip_type, log_callback, completion_callback):
    """
    Downloads and installs driver for target chip_type asynchronously.
    """
    url = DRIVER_LINKS.get(chip_type)
    if not url:
        if completion_callback:
            completion_callback(
                False, f"Tautan unduhan untuk chip {chip_type} tidak terkonfigurasi."
            )
        return

    def run_installer():
        """TODO: add documentation"""
        try:
            # 1. Create a drivers temp folder in workspace
            base_dir = os.path.dirname(os.path.abspath(__file__))
            temp_dir = os.path.join(base_dir, "temp_drivers")
            os.makedirs(temp_dir, exist_ok=True)

            file_name = url.split("/")[-1]
            download_path = os.path.join(temp_dir, file_name)

            # 2. Download official setup file
            if log_callback:
                log_callback(f"Mengunduh driver resmi {chip_type}...")

            # Simple chunked downloader with percentage tracking
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as response:
                total_size = int(response.info().get("Content-Length", 0))
                downloaded = 0
                block_size = 8192

                with open(download_path, "wb") as f:
                    while True:
                        buffer = response.read(block_size)
                        if not buffer:
                            break
                        downloaded += len(buffer)
                        f.write(buffer)
                        if total_size > 0:
                            percent = int((downloaded / total_size) * 100)
                            if log_callback and percent % 20 == 0:
                                log_callback(f"Unduhan Driver: {percent}% selesai")

            if log_callback:
                log_callback(f"Berkas berhasil diunduh ke {os.path.basename(download_path)}")

            # 3. Handle ZIP extraction (like FTDI Setup)
            executable_path = download_path
            if file_name.endswith(".zip"):
                if log_callback:
                    log_callback("Mengekstrak paket instalasi ZIP...")
                with zipfile.ZipFile(download_path, "r") as zip_ref:
                    zip_ref.extractall(temp_dir)
                # Find .exe file inside extracted folder
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        if file.endswith(".exe"):
                            executable_path = os.path.join(root, file)
                            break

            # 4. Execute Installer (trigger UAC)
            if log_callback:
                log_callback(f"Meluncurkan: {os.path.basename(executable_path)}...")
                log_callback("Silakan setujui dialog Administrator Windows (UAC) jika diminta.")

            # Standard subprocess launch. startfile naturally handles UAC popups in Windows.
            os.startfile(executable_path)

            if log_callback:
                log_callback(
                    "Installer berhasil diluncurkan. Selesaikan instalasi di jendela baru."
                )
            if completion_callback:
                completion_callback(
                    True, "Installer diluncurkan! Silakan ikuti instruksi di jendela instalasi."
                )

        except Exception as e:
            print("Error occurred")
            if log_callback:
                log_callback(f"Gagal menginstal driver: {str(e)}")
            if completion_callback:
                completion_callback(False, str(e))

    # Run in separate thread to prevent freezing Tkinter GUI
    threading.Thread(target=run_installer, daemon=True).start()
