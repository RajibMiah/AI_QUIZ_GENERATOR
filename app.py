import streamlit as st


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
    st.button("Click to generate" , type = "primary")
