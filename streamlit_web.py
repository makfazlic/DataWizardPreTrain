import streamlit as st
import os 
import json


if 'count' not in st.session_state:
	st.session_state.count = 0

with open('count.txt') as f:
    c = int(f.read().strip())
    st.session_state.count = c

def update_count():
    st.session_state.count += 1
    with open('count.txt', 'w') as f:
        f.write(str(st.session_state.count))

with open('games.json') as f:
    data = json.load(f)

with open("decks.txt") as f:
    decks = f.readlines()
    decks = [x.strip() for x in decks]

def process(id, player_1, player_2):
    print(f"Processing game {id} between {player_1} and {player_2}")
    with open("./processed.json") as f:
        processed = json.load(f)
    
    processed[id] = [player_1, player_2]
    
    with open("./processed.json", "w") as f:
        json.dump(processed, f)

    update_count()
    return 

def is_processed(id):
    with open("./processed.json") as f:
        processed = json.load(f)
    
    if id in processed:
        return True
    else:
        return False
    
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: grey;'>Deck data collection</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>For the purposes of training neural networks</h2>", unsafe_allow_html=True)



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# State for deck1 and deck2
if 'deck1' not in st.session_state:
    st.session_state.deck1 = None

if 'deck2' not in st.session_state:
    st.session_state.deck2 = None
        
col1, col2 = st.columns(2)
col1.selectbox('Deck 1', decks, label_visibility="collapsed", key='deck1')
col2.selectbox('Deck 2', decks, label_visibility="collapsed", key='deck2')


st.button('Submit', use_container_width=True, on_click=process, args=(data[st.session_state.count][0], st.session_state.deck1, st.session_state.deck2))


grid = st.columns(11)

for i in range(len(data[st.session_state.count][1])):

    im = data[st.session_state.count][1][i]
    image = "./images/"+im+".jpg"
    grid[i%5].image(image, use_column_width=True)

for i in range(len(data[st.session_state.count][2])):

    im = data[st.session_state.count][2][i]
    image = "./images/"+im+".jpg"
    grid[i%5+6].image(image, use_column_width=True)

def increment_counter():
	st.session_state.count += 1