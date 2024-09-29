---
# **PHANTOM - Port Spoofing Tool**

**PHANTOM** is a simple Python-based tool that allows users to spoof ports on a machine to appear open and running a specified service. This can be useful for testing and simulating services during network scans.

## **Features**
- Spoof any port (0-65535) to appear open.
- Simulate a wide range of services (e.g., HTTP, FTP, SSH, etc.).
- Customizable service name and version inputs.
- Detect incoming connections to the spoofed port.
  
## **Requirements**
- Python 3.x
- Root/Administrator privileges (required to bind to privileged ports below 1024)

### **Dependencies**
- `socket`: Built-in Python library for network communication.

## **Installation**

Clone the repository:

```bash
git clone https://github.com/yourusername/phantom.git
```

Navigate to the project directory:

```bash
cd phantom
```

## **Usage**

To run the tool, use the following command:

```bash
sudo python3 phantom.py
```

### **Input Example**

Once the tool is running, you’ll be prompted to enter the following:

- **Port number**: Any port between 0-65535 that you want to spoof.
- **Service name**: Name of the service you want to simulate (e.g., `ftp`, `http`, `ssh`).
- **Service version**: Version of the service you’re spoofing (e.g., `vsftpd 2.0.5` for FTP, `Apache 2.4.41` for HTTP).

### **Example Run**

```bash
****************************************
**      PHANTOM - PORT SPOOFING TOOL      **
****************************************
Enter port number (0-65535): 21
Enter service name (e.g., http, ftp): ftp
Enter service version (e.g., 2.1): vsftpd 2.0.5
Port 21 is now appearing open, simulating ftp version vsftpd 2.0.5.
Waiting for connections on port 21...
```

You can then scan the machine or test the connection using tools like **Nmap** or **Netcat**.

#### **Nmap Scan Example**
```bash
nmap -p 21 127.0.0.1
```

This will show port 21 as open and running the simulated FTP service.

## **Stopping the Tool**
To stop the tool, press `Ctrl + C` in the terminal running **PHANTOM**.

## **Contributing**
Contributions are welcome! If you have any ideas, find bugs, or want to improve the tool, feel free to open a pull request or submit an issue.

---
