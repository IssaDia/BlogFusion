from bs4 import BeautifulSoup

def get_stripped_content(content):
        soup = BeautifulSoup(content, 'html.parser')
        stripped_content = soup.get_text(separator=' ', strip=True)
        return stripped_content
    
def remove_encoded_chars(content):
        str_en = content.encode("ascii", "ignore")
        str_de = str_en.decode()
        return str_de
