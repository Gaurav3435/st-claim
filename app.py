import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

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
            st.write('Title: {}'.format(title))
            st.write(filtered_df.sort_index())

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
            st.write('Title: {}'.format(title))
            st.write(filtered_df.sort_index())

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
            st.write('Title: {}'.format(title))
            st.write(filtered_df.sort_index())

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
            st.write('Title: {}'.format(title))
            st.write(filtered_df.sort_index())

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

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
            st.write('Title: {}'.format(title))
            st.write(filtered_df.sort_index())

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
    "MiniLM-L6-v2": data_frame_demo5
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()