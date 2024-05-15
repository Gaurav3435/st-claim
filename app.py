import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import stanza

def intro():
    st.write("# Welcome to the Semantic Textual Similarity Demo! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This application showcases the power of different pre-trained language models in determining semantic textual similarity.

        **👈 Select a demo from the dropdown on the left** to explore the capabilities of each model!

        .
        
        .
        
        .
        
        Developer: Gaurav

        Guide: Dr. Robert Mercer
        """
    )

def data_frame_demo():
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write(
        """
        This demo utilizes the `bert-large-cased` model to compute semantic similarity between titles and sentences in different sections of research article. 
        """
    )

    @st.cache_data
    def get_data():
        df = pd.read_json('bert-large-cased.json')
        return df

    try:
        df = get_data()
        
        #select pmids and section
        pmids = st.multiselect("Choose PMID", list(set(df.pmid)), [])
        sections = st.multiselect("Choose Section", df['section'].unique(),[])
        
        #filter the dataframe 
        filtered_df = df[(df['pmid'].isin(pmids)) & (df['section'].isin(sections))]

        #drop title column
        try:
            title = filtered_df['title'].values[0]
            filtered_df = filtered_df.drop(['title'], axis=1)
        except:
            title = ''
            
        if filtered_df.empty:
            st.error("No data matches the selected filters.")
        else:
            st.write("### Sentence and their Similarity Score")
            # Apply background color to the similarity score column
            filtered_df.sort_index()
            styled_df = filtered_df.style.applymap(color_background, subset=['similarity_score'])
            st.write('Title: {}'.format(title))
            st.write(styled_df)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

def data_frame_demo2():
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        This demo utilizes the `biobert` model to compute semantic similarity between titles and sentences in different sections of research article. 
        """
    )

    @st.cache_data
    def get_data():
        df = pd.read_json('biobert-v1.1.json')
        return df

    try:
        df = get_data()
        
        #select pmids and section
        pmids = st.multiselect("Choose PMID", list(set(df.pmid)), [])
        sections = st.multiselect("Choose Section", df['section'].unique(),[])
        
        #filter the dataframe 
        filtered_df = df[(df['pmid'].isin(pmids)) & (df['section'].isin(sections))]

        #drop title column
        try:
            title = filtered_df['title'].values[0]
            filtered_df = filtered_df.drop(['title'], axis=1)
        except:
            title = ''
  
        if filtered_df.empty:
            st.error("No data matches the selected filters.")
        else:
            st.write("### Sentence and their Similarity Score")
            # Apply background color to the similarity score column
            filtered_df.sort_index()
            styled_df = filtered_df.style.applymap(color_background, subset=['similarity_score'])
            st.write('Title: {}'.format(title))
            st.write(styled_df)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

