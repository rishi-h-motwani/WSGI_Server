# WSGI_Server

A minimal WSGI-compatible web server implementation in Python with example application.

## Features

- Implements the WSGI (Web Server Gateway Interface) specification (PEP 3333)
- Handles HTTP requests and responses
- Supports multithreading for concurrent connections
- Easy-to-extend for custom web frameworks or applications

## Requirements

- Python 3.x

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WSGI_Server.git
   cd WSGI_Server
   ```

2. Run the server with the included example WSGI app (wsgiapp.py):
   ```bash
    python main.py wsgiapp:app
   ```

3.Visit in your browser or test with curl:
  ```bash
     curl -v http://localhost:8888
```

## How It Works

1. Server Initialization:
   ```bash
   httpd = make_server(SERVER_ADDRESS, application)
   httpd.serve_forever()
   ```
2. Request Handling Flow:
   ```bash
   Client Request → parse_request() → get_environ() → 
   WSGI App → start_response() → finish_response()
   ```
   

   
   
   












   
