import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

def main():

    st.title("Linked In Post Generator for Yogesh Shete")
    col1, col2 = st.columns(2)
    text_ip = st.text_input("Write a short description of what you want to generate : ")


    fs = FewShotPosts()
    
  
    with col1:
        selected_tag = st.selectbox("Title", options = fs.get_tags())  
    with col2:
        selected_length = st.selectbox("Length", options = ["Short" , "Medium" , "Long"])  

    if st.button("Generate"):
        post = generate_post(selected_length, selected_tag, text_ip)
        st.markdown(f"{post}")



if __name__ == "__main__":
    main()


