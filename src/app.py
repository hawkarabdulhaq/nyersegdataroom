import streamlit as st

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to update page state
def set_page(page):
    st.session_state.page = page

# Custom CSS for styling
st.markdown("""
    <style>
    /* Set the default font to Courier */
    * {
        font-family: "Courier", monospace;
    }
    
    /* Styling the title */
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Styling for section titles */
    .section-title {
        font-size: 1.7em;
        font-weight: bold;
        color: #34495E;
        margin-top: 30px;
        margin-bottom: 10px;
        border-bottom: 2px solid #34495E;
        padding-bottom: 5px;
    }
    
    /* General content styling */
    .content {
        font-size: 1.1em;
        color: #2C3E50;
        line-height: 1.6;
        text-align: justify;
        margin-bottom: 20px;
    }

    /* Highlighting important sections */
    .highlight {
        font-weight: bold;
        color: #1ABC9C;
    }
    
    /* Style for video container */
    .video-container {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation using Buttons
with st.sidebar:
    st.title("Navigation")
    st.button("Home", on_click=set_page, args=("Home",))
    st.button("Gallery", on_click=set_page, args=("Gallery",))
    st.button("Learning Platform", on_click=set_page, args=("Learning Platform",))

# Home Page Content
if st.session_state.page == "Home":
    st.markdown('<div class="title">Welcome to Personalized Python Training</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Perfect for beginners looking to learn coding in just one month and deploy their prototype projects.</div>', unsafe_allow_html=True)

    # Embed YouTube video
    st.markdown("""
    <div class="video-container">
        <h3>Watch the demo video and get to know about the course</h3>
        <iframe width="853" height="480" src="https://www.youtube.com/embed/Y_dxPZu1J6M" 
        title="Demo: Coding with Hawkar" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
        encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" 
        allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    # Course Overview
    st.markdown('<div class="section-title">Course Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
    Here’s a quick summary of what we’ll cover:

    - <strong>Setting Up Python</strong>: We’ll start by preparing your Python environment, ensuring you’re ready to begin your learning journey with a strong foundation.
    - <strong>Hawkar's Workflow</strong>: I’ll introduce my structured approach to learning Python, focusing on breaking down complex concepts into manageable steps for an efficient learning process.
    - <strong>Applying GitHub for App Creation</strong>: In this module, you'll learn to leverage GitHub to create a small app, setting the stage for your final project. By the end of the week, you’ll be equipped with the skills to develop, manage, and version control your project efficiently, all through GitHub.
    - <strong>Developing Your Final Project</strong>: Over the course of a week, you’ll work on a draft version of your final project, applying core coding concepts in a practical way. This phase will allow you to gather feedback, refine your approach, and ensure your project aligns with your goals.
    - <strong>Finalizing and Launching Your Project</strong>: In the final week, you’ll bring your project to completion. You’ll deploy the app, integrate key features, and showcase it within your community, creating a tangible outcome that reflects your learning journey.
    </div>
    """, unsafe_allow_html=True)

    # Pricing Information
    st.markdown('<div class="section-title">Pricing Options</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
    - <span class="highlight">Standard Course Fee</span>: <strong>375,000 IQD (discounted)</strong>
    - <span class="highlight">One-on-One Session</span>: <strong>$290</strong> for a personalized experience
    - <span class="highlight">Group Session (3+ people)</span>: <strong>$195 per person</strong>

    Choose the option that best fits your needs and learning preferences.
    </div>
    """, unsafe_allow_html=True)

    # Enrollment information
    st.markdown('<div class="section-title">Enrollment</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
    To confirm your enrollment, please make the course payment to <strong>FIB account 07504792181</strong>. Once the payment is received, you’ll receive a personalized survey to tailor the training according to your unique needs.

    For further details:
    - <strong>Email</strong>: <a href="mailto:connect@habdulhaq.com">connect@habdulhaq.com</a>
    - <strong>Website</strong>: <a href="https://www.habdulhaq.com/trainings">www.habdulhaq.com</a>
    </div>
    """, unsafe_allow_html=True)

# Gallery Page Placeholder
elif st.session_state.page == "Gallery":
    st.markdown('<div class="title">Gallery</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">This section will showcase images and achievements from the training sessions. Stay tuned for updates!</div>', unsafe_allow_html=True)

# Learning Platform Page Placeholder
elif st.session_state.page == "Learning Platform":
    st.markdown('<div class="title">Learning Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Our dedicated learning platform will provide resources, assignments, and quizzes. Updates coming soon!</div>', unsafe_allow_html=True)
