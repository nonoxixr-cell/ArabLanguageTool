import streamlit as startswith

def app():
    st.title("Arabic Alphabet")
    
    st.markdown(
        """
        Welcome to the Arabic Alphabet!
        The alphabet has 28 letters, written from right to left.
        Each letter can change shape depending on its position in a word.
        """
    )
    
    st.divider()
    
    letters = [
        ("ا", "Alif", "aa"),
        ("ب", "Ba", "b"),
        ("ت", "Ta", "t"),
        ("ث", "Tha", "th"),
        ("ج", "Jeem", "j"),
        ("ح", "Haa", "ḥ"),
        ("خ", "Khaa", "kh"),
        ("د", "Dal", "d"),
        ("ذ", "Dhal", "dh"),
        ("ر", "Ra", "r"),
        ("ز", "Zay", "z"),
        ("س", "Seen", "s"),
        ("ش", "Sheen", "sh"),
        ("ص", "Saad", "ṣ"),
        ("ض", "Daad", "ḍ"),
        ("ط", "Taa", "ṭ"),
        ("ظ", "Dhaa", "ẓ"),
        ("ع", "Ayn", "ʿ"),
        ("غ", "Ghayn", "gh"),
        ("ف", "Fa", "f"),
        ("ق", "Qaf", "q"),
        ("ك", "Kaf", "k"),
        ("ل", "Lam", "l"),
        ("م", "Meem", "m"),
        ("ن", "Noon", "n"),
        ("ه", "Ha", "h"),
        ("و", "Waw", "w / oo"),
        ("ي", "Ya", "y / ee"),
    ]