Program wykorzystuje API OpenAI do automatycznego przekształcenia artykułu z pliku tekstowego na kod HTML.
Umożliwia:
- wczytanie artykułu z pliku tekstowego tresc_artykulu.txt
- przetworzenie treści artykułu za pomocą modelu językowego OpenAI (gpt-4o-mini)
- wygenerowanie kodu HTML z odpowiednimi tagami, tj.: nagłówki, akapity, listy, itp.
- wskazanie miejsca na grafiki za pomocą znaczników <img src="image_placeholder.jpg" alt="prompt dla grafiki">.
- zapisanie wygenerowanego kodu w pliku artykul.html
- użycie podglad.html do wyświetlenia w przeglądarce przykładowo wygenerowanego artykułu.
- użycie szablon.html do wkleja własnego wygenerowanego artykułu i wyświetlenia go w przeglądarce lub uruchomienie skryptu automat.py do automatycznie zaciągnięcia treści artykul.html i wyświetlenia go automatycznie w przeglądarce za pomocą serwera lokalnego.

Wymagania:
- Python
- klucz API OpenAI
- pakiet openai

Instrukcja instalacji:
1. Sklonowanie repozytorium
2. Przejście do katalogu projektu
3. Instalacja wymaganych pakietów:
pip install -r requirements.txt
4. Konfiguracja klucza API
Należy utworzyć plik .env w katalogu głównym projektu za pomocą komendy: touch .env
Następnie dodajemy w nim klucz API:
OPENAI_API_KEY=’klucz-api’

Uruchomienie aplikacji
Aby wczytać program, należy uruchomić skrypt main.py (w terminalu wpisać python main.py).
Jeżeli chcemy użyć do przetworzenia innego artykułu, należy go umieścić w pliku tresc_artykulu.txt.

Podgląd przykładowego artykułu
Aby zobaczyć wizualizację przykładowo wygenerowanego artykułu należy otworzyć plik podgląd.html w przeglądarce internetowej.

Wyświetlenie wygenerowanego artykułu
Aby zobaczyć wizualizację własnego wygenerowanego artykułu należy otworzyć plik szablon.html i w miejscu <!-- Miejsce na artykuł --> wkleić wygenerowany artykuł z pliku artykul.html. Następnie należy plik szablon.html otworzyć w przeglądarce internetowej.

Wyświetlanie artykułu za pomocą serwera lokalnego
- Po uruchomieniu skrytpu automat.py, automatycznie uruchomi się serwer lokalny i otworzy przeglądarkę z podglądem artykułu.
- Jeśli przeglądarka się nie otworzy automatycznie, należy wpisać ręcznie w pasku adresu przeglądarki: http://localhost:8000/podglad_auto.html
- Aby zatrzymać serwer, naciśnij Ctrl+C w terminalu.






# html_generator
