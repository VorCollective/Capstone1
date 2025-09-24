import streamlit as st
import json
from datetime import datetime
from pathlib import Path
import uuid
import os
from typing import Dict, List, Any
import difflib

@st.cache_data(ttl=3600)  # Cache for 1 hour instead of default
def load_json_data(file_path: str, default_data: List[Any] = None) -> List[Any]:
    # Your existing function code

# Clear all caches on deployment
    st.cache_data.clear()
    st.cache_resource.clear()


# Page Configuration - USING KENYAN FLAG AS ICON
st.set_page_config(
    page_title="Utamaduni Archive - Kenyan Cultural Heritage",
    page_icon="🇰🇪",
    layout="wide"
)

# NEW 2025 COLOR SCHEME - Modern Kenyan-inspired palette
st.markdown("""
<style>
    :root {
        --primary: #2E8B57;      
        --secondary: #FF6B35;     
        --accent: #4A90E2;        
        --dark: #2C3E50;          
        --light: #F8F9FA;         
        --success: #27AE60;       
    }
    
    .main-header {font-size: 3rem; color: var(--primary); text-align: center; font-weight: bold; margin-bottom: 0;}
    .sub-header {font-size: 1.8rem; color: var(--light); border-bottom: 3px solid var(--secondary); padding-bottom: 0.3rem; margin-top: 1rem;}
    .asset-card {border: 2px solid var(--primary); border-radius: 12px; padding: 20px; margin: 15px 0; background: linear-gradient(135deg, #FFFFFF 0%, #F8F9FA 100%);}
    .license-tag {background: linear-gradient(135deg, var(--primary) 0%, var(--light) 100%); color: white; padding: 6px 16px; border-radius: 8px; font-size: 0.9em; font-weight: bold;}
    .footer {font-size: 0.8rem; text-align: center; margin-top: 4rem; padding: 1.5rem; background-color: var(--dark); color: white; border-radius: 8px;}
    .file-info {background: linear-gradient(135deg, #E8F4F8 0%, #D4E7FA 100%); padding: 12px; border-radius: 8px; margin: 12px 0; border-left: 4px solid var(--accent);}
    .kenyan-flag {color: var(--primary); font-weight: bold; font-size: 1.1em;}
    .section-divider {border-top: 2px solid var(--secondary); margin: 25px 0; opacity: 0.6;}
    .success-banner {background: linear-gradient(135deg, var(--success) 0%, #2ECC71 100%); color: white; padding: 15px; border-radius: 8px; margin: 10px 0;}
    .warning-banner {background: linear-gradient(135deg, #E67E22 0%, #F39C12 100%); color: white; padding: 15px; border-radius: 8px; margin: 10px 0;}
    .info-banner {background: linear-gradient(135deg, var(--accent) 0%, #5DADE2 100%); color: white; padding: 15px; border-radius: 8px; margin: 10px 0;}
    
    /* Button styling */
    .stButton>button {background: linear-gradient(135deg, var(--primary) 0%, #34A853 100%); color: white; border: none; border-radius: 8px; padding: 10px 20px; font-weight: bold;}
    .stButton>button:hover {background: linear-gradient(135deg, var(--secondary) 0%, #E67E22 100%); transform: translateY(-1px);}
    
    /* Admin panel styling */
    .admin-section {background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid var(--secondary);}
    .admin-header {color: var(--secondary); font-weight: bold; font-size: 1.2em; margin-bottom: 10px;}
</style>
""", unsafe_allow_html=True)

# Function to add stylish divider
def kenyan_divider():
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Header with Kenyan Flag - UPDATED 2025 STYLING
st.markdown('**<p class="main-header"> Utamaduni Archive 2025</p>**', unsafe_allow_html=True)
st.markdown("**<span class='kenyan-flag'>Preserving Kenya's Cultural Legacy for Future Generations</span>**", unsafe_allow_html=True)
st.caption("Celebrating the rich tapestry of Kenyan heritage through digital preservation and community collaboration")
# Define Data Files - Using relative paths for Loveable deployment
TRIBES_FILE = "tribes.json"
ASSETS_FILE = "assets.json"
UPLOAD_DIR = "uploads"

