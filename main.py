import pandas as pd
from bs4 import BeautifulSoup


# Definizione della funzione clean_html
def clean_html(html):
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Define the allowed tags
    allowed_tags = {'p', 'b', 'strong', 'ul', 'li', 'ol'}

    # Remove all tags that are not allowed
    for tag in soup.find_all():
        if tag.name not in allowed_tags:
            tag.unwrap()

    # Remove all attributes from the allowed tags
    for tag in soup.find_all(allowed_tags):
        tag.attrs = {}

    return str(soup)


# Caricare il file Excel
input_file = 'input.xlsx'
output_file = 'output.xlsx'

# Leggere il file Excel
df = pd.read_excel(input_file)

# Applicare la funzione clean_html alla colonna A
df['Descrizione'] = df['Descrizione'].apply(clean_html)

# Salvare il risultato in un nuovo file Excel
df.to_excel(output_file, index=False)
