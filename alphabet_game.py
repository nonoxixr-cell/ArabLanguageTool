import streamlit as st
import random

def alphabetgame(letters):
    st.subheader("Play to learn Alphabet")
    
    if "score" not in st.session_state:
        st.session_state.score = 0
        
    if "question" not in session_state:
        st.session_state.question = random.choice(letters)
        
    game_type = st.selectbox(
        "Choose game mode:",
        [
            "Litsen and guess"
            "Guess Letter"
        ],
        key = game_type
    )
    
    st.divider()
    
 #this basically check if what the user submits is right then add 1 to their score if it is correct.   
 #litsen and guess game  
    if game_type == "Listen and guess"
        letter, name, sound, audio = st.session_state.question
        
        
        st.audio(f"Sounds/{audio}")
        
        user_input = st.text_input("Enter arabic letter:", key = "letter_input")     
        
        
        if st.button("Submit", key = "submit_litsen"):
            if user_input.strip() == letter:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Wrong. Correct letter was: {letter}")
                
            st.session_state.question = random.choice(letters)
            st.experimental_rerun() #forces streamlit to run the code again as it does not do it automatically
            
            
            
    elif game_type == "Guess Letter":
        letter, correct_name, sound, audio = st.session_state.question
        
        
        st.markdown(
            f"<h1 style='text-align:center;'>{letter}</h1>",
            unsafe_allow_html=True
        )
        
        
        options = [l[1] for l in letters]
        user_choice = st.radio(
            "Choose the correct letter name:",
            options,
            key="name_choice"
        )
        
        if st.button("Submit", key = "submit_see")
            if user_choice == correct_name:
                st.success("Correct!)
                st.session_state.score += 1
            else:
                st.error(f"Wrong, Correct Answer: {correct_name}")
                
        st.session_state.question = random.choice(letters)
        st.experimental_rerun()
                
    st.write(f"Score:{st.session_state.score}")    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            