# Data directories - Create if they don't exist
Path(UPLOAD_DIR).mkdir(exist_ok=True)

# License Options - for Copyright
LICENSE_OPTIONS = {
    "ALL_RIGHTS_RESERVED": "© All Rights Reserved. No reuse without explicit permission.",
    "CC_BY_NC_ND": "Creative Commons: Attribution-NonCommercial-NoDerivs",
    "CC_BY_NC_SA": "Creative Commons: Attribution-NonCommercial-ShareAlike",
    "CC_BY_SA": "Creative Commons: Attribution-ShareAlike",
    "CUSTOM": "Custom Terms (Specify in description)"
}

# Function to load data from JSON files with error handling
def load_json_data(file_path: str, default_data: List[Any] = None) -> List[Any]:
    """Load data from a JSON file. Return default data if file doesn't exist."""
    default_data = default_data or []
    try:
        if Path(file_path).exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Create an empty file if it doesn't exist
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, indent=2)
            return default_data
        
    except (FileNotFoundError, json.JSONDecodeError):
        # If file is corrupted, recreate it
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, indent=2)
        return default_data

# Function to save data to JSON files
def save_json_data(file_path: str, data: List[Any]) -> None:
    """Save data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)

# Pre-populate with some Kenyan Tribes data
kenyan_tribes = [
    {"id": "kalenjin", "name": "Kalenjin", "alternative_names": "Kalenjin", "region": "Rift Valley", "description": "A family of Southern Nilotic tribes known for athletic prowess and rich oral traditions...", "contact_community": "Council of Elders"},
    {"id": "kikuyu", "name": "Kikuyu", "alternative_names": "Agĩkũyũ", "region": "Central Kenya", "description": "One of the largest Bantu communities with rich agricultural traditions and storytelling heritage...", "contact_community": "Njuri Ncheke"},
    {"id": "luo", "name": "Luo", "alternative_names": "Jaluo", "region": "Nyanza", "description": "A Nilotic ethnic group known for fishing traditions, vibrant music, and rich oral history...", "contact_community": "Luo Council of Elders"},
    {"id": "luhya", "name": "Luhya", "alternative_names": "Abaluhya", "region": "Western Kenya", "description": "A Bantu ethnic group comprising many sub-communities with diverse cultural practices...", "contact_community": "Luhya Council of Elders"},
    {"id": "kamba", "name": "Kamba", "alternative_names": "Akamba", "region": "Eastern Kenya", "description": "A Bantu ethnic group known for wood carving, music, and rich storytelling traditions...", "contact_community": "Kamba Elders"},
    {"id": "maasai", "name": "Maasai", "alternative_names": "Ilmaasai", "region": "Rift Valley", "description": "A Nilotic ethnic group known for their distinctive culture, pastoral traditions, and beadwork...", "contact_community": "Maasai Elders"},
    {"id": "samburu", "name": "Samburu", "alternative_names": "Loikop, Kore", "region": "Rift Valley", "description": "A Nilotic ethnic group known for their distinctive culture, pastoral traditions, and beadwork. Also referred to as The Butterfly People due to the colorful dressing..", "contact_community": "Samburu Elders"},
    {"id": "meru", "name": "Meru", "alternative_names": "Ameru", "region": "Central", "description": "Bantu ethnic group that inhabit the Meru region of Kenya. The region is situated on the fertile lands of the north and eastern slopes of Mount Kenya in the former Eastern Province. The word Meru means 'shining light' in the Meru language.", "contact_community": "Njuri Ncheke"}
]

# Load existing data or initialize with default data
tribes_data = load_json_data(TRIBES_FILE, kenyan_tribes)
assets_data = load_json_data(ASSETS_FILE, [])

# ADMIN AUTHENTICATION 
ADMIN_USERNAME = "Benson"
ADMIN_PASSWORD = "utamaduni2025"

# Initialize session state for admin login
if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

# Sidebar section
kenyan_flag_url = "https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg"

st.sidebar.markdown(f"""
    <div style="text-align: center; margin: 20px 0 30px 0;">
        <img src="{kenyan_flag_url}" width="120" 
        style="margin-bottom: 10px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #2E8B57; margin: 5px 0;">Utamaduni Archive</h3>
        <p style="color: #666; font-size: 0.9em; margin: 0;">Kenyan Cultural Heritage</p>
    </div>
