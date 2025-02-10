from bs4 import BeautifulSoup
 
# Replace 'ss.html' with the actual path to your HTML file
html_file_path = 'ss.html'
 
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
 
 
soup = BeautifulSoup(html_content, 'html.parser')
vocabulary_data = []
flashcard_previews = soup.find_all('app-flashcard-preview')
 
for flashcard in flashcard_previews:
    question = flashcard.find_all('div', class_='viewer')[0].get_text(strip=True).replace(";", " sk ").replace("\n", "")

    answer_div = flashcard.find_all('div', class_='viewer')[1]
    answer_div.attrs = {}
    answer = str(answer_div).replace(";", "(semikolon here)").replace("\n", "")

    vocabulary_data.append((question, answer))
 

# Write the extracted information to a text file
with open('flashcards.txt', 'w', encoding='utf-8') as file:
    for q,a in vocabulary_data:
        print(f'{q[:20]};{a[:20]}')
        file.write(f'{q};{a}\n')
