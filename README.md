# Accural-Tor-Flux
**Elite IP Rotator | Optimized for Accural | Powered by Artiphoria**

Accural-Tor-Flux is a high-performance, automated IP rotation tool built on the Tor network. It is designed for maximum privacy and seamless integration with the Accural ecosystem.

## Features
- **Distro-Aware**: Automatically detects your Linux distribution (Debian, Arch, Fedora, etc.) and manages Tor installation/services.
- **Root Security**: Enforces secure execution and handles service permissions.
- **Smart Rotation**: Configurable intervals and customizable iteration counts.
- **Branded UI**: Premium terminal experience designed by | Artiphoria | Accural.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mohamed-Salah-1/Accural-Tor-Flux.git
   cd Accural-Tor-Flux
   ```

2. **Make the installer executable**:
   ```bash
   chmod +x install.py
   ```

3. **Run the installer**:
   ```bash
   ./install.py
   ```
   *Note: You can also use `python3 install.py` if you prefer.*

4. **Usage**:
   Once installed, type `acc` or `aut` in any terminal to launch the tool.
   ```bash
   sudo acc
   ```

## Alternative: Run Without Installation
If you don't want to install the tool globally, you can run it directly from the directory:

1. **Make the script executable**:
   ```bash
   chmod +x auto_flux.py
   ```

2. **Run it with sudo**:
   ```bash
   sudo ./auto_flux.py
   ```

## Configuration
### Browser Configuration

#### Firefox
1. Go to **Settings** > **General** > **Network Settings** > **Settings...**
2. Select **Manual proxy configuration**.
3. In **SOCKS Host**, enter `127.0.0.1` and Port `9050`.
4. Select **SOCKS v5**.
5. Check **Proxy DNS when using SOCKS v5**.
6. Click **OK**.

#### Chrome / Chromium
Chrome uses the system proxy settings by default. To use a specific proxy:
1. Launch Chrome from the terminal with the proxy flag:
   ```bash
   google-chrome --proxy-server="socks5://127.0.0.1:9050"
   ```
   *Or for Chromium:*
   ```bash
   chromium --proxy-server="socks5://127.0.0.1:9050"
   ```
2. Alternatively, use extensions like **FoxyProxy** or **SwitchyOmega** to manage proxy settings easily within the browser.
- The tool will automatically request rotation timing and iteration preferences upon launch.

## Disclaimer
This tool is intended for privacy and educational purposes. Ensure you comply with all local laws and the Tor Project's terms of service.

---
**Marketing & Support**:
- Youtube: [Artiphoria](https://www.youtube.com/@Artiphoria)
- System: **Accural ERP**
