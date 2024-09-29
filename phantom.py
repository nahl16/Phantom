import socket

# Banner for the tool
def print_banner():

    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")
    print("**********      ***          ***    **********    ****          ***  ***************   ********      ****          ****")
    print("***       **    ***          ***  ***        ***  *** *         ***        ***       **        **    *** *        * ***")
    print("***        **   ***          ***  ***        ***  ***  *        ***        ***      **          **   ***  *      *  ***")
    print("***        ***  ***          ***  ***        ***  ***   *       ***        ***     ***          ***  ***   *    *   ***")
    print("***        ***  ***          ***  ***        ***  ***    *      ***        ***     ***          ***  ***    *  *    ***")
    print("***       **    ****************  **************  ***     *     ***        ***     ***          ***  ***     **     ***")
    print("**********      ***          ***  ***        ***  ***      *    ***        ***     ***          ***  ***            ***")
    print("***             ***          ***  ***        ***  ***       *   ***        ***     ***          ***  ***            ***")
    print("***             ***          ***  ***        ***  ***        *  ***        ***      **          **   ***            ***")
    print("***             ***          ***  ***        ***  ***         * ***        ***       **        **    ***            ***")
    print("***             ***          ***  ***        ***  ***          ****        ***         ********      ***            ***")
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("")

def spoof_port():
    """Spoofs a port to appear open and running a specified service."""

    # Get user input
    while True:
        try:
            port = int(input("\nEnter port number (0-65535): "))  # Allowing any port number in the valid range for TCP/UDP
            if 0 <= port <= 65535:
                break
            else:
                print("Invalid port number. Please enter a value between 0 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    service_name = input("Enter service name (e.g., http, ftp): ")
    service_version = input("Enter service version (e.g., 2.1): ")

    # Spoof port by creating a simple TCP listener
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))  # Bind to all interfaces on the given port
    s.listen(1)

    print(f"Port {port} is now appearing open, simulating {service_name} version {service_version}.")
    print(f"Waiting for connections on port {port}...")

    # Keep the port open
    try:
        conn, addr = s.accept()
        print(f"Connection from {addr} detected. Port {port} successfully spoofed.")
        conn.close()
    except KeyboardInterrupt:
        print("\nStopping PHANTOM.")

# Main function to run the tool
def main():
    print_banner()
    spoof_port()

if __name__ == "__main__":
    main()
