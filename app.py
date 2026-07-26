import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import nltk
from nltk.corpus import stopwords
import os

# ==========================================
# 1. Page Configuration & Setup
# ==========================================
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Content-Based Book Recommender")
st.write("Select a book from the collection to get personalized recommendations based on title, author, and publisher similarities.")

# Download NLTK stopwords
nltk.download('stopwords', quiet=True)

# ==========================================
# 2. Data Loading & Preprocessing (Cached)
# ==========================================
@st.cache_data
def load_and_preprocess_data():
    # Dynamically resolve Books.csv file path to prevent FileNotFoundError
    file_path = os.path.join(os.path.dirname(__file__), 'Books.csv')
    df = pd.read_csv(file_path, low_memory=False)
    
    # Handle missing values
    for col in ['Book-Title', 'Book-Author', 'Publisher']:
        df[col] = df[col].fillna('')
        
    # Take a sample for fast app performance
    df_sub = df.head(5000).copy().reset_index(drop=True)
    
    # Text cleaning
    stop_words = set(stopwords.words('english'))
    def clean_text(text):
        text = str(text).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = [w for w in text.split() if w not in stop_words]
        return ' '.join(words)
    
    df_sub['combined'] = df_sub['Book-Title'] + ' ' + df_sub['Book-Author'] + ' ' + df_sub['Publisher']
    df_sub['clean_text'] = df_sub['combined'].apply(clean_text)
    
    # TF-IDF & Cosine Similarity Computation
    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    tfidf_matrix = tfidf.fit_transform(df_sub['clean_text'])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    return df_sub, similarity_matrix

# Load processed data
with st.spinner("Loading book catalog..."):
    df_books, sim_matrix = load_and_preprocess_data()

# Create title index lookup
indices = pd.Series(df_books.index, index=df_books['Book-Title']).drop_duplicates()

# ==========================================
# 3. Recommendation Function
# ==========================================
def recommend_books(book_title, top_n=5):
    idx = indices[book_title]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]
        
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    
    book_indices = [i[0] for i in sim_scores]
    scores = [i[1] for i in sim_scores]
    
    results = df_books.iloc[book_indices][['Book-Title', 'Book-Author', 'Publisher']].copy()
    results['Similarity Match'] = [f"{round(s * 100, 1)}%" for s in scores]
    return results

# ==========================================
# 4. Streamlit UI Elements
# ==========================================
st.markdown("---")

# Dropdown menu to select a book
book_list = sorted(df_books['Book-Title'].unique())
selected_book = st.selectbox(
    "🔍 Choose or type a book title:",
    options=book_list
)

# Button to trigger recommendation
if st.button("🚀 Get Recommendations", type="primary"):
    if selected_book:
        st.subheader(f"Top 5 Books Similar to *'{selected_book}'*:")
        
        recommendations = recommend_books(selected_book, top_n=5)
        
        # Display recommendations cleanly
        for idx, row in recommendations.iterrows():
            with st.container():
                st.markdown(f"### 📖 {row['Book-Title']}")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.caption(f"**Author:** {row['Book-Author']}")
                with col2:
                    st.caption(f"**Publisher:** {row['Publisher']}")
                with col3:
                    st.caption(f"**Match Score:** {row['Similarity Match']}")
                st.divider()