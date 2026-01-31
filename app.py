import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Celestial Ocean", page_icon="🌊", layout="wide")

st.markdown("# 🌊✨ Celestial Ocean")
st.markdown("### *Where the night sky meets the sea*")

st.sidebar.header("⚙️ Controls")
num_stars = st.sidebar.slider("Number of stars", 50, 500, 200)
star_size = st.sidebar.slider("Star size", 1, 10, 3)
wave_height = st.sidebar.slider("Wave amplitude", 0.1, 2.0, 0.5, 0.1)
ocean_color = st.sidebar.color_picker("Ocean color", "#1e3a5f")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### 🌌 Your Celestial View")
    
    @st.cache_data
    def generate_stars(n, size):
        np.random.seed(42)
        return pd.DataFrame({
            'x': np.random.uniform(0, 100, n),
            'y': np.random.uniform(50, 100, n),
            'size': np.random.uniform(size/2, size*2, n),
            'brightness': np.random.uniform(0.3, 1.0, n)
        })
    
    stars = generate_stars(num_stars, star_size)
    
    x = np.linspace(0, 100, 200)
    y = wave_height * np.sin(x * 0.1) + 25
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=stars['x'], y=stars['y'], mode='markers',
        marker=dict(size=stars['size'], color='white', opacity=stars['brightness'], symbol='star'),
        hoverinfo='skip', showlegend=False
    ))
    
    fig.add_trace(go.Scatter(
        x=x, y=y, mode='lines', fill='tozeroy',
        fillcolor=ocean_color, line=dict(color=ocean_color, width=2),
        hoverinfo='skip', showlegend=False
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[0, 100], showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(range=[0, 100], showgrid=False, showticklabels=False, zeroline=False),
        height=600, margin=dict(l=0, r=0, t=0, b=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### 📊 Info")
    st.info(f"🕐 {datetime.now().strftime('%H:%M:%S')}")
    st.metric("✨ Stars", f"{num_stars:,}")
    st.metric("🌊 Waves", f"{wave_height:.1f}")

st.caption("🌊 Built with Streamlit")
```

5. **Click** "Commit new file"

6. **Repeat for** `requirements.txt`:
   - Add file → Create new file
   - Name: `requirements.txt`
   - Content:
```
streamlit>=1.28.0
plotly>=5.17.0
numpy>=1.24.0
pandas>=2.0.0
