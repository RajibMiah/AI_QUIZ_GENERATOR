import streamlit as st
from utils import api_call 
from utils import casting_files

st.title("Note summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate note summary and quiz questions.")
st.divider()


with st.sidebar:

    st.header("Controls")
    
    images = st.file_uploader("Upload your photos of your notes" , 
                     type = ["jpg" , "jpeg" , "png"],
                     accept_multiple_files=True
                     )
    
    if images:
        st.subheader("Uploaded Images")
        column = st.columns(len(images))
        
        if len(images) > 3:
            st.warning("Please upload a maximum of 3 images.")
        else:
            
            for i in range(len(images)):
                with column[i]:
                    st.image(images[i] )

    #difficulty level for quiz questions
    selected_option = st.selectbox(" Select the difficulty level for quiz questions" , 
                        ("Easy" , "Medium" , "Hard"),
                        index = None)
    
    if selected_option:
        st.markdown(f"You have selected **{selected_option}** difficulty level for quiz questions.")
    else:
        st.markdown("Please select a difficulty level for quiz questions.")
    pressed = st.button("Click to generate" , type = "primary")


if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulity")
    

    if images and selected_option:

        # NOTEE
        st.subheader("Your notes")
        with st.container(border=True):

            with st.spinner("AI is writing notes for you!"):
                note_gen = api_call.note_generator(images)
                st.markdown(note_gen)


        # AUDIO TRANSCRIPT
        with st.container(border=True):
            with st.spinner("Ai is generating audio text"):
                st.subheader("Your audio transcript.")
                audio_transcript = api_call.audio_transcript(casting_files.make_plain_text(note_gen))
                # YOUR AUDIO TRANSCRIPT WILL BE SHOWN HERE
                st.audio(audio_transcript)


        # QUIZ
        with st.container(border= True):

            st.subheader(f"Quiz {selected_option}")

            # YOUR QUIZE WILL BE SHOWN HERE
            st.text("Your quize will be shown here.")