""", unsafe_allow_html=True)

# ADMIN PANEL in Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔐 Admin Panel")

if not st.session_state.admin_logged_in:
    with st.sidebar.expander("Admin Login", expanded=False):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.sidebar.success("Admin access granted!")
            else:
                st.sidebar.error("Invalid credentials")
else:
    st.sidebar.success(f"Logged in as {ADMIN_USERNAME}")
    if st.sidebar.button("Logout"):
        st.session_state.admin_logged_in = False
        st.sidebar.info("Logged out successfully")
    
    # Admin functions
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🛠️ Admin Tools")
    
    admin_option = st.sidebar.selectbox(
        "Select Action",
        ["Dashboard", "Manage Tribes", "Manage Assets", "System Info"]
    )
    
    # Display admin section based on selection
    if admin_option == "Dashboard":
        st.sidebar.markdown("""
        <div class="admin-section">
            <div class="admin-header">📊 System Overview</div>
            <p><strong>Tribes:</strong> {}</p>
            <p><strong>Assets:</strong> {}</p>
            <p><strong>Uploads:</strong> {} files</p>
        </div>
        """.format(     
            len(tribes_data), 
            len(assets_data),
            len(os.listdir(UPLOAD_DIR)) if os.path.exists(UPLOAD_DIR) else 0 #returning listed items from the existing directory
        ), unsafe_allow_html=True)
    
    elif admin_option == "Manage Tribes":
        st.sidebar.markdown('<div class="admin-header">👥 Manage Tribes</div>', unsafe_allow_html=True)
        
        # Add new tribe
        with st.sidebar.form("add_tribe_form"):
            st.markdown("**Add New Tribe**")
            new_tribe_name = st.text_input("Tribe Name")
            new_tribe_region = st.text_input("Region")
            submitted = st.form_submit_button("Add Tribe")
            
            if submitted and new_tribe_name:
                new_tribe = {
                    "id": new_tribe_name.lower().replace(" ", "_"),
                    "name": new_tribe_name,
                    "region": new_tribe_region,
                    "description": "",
                    "contact_community": ""
                }
                tribes_data.append(new_tribe)
                save_json_data(TRIBES_FILE, tribes_data)
                st.sidebar.success(f"Added {new_tribe_name} tribe")
        
        # Tribe management options
        tribe_names = [tribe["name"] for tribe in tribes_data]
        selected_tribe_name = st.sidebar.selectbox("Select Tribe to Manage", tribe_names)
        
        if selected_tribe_name:
            selected_tribe = next((t for t in tribes_data if t["name"] == selected_tribe_name), None)
            if selected_tribe:
                if st.sidebar.button("Delete Tribe"):
                    tribes_data = [t for t in tribes_data if t["name"] != selected_tribe_name]
                    save_json_data(TRIBES_FILE, tribes_data)
                    st.sidebar.success(f"Deleted {selected_tribe_name} tribe")
    
    elif admin_option == "Manage Assets":
        st.sidebar.markdown('<div class="admin-header">📦 Manage Assets</div>', unsafe_allow_html=True)
        
        st.sidebar.info(f"Total Assets: {len(assets_data)}")
        
        if assets_data:
            asset_titles = [f"{asset['title']} ({asset['tribe_name']})" for asset in assets_data]
            selected_asset_title = st.sidebar.selectbox("Select Asset", asset_titles)
            
            if selected_asset_title and st.sidebar.button("Delete Asset"):
                # Extract the actual title from the display format
                title_only = selected_asset_title.split(" (")[0]
                assets_data = [a for a in assets_data if a["title"] != title_only]
                save_json_data(ASSETS_FILE, assets_data)
                st.sidebar.success("Asset deleted")
        else:
            st.sidebar.info("No assets available")
    
    elif admin_option == "System Info":
        st.sidebar.markdown('<div class="admin-header">ℹ️ System Information</div>', unsafe_allow_html=True)
        st.sidebar.code(f"""
        App: Utamaduni Archive
        Version: 2025.1
        Data Files: {TRIBES_FILE}, {ASSETS_FILE}
        Upload Directory: {UPLOAD_DIR}
        Tribes: {len(tribes_data)}
        Assets: {len(assets_data)}
        """)

# Fuzzy match helper function
def fuzzy_match(query: str, text: str, threshold: float = 0.6) -> bool:
    if not query:
        return True
    score = difflib.SequenceMatcher(None, query.lower(), text.lower()).ratio()
    return score >= threshold

# SECTION 1: COMMUNITY CONTRIBUTION PORTAL
st.markdown('<p class="sub-header">🌱 Contribute to Our Heritage</p>', unsafe_allow_html=True)
st.markdown('<div class="info-banner">Share your community\'s cultural treasures. All contributions are preserved with the utmost respect for ownership and tradition.</div>', unsafe_allow_html=True)

with st.form("asset_contribution_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        # Create a list of tribe names for the dropdown
        tribe_names = [tribe["name"] for tribe in tribes_data]
        selected_tribe_name = st.selectbox("Select Community/Tribe*", options=tribe_names)
        # Find the selected tribe's ID
        selected_tribe = next((t for t in tribes_data if t["name"] == selected_tribe_name), None)
        
        asset_title = st.text_input("Title of Asset*")
        asset_type = st.selectbox("Type of Asset*", [
            "Oral History (Audio)", "Oral History (Video)", "Photograph", 
            "Document", "Artifact Description", "Song", "Proverb", 
            "Ritual Description", "Traditional Recipe", "Craft Instructions",
            "Dance Description", "Ceremony Recording", "Language Lesson",
            "Other"
        ])
        date_recorded = st.date_input("Date Recorded/Created", datetime.now())
    with col2:
        custodian_name = st.text_input("Name of Storyteller/Custodian")
        custodian_contact = st.text_input("Contact of Custodian (if willing to share)")
        license_type = st.selectbox("Usage License/Terms*", options=list(LICENSE_OPTIONS.keys()), format_func=lambda x: LICENSE_OPTIONS[x])
        custom_terms = st.text_area("Custom Terms (if selected 'CUSTOM' license)", placeholder="E.g., 'This story may only be used for educational purposes with attribution to the Luo Council of Elders.'")

    description = st.text_area("Description of the Asset*", help="What is this asset about? What does it represent?")
    narrative_context = st.text_area("Full Narrative, Story, or Context*", height=150, help="The full story being told, the lyrics of the song, the meaning of the proverb, etc.")
    
    # FILE UPLOAD SECTION
    st.markdown("**📎 Attach a File (Optional)**")
    uploaded_file = st.file_uploader("Choose a file", type=[
        'png', 'jpg', 'jpeg', 'gif',  # Images
        'mp3', 'wav', 'ogg',          # Audio
        'mp4', 'mov', 'avi',          # Video
        'pdf', 'doc', 'docx', 'txt'   # Documents
    ], label_visibility="collapsed")
    
    if uploaded_file:
        st.markdown(f'<div class="file-info">Selected file: <strong>{uploaded_file.name}</strong> ({uploaded_file.size} bytes)</div>', unsafe_allow_html=True)
    
    external_url = st.text_input("External URL (Optional)", placeholder="https://your-community-archive.org/asset123", help="A link to where this asset is stored on your community's own website or trusted archive.")

    submitted = st.form_submit_button("🌿 Submit Cultural Asset")
    if submitted:
        if not all([selected_tribe, asset_title, asset_type, description, narrative_context]):
            st.markdown('<div class="warning-banner">Please fill in all required fields (*).</div>', unsafe_allow_html=True)
        else:
            # Generate a unique ID for the asset
            asset_id = str(uuid.uuid4())[:8]
            date_added = datetime.now().date()  #Timestamping

            # HANDLE FILE UPLOAD
            saved_filename = None
            if uploaded_file is not None:
                try:
                    # Create a unique filename to avoid overwrites
                    file_extension = Path(uploaded_file.name).suffix.lower()
                    saved_filename = f"{asset_id}_{selected_tribe['id']}{file_extension}"
                    file_path = Path(UPLOAD_DIR) / saved_filename
                    
                    # Save the file
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    st.markdown('<div class="success-banner">File successfully uploaded and secured!</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.markdown(f'<div class="warning-banner">Error saving file: {e}</div>', unsafe_allow_html=True)
                    saved_filename = None

            # Create the new asset dictionary
            new_asset = {
                "id": asset_id,
                "tribe_id": selected_tribe["id"],
                "tribe_name": selected_tribe["name"],
                "title": asset_title,
                "asset_type": asset_type,
                "description": description,
                "narrative_context": narrative_context,
                "date_recorded": date_recorded.isoformat(),
                "custodian_name": custodian_name,
                "custodian_contact": custodian_contact,
                "license_type": license_type,
                "custom_terms": custom_terms,
                "attached_file": saved_filename,
                "original_filename": uploaded_file.name if uploaded_file else None,
                "external_url": external_url,
                "date_added": date_added.isoformat(),
                "region": selected_tribe["region"]
            }

            # Add to our in-memory list and save to file
            assets_data.append(new_asset)
            save_json_data(ASSETS_FILE, assets_data)
            
            st.markdown(f'<div class="success-banner">🇰🇪 Asante sana! Thank you for your contribution! Asset "{asset_title}" has been added to the archive. Your community\'s terms have been recorded.</div>', unsafe_allow_html=True)
            st.balloons()

# Public add missing tribe section
st.markdown('<p class="sub-header">➕ Add Missing Community</p>', unsafe_allow_html=True)
st.markdown('<div class="info-banner">If your community is not listed, submit it here for inclusion in the archive.</div>', unsafe_allow_html=True)

with st.form("add_tribe_form_public", clear_on_submit=True):
    tribe_name = st.text_input("Community Name*")
    alt_names = st.text_input("Alternative Names (comma-separated)")
    region = st.text_input("Primary Region*")
    description = st.text_area("Description*")
    contact = st.text_input("Contact/Governance Body (e.g., Council of Elders)")
    
    submit_tribe = st.form_submit_button("🌿 Submit Community")
    
    if submit_tribe:
        if not all([tribe_name, region, description]):
            st.markdown('<div class="warning-banner">Please fill in all required fields (*).</div>', unsafe_allow_html=True)
        else:
            # Check for duplicates
            if any(t["name"].lower() == tribe_name.lower() for t in tribes_data):
                st.markdown('<div class="warning-banner">This community already exists in the archive.</div>', unsafe_allow_html=True)
            else:
                new_tribe = {
                    "id": tribe_name.lower().replace(" ", "_"),
                    "name": tribe_name,
                    "alternative_names": alt_names,
                    "region": region,
                    "description": description,
                    "contact_community": contact
                }
                tribes_data.append(new_tribe)
                save_json_data(TRIBES_FILE, tribes_data)
                st.markdown(f'<div class="success-banner">🇰🇪 Asante sana! Community "{tribe_name}" has been added to the archive.</div>', unsafe_allow_html=True)
                st.balloons()

kenyan_divider()

# SECTION 2: PUBLIC EXPLORATION PORTAL
st.markdown('<p class="sub-header">🔍 Explore Cultural Treasures</p>', unsafe_allow_html=True)

if not assets_data:
    st.markdown('<div class="info-banner">🌟 Welcome to Utamaduni Archive! No assets have been added yet. Be the first to contribute!</div>', unsafe_allow_html=True)
else:
    # Filtering options
    col1, col2, col3 = st.columns(3)
    with col1:
        # Get unique tribe names and asset types from the assets data
        unique_tribes_in_assets = sorted(list(set(asset.get("tribe_name", "Unknown") for asset in assets_data)))
        tribe_filter = st.selectbox("Filter by Community", options=["All Communities"] + unique_tribes_in_assets)
    with col2:
        unique_asset_types = sorted(list(set(asset["asset_type"] for asset in assets_data)))
        type_filter = st.selectbox("Filter by Asset Type", options=["All Types"] + unique_asset_types)
    with col3:
        sort_option = st.selectbox("Sort by", ["Newest First", "Oldest First"])

    # Search input
    search_query = st.text_input("Search by Title, Description, or Narrative (Fuzzy Search)")

    # Filter the assets based on user selection
    filtered_assets = assets_data.copy()

    if tribe_filter != "All Communities":
        filtered_assets = [asset for asset in filtered_assets if asset.get("tribe_name") == tribe_filter]
    if type_filter != "All Types":
        filtered_assets = [asset for asset in filtered_assets if asset["asset_type"] == type_filter]

    if search_query:
        filtered_assets = [asset for asset in filtered_assets if (
            fuzzy_match(search_query, asset.get('title', '')) or
            fuzzy_match(search_query, asset.get('description', '')) or
            fuzzy_match(search_query, asset.get('narrative_context', ''))
        )]

    # Sort the assets
    if sort_option == "Newest First":
        filtered_assets.sort(key=lambda x: x.get("date_added", ""), reverse=True)
    else:
        filtered_assets.sort(key=lambda x: x.get("date_added", ""))

    # Display results
    if not filtered_assets:
        st.markdown('<div class="info-banner">Hakuna hazina iliyopatikana. No treasures found matching your filters. Please try a different search.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="success-banner">📚 Hazina {len(filtered_assets)} zilizopatikana! Found {len(filtered_assets)} Cultural Assets!</div>', unsafe_allow_html=True)
        
        for asset in filtered_assets:
            with st.expander(f"🌿 {asset['title']} - {asset['tribe_name']} ({asset['asset_type']})", expanded=False):
                col_info, col_media = st.columns([2, 1])
                
                with col_info:
                    st.markdown(f"**👥 Community:** {asset['tribe_name']} ({asset.get('region', 'N/A')})")
                    st.markdown(f"**📝 Description:** {asset['description']}")
                    st.markdown(f"**📖 Narrative/Context:**")
                    st.write(asset['narrative_context'])
                    st.markdown(f"**🧓 Custodian/Storyteller:** {asset.get('custodian_name', 'Not specified')}")
                    st.markdown(f"**📅 Date Recorded:** {asset.get('date_recorded', 'N/A')}")
                    st.markdown(f"**🗓️ Date Added to Archive:** {asset.get('date_added', 'N/A')}")

                    # Display the license terms clearly
                    license_text = LICENSE_OPTIONS.get(asset['license_type'], asset['license_type'])
                    if asset['license_type'] == 'CUSTOM' and asset.get('custom_terms'):
                        license_text = asset['custom_terms']
                    st.markdown(f"**📜 Usage Terms:** :license-tag[{license_text}]", unsafe_allow_html=True)

                    if asset.get('external_url'):
                        st.markdown(f"**🔗 External Link:** [Access external resource]({asset['external_url']})")
                
                with col_media:
                    # DISPLAY ATTACHED FILE
                    if asset.get("attached_file"):
                        file_path = Path(UPLOAD_DIR) / asset["attached_file"]
                        file_extension = Path(asset["attached_file"]).suffix.lower()
                        
                        st.markdown("**📎 Attached File:**")
                        st.markdown(f'<div class="file-info">File: {asset.get("original_filename", asset["attached_file"])}</div>', unsafe_allow_html=True)
                        
                        if file_extension in ['.png', '.jpg', '.jpeg', '.gif']:
                            # Display images directly
                            try:
                                st.image(str(file_path), caption="Attached Image", use_container_width=True)
                            except:
                                st.markdown('<div class="warning-banner">Could not display image. File may be corrupted.</div>', unsafe_allow_html=True)
                        
                        elif file_extension in ['.mp3', '.wav', '.ogg']:
                            # Display audio player
                            try:
                                st.audio(str(file_path))
                            except:
                                st.markdown('<div class="warning-banner">Could not play audio. File may be corrupted.</div>', unsafe_allow_html=True)
                        
                        elif file_extension in ['.mp4', '.mov', '.avi']:
                            # Display video player
                            try:
                                st.video(str(file_path))
                            except:
                                st.markdown('<div class="warning-banner">Could not play video. File may be corrupted.</div>', unsafe_allow_html=True)
                        
                        else:
                            # For PDFs, DOCS, TXT, etc., provide a download link
                            try:
                                with open(file_path, "rb") as file:
                                    st.download_button(
                                        label="📥 Download File",
                                        data=file,
                                        file_name=asset.get("original_filename", asset["attached_file"]),
                                        mime="application/octet-stream"
                                    )
                            except:
                                st.markdown('<div class="warning-banner">File unavailable for download.</div>', unsafe_allow_html=True)
                    
                    elif asset.get('external_url'):
                        st.markdown("**🌐 External Resource**")
                        st.markdown('<div class="info-banner">This asset is stored on an external platform. Use the link provided to access it.</div>', unsafe_allow_html=True)

kenyan_divider()

# SECTION 3: TRIBAL OVERVIEW
st.markdown('<p class="sub-header">👥 Kenyan Communities</p>', unsafe_allow_html=True)

# Tribe search
tribe_search_query = st.text_input("Search Communities by Name, Alternative Names, or Description (Fuzzy Search)")

# Filter tribes
filtered_tribes = tribes_data.copy()
if tribe_search_query:
    filtered_tribes = [tribe for tribe in filtered_tribes if (
        fuzzy_match(tribe_search_query, tribe.get('name', '')) or
        fuzzy_match(tribe_search_query, tribe.get('alternative_names', '')) or
        fuzzy_match(tribe_search_query, tribe.get('description', ''))
    )]

# Display tribes in a clean format
for tribe in filtered_tribes:
    with st.expander(f"🌍 {tribe['name']} - {tribe['region']}", expanded=False):
        st.markdown(f"**🔤 Alternative Names:** {tribe.get('alternative_names', 'N/A')}")
        st.markdown(f"**📋 Description:** {tribe.get('description', 'No description available.')}")
        st.markdown(f"**🤝 Contact/Governance:** {tribe.get('contact_community', 'N/A')}")
        
        # Count assets for this tribe
        tribe_assets = [asset for asset in assets_data if asset.get('tribe_id') == tribe['id']]
        st.markdown(f"**📦 Assets in Archive:** {len(tribe_assets)}")
        
        if tribe_assets:
            st.markdown("**🆕 Recent Additions:**")
            for asset in tribe_assets[:3]:  # Show first 3 assets
                st.markdown(f"- {asset['title']} ({asset['asset_type']})")

# Footer with Kenyan pride - UPDATED 2025
st.markdown("---")
st.markdown("""
<div class="footer">
    <strong>🌿 © Utamaduni Archive 2025</strong> | <em>Preserving Our Heritage, Building Our Future</em>
    <br>
    <color <small>This platform respects and upholds the copyrights of all contributing communities. 
    All cultural assets remain the intellectual property of the respective Kenyan communities.</small>
    <br><br>
    <strong>Let us all pull together towards preserving our cultural legacy.</strong>
            <marquee> 🐦Developed by Sipel Systems&trade; 2025</marquee>
</div>
""", unsafe_allow_html=True)2025-09-24 07:35:13.903 WARNING streamlit.runtime.caching.cache_data_api: N
