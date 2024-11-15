import webbrowser
import http.server
import socketserver
import os

PORT = 8000

# Sprawdzenie, czy plik istnieje
file_path = os.path.abspath('podglad_auto.html')
if os.path.exists(file_path):
    # Uruchomienie serwera lokalnego
    os.chdir(os.path.dirname(file_path))
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Serwer HTTP działa na http://localhost:{PORT}")
        webbrowser.open(f'http://localhost:{PORT}/podglad_auto.html')
        httpd.serve_forever()
else:
    print("Plik 'podglad_auto.html' nie został znaleziony.")