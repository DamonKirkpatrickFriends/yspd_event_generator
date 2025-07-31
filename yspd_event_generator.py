import streamlit as st
import pandas as pd
import io
import zipfile
from datetime import datetime

# Template generation functions
def generate_14_day_template(event):
    """Generate the 14-day reminder email template"""
    
    # Map CSV columns to template variables
    park_name = event.get("Chapter/Park Name", "")
    coordinator_name = event.get("Volunteer Coordinator Name", "")
    coordinator_email = event.get("Volunteer Coordinator Email", "")
    coordinator_phone = event.get("Volunteer Coordinator Phone", "")
    project_description = event.get("Describe the project(s) that are planned at your site.", "")
    meeting_location = event.get("Specific meeting location - e.g., Visitor Center, Group Shelter 1.", "")
    meeting_time = event.get("Meeting Time", "")
    
    # For now, using placeholder date - we'll need to get actual event date
    event_date = "[EVENT DATE]"  # TODO: Get actual date
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; }}
        .header {{ background-color: #2c5530; color: white; padding: 20px; text-align: center; }}
        .content {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; }}
        .highlight-box {{ background-color: #e8f5e8; padding: 15px; margin: 15px 0; border-left: 3px solid #2c5530; }}
        .main-section {{ background-color: #fff; padding: 20px; border: 2px solid #8fbc8f; margin-top: 20px; }}
        .section-header {{ color: #2c5530; font-size: 18px; font-weight: bold; margin-bottom: 15px; border-bottom: 2px solid #8fbc8f; padding-bottom: 5px; }}
        .footer-box {{ background-color: #2c5530; color: #FFFFFF; padding: 15px; margin-top: 20px; }}
        ul {{ margin: 10px 0; padding-left: 20px; }}
        li {{ margin-bottom: 5px; }}
        a {{ color: #2c5530; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Your State Parks Day is Almost Here!</h1>
        <p>Two weeks to go - {park_name} - Your State Parks Day</p>
    </div>
    
    <div class="content">
        <p>Dear Volunteer,</p>
        
        <p>We're excited that you've registered for <strong>{park_name} - Your State Parks Day</strong>! In just two weeks, you'll join volunteers across all 63 Georgia State Parks and Historic Sites for a statewide day of service.</p>
        
        <div class="highlight-box">
            <strong>Your Project:</strong> {project_description}
        </div>
        
        <p><strong>Date:</strong> {event_date}</p>
        <p><strong>Meeting Location:</strong> {meeting_location}</p>
        <p><strong>Meeting Time:</strong> {meeting_time}</p>
        
        <div class="main-section">
            <div class="section-header">General Information - Your State Parks Day</div>
            
            <img alt="Your State Parks Day Logo" src="/sites/default/files/styles/large/public/2025-06/YSPD-LOGO---Original.png" style="float:left;max-width:120px;height:auto;margin:0 15px 15px 0;" />
            
            <p><strong>About Your State Parks Day:</strong><br />
            Join Friends of Georgia State Parks for a statewide day of service! Volunteers across all 63 Georgia State Parks and Historic Sites will come together to help preserve and enhance these treasured natural and cultural resources.</p>
            
            <div style="clear:both;">&nbsp;</div>
            
            <div class="highlight-box">
                <strong>About Friends of Georgia State Parks</strong>
                <p style="margin-bottom:5px;">Friends of Georgia State Parks & Historic Sites is a nonprofit organization that serves, supports, and celebrates Georgia's state parks and historic sites. Through volunteer service, fundraising, and community partnerships, we help enhance visitor experiences and strengthen the connection between people and Georgia's most important treasures.</p>
            </div>
            
            <p><strong>What to Expect:</strong></p>
            <ul>
                <li>Meaningful outdoor conservation work</li>
                <li>Meeting fellow nature enthusiasts and park lovers</li>
                <li>Making a visible difference in your local state park</li>
                <li>Learning about your park's unique ecosystem and history</li>
            </ul>
            
            <p><strong>General Guidelines:</strong></p>
            <ul>
                <li>Dress appropriately for the project and weather conditions</li>
                <li>Bring plenty of water and sunscreen</li>  
                <li>All tools and equipment will be provided unless otherwise noted</li>
                <li>Most projects are suitable for ages 12 and up, younger volunteers will need extra help (minors must be accompanied by an adult)</li>
            </ul>
            
            <p><strong>Weather Policy:</strong><br />
            Inclement weather may force cancellation of some events. Check with the park if you have questions on the day of.</p>
            
            <div class="footer-box">
                <strong>Questions?</strong><br />
                Local Site Coordinator: {coordinator_name}<br />
                Email: {coordinator_email}<br />
                Phone: {coordinator_phone}<br />
                <br />
                Friends of Georgia State Parks<br />
                Email: info@friendsofgastateparks.org<br />
                Website: www.friendsofgastateparks.org
            </div>
        </div>
        
        <p style="margin-top: 20px;">We can't wait to see you in two weeks!</p>
        
        <p>Thank you for helping preserve Georgia's natural treasures,<br>
        <strong>Friends of Georgia State Parks</strong></p>
    </div>
</body>
</html>"""
    
    return html_template

def generate_3_day_template(event):
    """Generate the 3-day reminder email template"""
    
    park_name = event.get("Chapter/Park Name", "")
    coordinator_name = event.get("Volunteer Coordinator Name", "")
    coordinator_email = event.get("Volunteer Coordinator Email", "")
    coordinator_phone = event.get("Volunteer Coordinator Phone", "")
    project_description = event.get("Describe the project(s) that are planned at your site.", "")
    meeting_location = event.get("Specific meeting location - e.g., Visitor Center, Group Shelter 1.", "")
    meeting_time = event.get("Meeting Time", "")
    what_to_bring = event.get("What Should A Volunteer Bring for the Day? e.g., gloves, sun screen, bug spray, etc.", "")
    special_instructions = event.get("Special Instructions: e.g., closed-toe shoes, working near water, bring a change of clothes if desired, etc.", "")
    
    event_date = "[EVENT DATE]"  # TODO: Get actual date
    
    # Convert what_to_bring to bullet points
    bring_items = what_to_bring.split(',') if what_to_bring else ["Work gloves", "Water bottle", "Closed-toe shoes"]
    bring_list = "\\n".join([f"                <li>{item.strip()}</li>" for item in bring_items])
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; }}
        .header {{ background-color: #2c5530; color: white; padding: 20px; text-align: center; }}
        .content {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; }}
        .highlight-box {{ background-color: #e8f5e8; padding: 15px; margin: 15px 0; border-left: 3px solid #2c5530; }}
        .footer-box {{ background-color: #2c5530; color: #FFFFFF; padding: 15px; margin-top: 20px; }}
        ul {{ margin: 10px 0; padding-left: 20px; }}
        li {{ margin-bottom: 5px; }}
        a {{ color: #2c5530; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>This Weekend: Your State Parks Day!</h1>
        <p>{park_name} - Your State Parks Day</p>
    </div>
    
    <div class="content">
        <p>Dear Volunteer,</p>
        
        <p>Your State Parks Day volunteer project is just 3 days away! Here are the important details:</p>
        
        <div class="highlight-box">
            <p><strong>Project:</strong> {project_description}</p>
            <p><strong>Date:</strong> {event_date}</p>
            <p><strong>Meeting Location:</strong> {meeting_location}</p>
            <p><strong>Meeting Time:</strong> {meeting_time}</p>
        </div>
        
        <img alt="Your State Parks Day Logo" src="/sites/default/files/styles/large/public/2025-06/YSPD-LOGO---Original.png" style="max-width:120px;height:auto;margin:15px 0;" />
        
        <p><strong>What to Bring:</strong></p>
        <ul>
{bring_list}
        </ul>
        
        <p><strong>Special Instructions:</strong> {special_instructions}</p>
        
        <div class="footer-box">
            <strong>Questions?</strong><br />
            Local Site Coordinator: {coordinator_name}<br />
            Email: {coordinator_email}<br />
            Phone: {coordinator_phone}
        </div>
        
        <p style="margin-top: 20px;">See you this weekend!</p>
        
        <p><strong>Friends of Georgia State Parks</strong></p>
    </div>
</body>
</html>"""
    
    return html_template

def generate_day_before_template(event):
    """Generate the day before reminder email template"""
    
    park_name = event.get("Chapter/Park Name", "")
    coordinator_name = event.get("Volunteer Coordinator Name", "")
    coordinator_phone = event.get("Volunteer Coordinator Phone", "")
    meeting_location = event.get("Specific meeting location - e.g., Visitor Center, Group Shelter 1.", "")
    meeting_time = event.get("Meeting Time", "")
    
    event_date = "[EVENT DATE]"  # TODO: Get actual date
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; }}
        .header {{ background-color: #2c5530; color: white; padding: 20px; text-align: center; }}
        .content {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; }}
        .highlight-box {{ background-color: #e8f5e8; padding: 15px; margin: 15px 0; border-left: 3px solid #2c5530; }}
        .weather-box {{ background-color: #fff3cd; padding: 15px; margin: 15px 0; border-left: 3px solid #ffc107; }}
        .footer-box {{ background-color: #2c5530; color: #FFFFFF; padding: 15px; margin-top: 20px; }}
        a {{ color: #2c5530; text-decoration: none; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Tomorrow: Your State Parks Day!</h1>
        <p>{park_name} - Your State Parks Day</p>
    </div>
    
    <div class="content">
        <p>Dear Volunteer,</p>
        
        <p>We're excited to see you tomorrow for Your State Parks Day!</p>
        
        <div class="highlight-box">
            <p><strong>Tomorrow at {event_date}</strong></p>
            <p><strong>Meeting Location:</strong> {meeting_location}</p>
            <p><strong>Meeting Time:</strong> {meeting_time}</p>
        </div>
        
        <img alt="Your State Parks Day Logo" src="/sites/default/files/styles/large/public/2025-06/YSPD-LOGO---Original.png" style="max-width:120px;height:auto;margin:15px 0;" />
        
        <div class="weather-box">
            <p><strong>🌤️ Weather Check:</strong> This is an outdoor volunteer project. 
            <a href="https://forecast.weather.gov/zipcity.php?inputstring=[PARK_ZIP_CODE]" target="_blank">
            Click here to check tomorrow's weather forecast
            </a> and dress appropriately!</p>
            
            <p>If conditions look unsafe, use your best judgement. For a list of any cancellations, <a href="[YSPD_CANCELLATION_PAGE_URL]" target="_blank">click here</a>.</p>
        </div>
        
        <p><strong>Quick Reminders:</strong></p>
        <p>✓ Bring your work gloves, water bottle, and closed-toe shoes<br>
        ✓ Dress for outdoor work and weather conditions</p>
        
        <div class="footer-box">
            <strong>Last-minute questions?</strong><br />
            Local Site Coordinator: {coordinator_name}<br />
            Phone: {coordinator_phone}
        </div>
        
        <p style="margin-top: 20px;">Thank you for volunteering to help preserve Georgia's natural treasures!</p>
        
        <p><strong>See you tomorrow!</strong><br>
        <strong>Friends of Georgia State Parks</strong></p>
    </div>
</body>
</html>"""
    
    return html_template

# Page config
st.set_page_config(
    page_title="YSPD Event Generator",
    page_icon="🌲",
    layout="wide"
)

# Title and description
st.title("🌲 YSPD Event Generator")
st.markdown("Upload your volunteer event spreadsheet and generate email templates for all parks!")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a step:", ["1. Upload Data", "2. Preview Data", "3. Data Cleanup", "4. Generate Templates"])

if page == "1. Upload Data":
    st.header("Step 1: Upload Your Spreadsheet")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose your CSV file", 
        type=['csv'],
        help="Upload the spreadsheet with all your park event data"
    )
    
    if uploaded_file is not None:
        # Store in session state
        st.session_state.uploaded_file = uploaded_file
        
        # Read and display basic info
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        
        st.success(f"✅ File uploaded successfully!")
        st.info(f"📊 Found {len(df)} events in your spreadsheet")
        
        # Show column names
        st.subheader("Column Headers Found:")
        cols = st.columns(3)
        for i, col in enumerate(df.columns):
            with cols[i % 3]:
                st.write(f"• {col}")
    
    else:
        st.info("👆 Please upload your CSV file to get started")

elif page == "2. Preview Data":
    if 'df' not in st.session_state:
        st.warning("⚠️ Please upload your data first!")
        st.stop()
    
    st.header("Step 2: Preview Your Data")
    
    df = st.session_state.df
    
    # Show data preview
    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)
    
    # Show data summary
    st.subheader("Data Summary")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Events", len(df))
    
    with col2:
        # Count unique parks
        park_col = "Chapter/Park Name"  # Adjust based on your actual column name
        if park_col in df.columns:
            unique_parks = df[park_col].nunique()
            st.metric("Unique Parks", unique_parks)
    
    with col3:
        # Count missing coordinator emails
        email_col = "Volunteer Coordinator Email"
        if email_col in df.columns:
            missing_emails = df[email_col].isna().sum()
            st.metric("Missing Emails", missing_emails)
    
    # Data quality checks
    st.subheader("Data Quality Check")
    
    required_columns = [
        "Volunteer Coordinator Name",
        "Volunteer Coordinator Email", 
        "Chapter/Park Name",
        "Describe the project(s) that are planned at your site.",
        "Specific meeting location - e.g., Visitor Center, Group Shelter 1.",
        "Meeting Time"
    ]
    
    missing_cols = [col for col in required_columns if col not in df.columns]
    
    if missing_cols:
        st.error(f"❌ Missing required columns: {', '.join(missing_cols)}")
    else:
        st.success("✅ All required columns found!")

elif page == "3. Data Cleanup":
    if 'df' not in st.session_state:
        st.warning("⚠️ Please upload your data first!")
        st.stop()
    
    st.header("Step 3: Clean Up Your Data")
    
    # Make a copy of the dataframe for editing
    if 'cleaned_df' not in st.session_state:
        st.session_state.cleaned_df = st.session_state.df.copy()
    
    df_clean = st.session_state.cleaned_df
    
    # Show current data status
    st.subheader("Data Quality Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        missing_emails = df_clean["Volunteer Coordinator Email"].isna().sum()
        st.metric("Missing Emails", missing_emails, delta=None if missing_emails == 0 else "⚠️")
    
    with col2:
        missing_phones = df_clean["Volunteer Coordinator Phone"].isna().sum()
        st.metric("Missing Phones", missing_phones, delta=None if missing_phones == 0 else "⚠️")
    
    with col3:
        # Check if zip code column exists
        if "Park Zip Code" in df_clean.columns:
            missing_zips = df_clean["Park Zip Code"].isna().sum()
            st.metric("Missing Zip Codes", missing_zips, delta=None if missing_zips == 0 else "⚠️")
        else:
            st.metric("Zip Code Column", "Missing", delta="❌")
    
    # Cleanup options
    st.subheader("Cleanup Tools")
    
    # Choose cleanup view
    cleanup_view = st.radio(
        "Choose how you want to edit your data:",
        ["🔧 Quick Tools", "📋 Table Editor", "📝 Single Event Editor"],
        horizontal=True
    )
    
    if cleanup_view == "🔧 Quick Tools":
        # Original tab layout for automated cleanup
        cleanup_tab1, cleanup_tab2, cleanup_tab3 = st.tabs(["📍 Add Zip Codes", "📞 Fix Phone Numbers", "✨ General Cleanup"])
        
        with cleanup_tab1:
            st.write("**Add Park Zip Codes**")
            
            # Add zip code column if it doesn't exist
            if "Park Zip Code" not in df_clean.columns:
                if st.button("➕ Add Zip Code Column"):
                    df_clean["Park Zip Code"] = ""
                    st.session_state.cleaned_df = df_clean
                    st.success("Added 'Park Zip Code' column!")
                    st.rerun()
            
            if "Park Zip Code" in df_clean.columns:
                # Show parks missing zip codes
                missing_zip_parks = df_clean[df_clean["Park Zip Code"].isna() | (df_clean["Park Zip Code"] == "")]
                
                if len(missing_zip_parks) > 0:
                    st.write(f"Parks missing zip codes ({len(missing_zip_parks)}):")
                    
                    for idx, row in missing_zip_parks.iterrows():
                        park_name = row["Chapter/Park Name"]
                        
                        col_park, col_zip = st.columns([3, 1])
                        
                        with col_park:
                            st.write(f"**{park_name}**")
                        
                        with col_zip:
                            zip_code = st.text_input(
                                "Zip", 
                                value="", 
                                key=f"zip_{idx}",
                                placeholder="30309"
                            )
                            if zip_code and len(zip_code) == 5:
                                df_clean.at[idx, "Park Zip Code"] = zip_code
                                st.session_state.cleaned_df = df_clean
                else:
                    st.success("✅ All parks have zip codes!")
        
        with cleanup_tab2:
            st.write("**Standardize Phone Numbers**")
            
            # Show current phone format issues
            phone_col = "Volunteer Coordinator Phone"
            if phone_col in df_clean.columns:
                # Count different phone formats
                phone_samples = df_clean[phone_col].dropna().head(5).tolist()
                
                if phone_samples:
                    st.write("Current phone number formats:")
                    for phone in phone_samples:
                        st.code(str(phone))
                    
                    if st.button("🔧 Auto-format Phone Numbers"):
                        # Simple phone number cleaning
                        def clean_phone(phone):
                            if pd.isna(phone):
                                return phone
                            
                            # Remove all non-digits
                            digits = ''.join(filter(str.isdigit, str(phone)))
                            
                            # If 10 digits, format as (XXX) XXX-XXXX
                            if len(digits) == 10:
                                return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
                            # If 11 digits and starts with 1, remove the 1
                            elif len(digits) == 11 and digits.startswith('1'):
                                digits = digits[1:]
                                return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
                            else:
                                return phone  # Return original if can't format
                        
                        df_clean[phone_col] = df_clean[phone_col].apply(clean_phone)
                        st.session_state.cleaned_df = df_clean
                        st.success("✅ Phone numbers formatted!")
                        st.rerun()
        
        with cleanup_tab3:
            st.write("**General Text Cleanup**")
            
            if st.button("🧹 Clean Text Fields"):
                text_columns = [
                    "Volunteer Coordinator Name",
                    "Chapter/Park Name", 
                    "Describe the project(s) that are planned at your site.",
                    "Specific meeting location - e.g., Visitor Center, Group Shelter 1."
                ]
                
                for col in text_columns:
                    if col in df_clean.columns:
                        # Strip whitespace and fix common issues
                        df_clean[col] = df_clean[col].astype(str).str.strip()
                        df_clean[col] = df_clean[col].str.replace('  ', ' ')  # Double spaces
                        df_clean[col] = df_clean[col].replace('nan', '')  # Remove 'nan' strings
                
                st.session_state.cleaned_df = df_clean
                st.success("✅ Text fields cleaned!")
    
    elif cleanup_view == "📋 Table Editor":
        st.write("**Edit data directly in the table below**")
        st.info("💡 Click on any cell to edit it. Changes are saved automatically.")
        
        # Use st.data_editor for inline editing
        edited_df = st.data_editor(
            df_clean,
            use_container_width=True,
            num_rows="dynamic",  # Allow adding/removing rows
            column_config={
                "Park Zip Code": st.column_config.TextColumn(
                    "Park Zip Code",
                    help="5-digit zip code for the park",
                    max_chars=5,
                ),
                "Volunteer Coordinator Phone": st.column_config.TextColumn(
                    "Phone",
                    help="Phone number in (XXX) XXX-XXXX format",
                ),
                "Meeting Time": st.column_config.TextColumn(
                    "Meeting Time",
                    help="e.g., 9:00 AM",
                ),
            }
        )
        
        # Update session state with edited data
        st.session_state.cleaned_df = edited_df
        df_clean = edited_df
    
    elif cleanup_view == "📝 Single Event Editor":
        st.write("**Review and edit events one at a time**")
        
        # Event navigation
        total_events = len(df_clean)
        
        if 'current_event_idx' not in st.session_state:
            st.session_state.current_event_idx = 0
        
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        
        with col1:
            if st.button("⬅️ Previous") and st.session_state.current_event_idx > 0:
                st.session_state.current_event_idx -= 1
                st.rerun()
        
        with col2:
            if st.button("➡️ Next") and st.session_state.current_event_idx < total_events - 1:
                st.session_state.current_event_idx += 1
                st.rerun()
        
        with col3:
            current_idx = st.selectbox(
                f"Event ({st.session_state.current_event_idx + 1} of {total_events})",
                range(total_events),
                index=st.session_state.current_event_idx,
                format_func=lambda x: f"{x+1}. {df_clean.iloc[x]['Chapter/Park Name']}"
            )
            if current_idx != st.session_state.current_event_idx:
                st.session_state.current_event_idx = current_idx
                st.rerun()
        
        with col4:
            if st.button("⏮️ First"):
                st.session_state.current_event_idx = 0
                st.rerun()
        
        with col5:
            if st.button("⏭️ Last"):
                st.session_state.current_event_idx = total_events - 1
                st.rerun()
        
        # Current event data
        current_event = df_clean.iloc[st.session_state.current_event_idx]
        
        st.markdown("---")
        st.subheader(f"Event {st.session_state.current_event_idx + 1}: {current_event['Chapter/Park Name']}")
        
        # Editable fields
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.write("**Contact Information**")
            new_coordinator = st.text_input("Coordinator Name", value=str(current_event.get("Volunteer Coordinator Name", "")))
            new_email = st.text_input("Coordinator Email", value=str(current_event.get("Volunteer Coordinator Email", "")))
            new_phone = st.text_input("Coordinator Phone", value=str(current_event.get("Volunteer Coordinator Phone", "")))
            
            # Add zip code field
            if "Park Zip Code" not in df_clean.columns:
                df_clean["Park Zip Code"] = ""
                st.session_state.cleaned_df = df_clean
            
            new_zip = st.text_input("Park Zip Code", value=str(current_event.get("Park Zip Code", "")), max_chars=5)
        
        with col_right:
            st.write("**Event Details**")
            new_park_name = st.text_input("Park Name", value=str(current_event.get("Chapter/Park Name", "")))
            new_meeting_location = st.text_area("Meeting Location", value=str(current_event.get("Specific meeting location - e.g., Visitor Center, Group Shelter 1.", "")))
            new_meeting_time = st.text_input("Meeting Time", value=str(current_event.get("Meeting Time", "")))
        
        st.write("**Project Description**")
        new_project = st.text_area(
            "Project Description", 
            value=str(current_event.get("Describe the project(s) that are planned at your site.", "")),
            height=100
        )
        
        col_bring, col_instructions = st.columns(2)
        
        with col_bring:
            st.write("**What to Bring**")
            new_bring = st.text_area(
                "Items to bring", 
                value=str(current_event.get("What Should A Volunteer Bring for the Day? e.g., gloves, sun screen, bug spray, etc.", "")),
                height=80
            )
        
        with col_instructions:
            st.write("**Special Instructions**")
            new_instructions = st.text_area(
                "Special instructions", 
                value=str(current_event.get("Special Instructions: e.g., closed-toe shoes, working near water, bring a change of clothes if desired, etc.", "")),
                height=80
            )
        
        # Save changes button
        if st.button("💾 Save Changes to This Event", type="primary"):
            idx = st.session_state.current_event_idx
            df_clean.at[idx, "Volunteer Coordinator Name"] = new_coordinator
            df_clean.at[idx, "Volunteer Coordinator Email"] = new_email
            df_clean.at[idx, "Volunteer Coordinator Phone"] = new_phone
            df_clean.at[idx, "Park Zip Code"] = new_zip
            df_clean.at[idx, "Chapter/Park Name"] = new_park_name
            df_clean.at[idx, "Specific meeting location - e.g., Visitor Center, Group Shelter 1."] = new_meeting_location
            df_clean.at[idx, "Meeting Time"] = new_meeting_time
            df_clean.at[idx, "Describe the project(s) that are planned at your site."] = new_project
            df_clean.at[idx, "What Should A Volunteer Bring for the Day? e.g., gloves, sun screen, bug spray, etc."] = new_bring
            df_clean.at[idx, "Special Instructions: e.g., closed-toe shoes, working near water, bring a change of clothes if desired, etc."] = new_instructions
            
            st.session_state.cleaned_df = df_clean
            st.success("✅ Event saved!")
            st.balloons()
    
    # Show cleaned data preview
    st.subheader("Cleaned Data Preview")
    st.dataframe(df_clean, use_container_width=True)
    
    # Download cleaned CSV
    st.subheader("Download Cleaned Data")
    
    csv_buffer = io.StringIO()
    df_clean.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv_data,
            file_name="yspd_events_cleaned.csv",
            mime="text/csv"
        )
    
    with col2:
        if st.button("✅ Use Cleaned Data for Templates"):
            st.session_state.df = df_clean  # Replace original with cleaned version
            st.success("Cleaned data is now active! Go to Generate Templates.")

elif page == "4. Generate Templates":
    if 'df' not in st.session_state:
        st.warning("⚠️ Please upload your data first!")
        st.stop()
    
    st.header("Step 3: Generate Email Templates")
    
    df = st.session_state.df
    
    # Template selection
    st.subheader("Select Templates to Generate")
    
    col1, col2 = st.columns(2)
    
    with col1:
        template_14_day = st.checkbox("14-Day Reminder Email", value=True)
        template_3_day = st.checkbox("3-Day Reminder Email", value=True)
    
    with col2:
        template_day_before = st.checkbox("Day Before Reminder Email", value=True)
        
    # Event selection
    st.subheader("Select Events")
    
    if st.checkbox("Generate for all events", value=True):
        selected_events = df.index.tolist()
    else:
        # Multi-select for specific events
        park_names = df["Chapter/Park Name"].tolist()
        selected_parks = st.multiselect("Choose specific parks:", park_names)
        selected_events = df[df["Chapter/Park Name"].isin(selected_parks)].index.tolist()
    
    # Generate button
    if st.button("🚀 Generate Templates", type="primary"):
        if not any([template_14_day, template_3_day, template_day_before]):
            st.error("Please select at least one template type!")
        elif not selected_events:
            st.error("Please select at least one event!")
        else:
            st.success(f"Generating templates for {len(selected_events)} events...")
            
            # Generate templates for selected events
            generated_files = []
            
            for idx in selected_events:
                event = df.iloc[idx]
                park_name = event["Chapter/Park Name"]
                
                # Clean up park name for filename
                safe_park_name = "".join(c for c in park_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
                safe_park_name = safe_park_name.replace(' ', '_')
                
                if template_14_day:
                    html_content = generate_14_day_template(event)
                    filename = f"{safe_park_name}_14_day_reminder.html"
                    generated_files.append((filename, html_content))
                
                if template_3_day:
                    html_content = generate_3_day_template(event)
                    filename = f"{safe_park_name}_3_day_reminder.html"
                    generated_files.append((filename, html_content))
                
                if template_day_before:
                    html_content = generate_day_before_template(event)
                    filename = f"{safe_park_name}_day_before_reminder.html"
                    generated_files.append((filename, html_content))
            
            st.success(f"✅ Generated {len(generated_files)} template files!")
            
            # Show first few as preview
            st.subheader("Preview Generated Templates")
            
            for i, (filename, content) in enumerate(generated_files[:3]):
                with st.expander(f"Preview: {filename}"):
                    # Show rendered HTML
                    st.components.v1.html(content, height=600, scrolling=True)
                    
                    # Option to view raw HTML if needed
                    if st.checkbox(f"Show HTML code for {filename}", key=f"show_code_{i}"):
                        st.code(content, language="html")
                    
                    # Download button for individual file
                    st.download_button(
                        label=f"📥 Download {filename}",
                        data=content,
                        file_name=filename,
                        mime="text/html"
                    )
            
            # Bulk download option
            if len(generated_files) > 1:
                st.subheader("Download All Templates")
                
                # Create a zip file with all templates
                import zipfile
                zip_buffer = io.BytesIO()
                
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for filename, content in generated_files:
                        zip_file.writestr(filename, content)
                
                zip_buffer.seek(0)
                
                st.download_button(
                    label="📦 Download All Templates as ZIP",
                    data=zip_buffer.getvalue(),
                    file_name="yspd_email_templates.zip",
                    mime="application/zip"
                )

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit for Friends of Georgia State Parks*")