def data_frame_demo3():
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        This demo utilizes the `pubmedbert-base-embeddings` model to compute semantic similarity between titles and sentences in different sections of research article. 
        """
    )

    @st.cache_data
    def get_data():
        df = pd.read_json('pubmedbert-base-embeddings.json')
        return df

    try:
        df = get_data()
        
        #select pmids and section
        pmids = st.multiselect("Choose PMID", list(set(df.pmid)), [])
        sections = st.multiselect("Choose Section", df['section'].unique(),[])
        
        #filter the dataframe 
        filtered_df = df[(df['pmid'].isin(pmids)) & (df['section'].isin(sections))]

        #drop title column
        try:
            title = filtered_df['title'].values[0]
            filtered_df = filtered_df.drop(['title'], axis=1)
        except:
            title = ''

        if filtered_df.empty:
            st.error("No data matches the selected filters.")
        else:
            st.write("### Sentence and their Similarity Score")
            # Apply background color to the similarity score column
            filtered_df.sort_index()
            styled_df = filtered_df.style.applymap(color_background, subset=['similarity_score'])
            st.write('Title: {}'.format(title))
            st.write(styled_df)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

def data_frame_demo4():
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")
    st.write(
        """
        This demo utilizes the `nli-distilroberta-base-v2` model to compute semantic similarity between titles and sentences in different sections of research article. 
        """
    )

    @st.cache_data
    def get_data():
        df = pd.read_json('nli-distilroberta-base-v2.json')
        return df

    try:
        df = get_data()
        
        #select pmids and section
        pmids = st.multiselect("Choose PMID", list(set(df.pmid)), [])
        sections = st.multiselect("Choose Section", df['section'].unique(),[])
        
        #filter the dataframe 
        filtered_df = df[(df['pmid'].isin(pmids)) & (df['section'].isin(sections))]

        #drop title column
        try:
            title = filtered_df['title'].values[0]
            filtered_df = filtered_df.drop(['title'], axis=1)
        except:
            title = ''

        if filtered_df.empty:
            st.error("No data matches the selected filters.")
        else:
            st.write("### Sentence and their Similarity Score")
            # Apply background color to the similarity score column
            filtered_df.sort_index()
            styled_df = filtered_df.style.applymap(color_background, subset=['similarity_score'])
            st.write('Title: {}'.format(title))
            st.write(styled_df)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )
def color_background(val):
        color = f'rgba(255, 255, 255, {val})'  # Red color with alpha based on similarity score
        return f'background-color: {color}'

def data_frame_demo5():
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[5]}")
    st.write(
        """
        This demo utilizes the `MiniLM-L6-v2` model to compute semantic similarity between titles and sentences in different sections of research article. 
        """
    )

    @st.cache_data
    def get_data():
        df = pd.read_json('MiniLM-L6-v2.json')
        return df

    try:
        df = get_data()
        
        #select pmids and section
        pmids = st.multiselect("Choose PMID", list(set(df.pmid)), [])
        sections = st.multiselect("Choose Section", df['section'].unique(),[])
        
        #filter the dataframe 
        filtered_df = df[(df['pmid'].isin(pmids)) & (df['section'].isin(sections))]

        #drop title column
        try:
            title = filtered_df['title'].values[0]
            filtered_df = filtered_df.drop(['title'], axis=1)
        except:
            title = ''

        if filtered_df.empty:
            st.error("No data matches the selected filters.")
        else:
            st.write("### Sentence and their Similarity Score")
            # Apply background color to the similarity score column
            filtered_df.sort_index()
            styled_df = filtered_df.style.applymap(color_background, subset=['similarity_score'])
            st.write('Title: {}'.format(title))
            st.write(styled_df)

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

# Function to identify parts of speech and return them with corresponding tags
def identify_pos(text):
    #load pos tagging model
    nlp = load_stanza()
    doc = nlp(text)
    pos_tags = []
    for sentence in doc.sentences:
        for word in sentence.words:
            pos_tags.append((word.text, word.upos))
    if pos_tags:
        return pos_tags
    else:
        return ''

@st.cache_resource
def load_stanza():
    return stanza.Pipeline('en', package='genia')

def verb_stanza():
    st.markdown(f"# {list(page_names_to_funcs.keys())[6]}")
    st.write(
        """
        This is a stanza based approach for detecting part of speech in sentence.  
        """
    )

    
    
    try:
        
        # Color mapping for parts of speech
        pos_colors = {
            'NOUN': '#1E90FF',  # Dodger Blue
            'VERB': '#FF4500',  # Orange Red (Warm color)
            'ADJ': '#00CED1',   # Dark Turquoise
            'ADV': '#5F9EA0',   # Cadet Blue
            'PRON': '#4682B4',  # Steel Blue
            'DET': '#6495ED',   # Cornflower Blue
            'ADP': '#87CEEB',   # Sky Blue
            'CONJ': '#4169E1',  # Royal Blue
            'AUX': '#00BFFF',   # Deep Sky Blue
            'PROPN': '#7B68EE', # Medium Slate Blue
            'NUM': '#6A5ACD',   # Slate Blue
            'PART': '#483D8B',  # Dark Slate Blue
            'PUNCT': '#000000', # Black
            'SYM': '#708090',   # Slate Gray
            'X': '#778899'      # Light Slate Gray
        }

        #user input 
        user_input = st.text_area("Input Text", "Stanza is a great library for natural language processing.")
        if user_input:
            pos_tags = identify_pos(user_input)

         # Create HTML string with highlighted text
        highlighted_text = ""
        for word, pos in pos_tags:
            color = pos_colors.get(pos, '#FFFFFF')  # Default to white if POS tag not found
            highlighted_text += f'<span style="background-color: {color}">{word}</span> '

        st.markdown(highlighted_text, unsafe_allow_html=True)

        # Display legend for colors
        st.write("## Legend")
        legend_html = "<table>"
        for pos, color in pos_colors.items():
            legend_html += f'<tr><td style="background-color: {color}; width: 100px;"></td><td>{pos}</td></tr>'
        legend_html += "</table>"
        st.markdown(legend_html, unsafe_allow_html=True)

    
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )


page_names_to_funcs = {
    "Welcome": intro,
    "BERT": data_frame_demo,
    "BioBERT": data_frame_demo2,
    "Pubmedbert": data_frame_demo3,
    "DistilRoberta": data_frame_demo4,
    "MiniLM-L6-v2": data_frame_demo5,
    "Verb Detector": verb_stanza
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()