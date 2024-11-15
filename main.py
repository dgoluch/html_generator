import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.Client(api_key=os.environ.get('OPENAI_API_KEY'))

#Odczytuje plik tekstowy z artykułem

nazwa_pliku = "tresc_artykulu.txt"

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            return plik.read()
    except FileNotFoundError:
        print("Error: Plik {nazwa_pliku} nie został znaleziony.")
        return None
    
#Łączy się  z azurem Open AI i treść artykułu wraz z promptem przekazuje do OpenAI w celu obróbki

def zapytaj_openai(tresc_artykulu):
    prompt = (
        '''Przekształć poniższy artykuł na kod HTML, używając odpowiednich tagów do strukturyzacji treści.
        Używaj nagłówków do dzielenia artykułu na sekcje, a akapitów do oddzielania bloków tekstu.
        Wstaw miejsca na obrazy za pomocą tagu <img src='image_placeholder.jpg'> oraz dodaj dokładny opis obrazka pasujący do treści artykułu jako atrybut alt. 
        Pod każdym obrazkiem umieść krótki podpis w odpowiednim tagu.
        Nie używaj tagów <html>, <head>, <body>, ani CSS i JavaScript.
        Nie dadawaj żadnego dodatkowego tekstu do treści artykułu.
        Nie dodawaj znaczników ```html lub html:.\n\n
        Artykuł:\n'''
    )

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Jesteś ekspertem w tworzeniu czystego kodu HTML."},
                {"role": "user", "content": prompt + tresc_artykulu}
            ],
            max_tokens=1500,
            temperature=0.5
        )

        response = completion.choices[0].message.content
        return response
    except Exception as e:
        return f"Błąd podczas komunikacji z API: {e}"
    

def zapis_do_pliku(nazwa_pliku, tresc):
    try:
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            plik.write(tresc)
        print(f"Zapisano kod HTML w pliku: {nazwa_pliku}")
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku: {e}")

if __name__ == "__main__":
    tresc_artykulu = wczytaj_plik(nazwa_pliku)
    
    if tresc_artykulu:
        # Wysyłanie artykułu do OpenAI
        wygenerowany_kod_html = zapytaj_openai(tresc_artykulu)
        
        # Zapisanie wygenerowanego kodu HTML do pliku 
        zapis_do_pliku("artykul.html", wygenerowany_kod_html)

