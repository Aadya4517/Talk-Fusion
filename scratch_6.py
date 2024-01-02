import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet


st.title("Definitions, synonyms and antonyms of any word")

text=st.text_input("Enter the word:")

synonyms=[]
antonyms=[]

try:
    word=wordnet.synsets(text)[0].defintion()
except:
      word=' '

for syn in wordnet.synsets(text):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name)

if st.button('Get Output'):

    if text==' ':
        st.write("Please Enter Text")
    else:
        synonyms=str(list(set(synonyms)))
        antonyms=str(list(set(antonyms)))

st.markdown('** Meaning- **'+ word)
st.markdown('** Synonyms- **'+synonyms)
st.markdown('** Antonyms- **'+antonyms)
st.markdown('** Sentence - **'+str(wordnet.synsets(text)[0].examples()))