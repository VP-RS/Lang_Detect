import pickle
import streamlit as st
@st.cache_data
# Defining the model
def lang_detect(text):
    model = "papluca/xlm-roberta-base-language-detection"
    pickle_in = open('model.pkl', 'rb')
    classifier = pickle.load(pickle_in)
    
#Detecting the language of the input text 
    
    language = classifier(text, top_k=1, truncation=True)
    print("The language of the input text is:")
    return language
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Language Detection Web App</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    text = st.text_area('Enter or Paste your text below:')
    

     # when 'Detect' is clicked, make the prediction and store it
    if st.button("Detect"):
        result = lang_detect(text)
        st.write("The language of the input text is:")
        st.write(result)
if __name__=='__main__':
                        main()
