
### 1. `README.md`
```markdown
# Windows RATs

`Windows RATs` is a simple project that uses Python to develop a Remote Access Trojan (RAT) for the Windows operating system. This project allows users to send commands from the server to the client to perform various tasks on the client machine such as changing the directory, listing files in the current directory, downloading files, uploading files, and deleting files. The project aims to provide an educational environment to understand how to build and improve RATs using safe and ethical programming practices. **This project is for educational purposes only and should not be used for any malicious or illegal activities.**

## Features

- Execute shell commands on the client.
- Change directory on the client.
- List files in the current directory on the client.
- Download files from the client to the server.
- Upload files from the server to the client.
- Delete files on the client.
- Encrypted communication for secure data transfer (planned).
- GUI for easier interaction (planned).

## Screenshots

### Server Running
![Server Running](screenshots/server_running.png)

### Client Running
![Client Running](screenshots/client_running.png)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/m3hm0o0ud/windows-RATs.git
   cd windows-RATs
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

## Usage

### Server

1. Run the server:
   ```bash
   python server.py
   ```

2. Available commands:
   - `cd <directory>`: Change directory on the client.
   - `dir`: List

 files in the current directory on the client.
   - `get <file_path>`: Download a file from the client to the server.
   - `put <file_path>`: Upload a file from the server to the client.
   - `remove <file_path>`: Delete a file on the client.
   - `exit`: Close the connection and stop the server.
   - `help`: Show available commands.

### Client

1. Convert the client script to an executable:
   ```bash
   pyinstaller --onefile client.py
   ```

2. Run the client:
   ```bash
   dist/client.exe
   ```

## Contribution

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

© 2024 Mahmoud Al-Sharif
```
