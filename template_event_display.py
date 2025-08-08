from utils import safe_get

def generate_event_display(event):
    """Generate the event display page for website/registration with styling matching YSPDMain.html"""
    
    park_name = safe_get(event, "Chapter/Park Name")
    coordinator_name = safe_get(event, "Volunteer Coordinator Name")
    coordinator_email = safe_get(event, "Volunteer Coordinator Email")
    coordinator_phone = safe_get(event, "Volunteer Coordinator Phone")
    project_description = safe_get(event, "Describe the project(s) that are planned at your site.")
    meeting_location = safe_get(event, "Specific meeting location - e.g., Visitor Center, Group Shelter 1.")
    meeting_time = safe_get(event, "Meeting Time")
    end_time = safe_get(event, "What time will the activities end?", "End of day")
    what_to_bring = safe_get(event, "What Should A Volunteer Bring for the Day? e.g., gloves, sun screen, bug spray, etc.")
    special_instructions = safe_get(event, "Special Instructions: e.g., closed-toe shoes, working near water, bring a change of clothes if desired, etc.")
    refreshments = safe_get(event, "Will snacks, lunch, water, be provided?")
    children_activities = safe_get(event, "Will you have activities for children? Age limit?")
    
    event_date = "September 27, 2025"
    
    # Convert what_to_bring to bullet points
    if what_to_bring:
        bring_items = [item.strip() for item in what_to_bring.split(',') if item.strip()]
    else:
        bring_items = ["Work gloves", "Water bottle", "Closed-toe shoes"]
    
    # Handle "Need to know" section grouping
    need_to_know_sections = []
    
    # Add "What to Bring" section
    if bring_items:
        bring_list_html = "".join([f"<li style='margin-bottom: 8px; font-size: 14px; line-height: 1.6; color: #333;'>{item}</li>" for item in bring_items])
        need_to_know_sections.append(f'''
    <div style="background-color: #f8f9fa; padding: 20px; margin: 20px 0; border-left: 3px solid #005987; border-radius: 10px;">
        <strong style="color: #005987; font-size: 16px;">What to Bring:</strong> 
        <ul style="margin: 10px 0; padding-left: 20px;">
            {bring_list_html}
        </ul>
    </div>''')
    
    if special_instructions:
        need_to_know_sections.append(f'''
    <div style="background-color: #f8f9fa; padding: 20px; margin: 20px 0; border-left: 3px solid #005987; border-radius: 10px;">
        <strong style="color: #005987; font-size: 16px;">Special Instructions:</strong> 
        <p style="margin: 10px 0 0 0; font-size: 14px; line-height: 1.6; color: #333;">{special_instructions}</p>
    </div>''')
    
    if refreshments:
        need_to_know_sections.append(f'''
    <div style="background-color: #f8f9fa; padding: 20px; margin: 20px 0; border-left: 3px solid #005987; border-radius: 10px;">
        <strong style="color: #005987; font-size: 16px;">Refreshments provided:</strong> 
        <p style="margin: 10px 0 0 0; font-size: 14px; line-height: 1.6; color: #333;">{refreshments}</p>
    </div>''')
    
    if children_activities:
        need_to_know_sections.append(f'''
    <div style="background-color: #f8f9fa; padding: 20px; margin: 20px 0; border-left: 3px solid #005987; border-radius: 10px;">
        <strong style="color: #005987; font-size: 16px;">Family-Friendly:</strong> 
        <p style="margin: 10px 0 0 0; font-size: 14px; line-height: 1.6; color: #333;">{children_activities}</p>
    </div>''')
    
    # Combine all sections under "What to Expect"
    need_to_know_combined = f'''
    <div class="info-section">
        <div class="section-header">What to Expect</div>
        {''.join(need_to_know_sections)}
    </div>''' if need_to_know_sections else ''
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your State Parks Day 2025 - {park_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; background-color: #f8f9fa; }}
        .header {{ background: linear-gradient(135deg, #005987 0%, #007bb8 100%); color: white; padding: 30px; text-align: center; border-radius: 12px; margin-bottom: 30px; }}
        .header h1 {{ margin: 0 0 10px 0; font-size: 2rem; font-weight: 600; line-height: 1.2; }}
        .header h2 {{ margin: 0 0 15px 0; font-size: 1.5rem; font-weight: 500; }}
        .header p {{ font-size: 1.1rem; margin: 0; opacity: 0.95; }}
        
        .event-details {{ background-color: #f8f9fa; padding: 25px; border-radius: 12px; margin: 20px 0; border-left: 5px solid #005987; }}
        .event-details h3 {{ color: #005987; margin-top: 0; font-size: 1.3rem; font-weight: 600; }}
        
        .info-section {{ background-color: white; padding: 25px; border: 2px solid #005987; margin: 20px 0; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1); }}
        .section-header {{ color: #005987; font-size: 1.25rem; font-weight: 600; margin-bottom: 15px; border-bottom: 2px solid #005987; padding-bottom: 8px; }}
        
        .register-button {{ background: linear-gradient(135deg, #005987 0%, #007bb8 100%); color: white; padding: 15px 30px; font-size: 1.1rem; font-weight: 600; text-decoration: none; border-radius: 8px; display: inline-block; margin: 20px 0; transition: all 0.3s ease; }}
        .register-button:hover {{ background: linear-gradient(135deg, #004470 0%, #006ba1 100%); transform: translateY(-1px); }}
        
        .two-column {{ display: flex; gap: 30px; margin: 20px 0; }}
        .column {{ flex: 1; }}
        
        .contact-box {{ background: linear-gradient(135deg, #005987 0%, #007bb8 100%); color: white; padding: 25px; margin-top: 20px; border-radius: 12px; text-align: center; }}
        .contact-box h3 {{ margin-top: 0; font-size: 1.3rem; font-weight: 600; }}
        .contact-box a {{ color: #d4af37; text-decoration: none; font-weight: 600; }}
        .contact-box a:hover {{ text-decoration: underline; }}
        
        ul {{ margin: 10px 0; padding-left: 20px; }}
        li {{ margin-bottom: 8px; font-size: 14px; line-height: 1.6; }}
        
        @media (max-width: 768px) {{ 
            .two-column {{ flex-direction: column; gap: 15px; }}
            body {{ padding: 10px; }}
            .header {{ padding: 20px; }}
            .header h1 {{ font-size: 1.5rem; }}
            .header h2 {{ font-size: 1.2rem; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Your State Parks Day 2025</h1>
        <h2>{park_name}</h2>
        <p>Join us for a day of conservation and community service!</p>
    </div>
    
    <div class="event-details">
        <h3>Event Details</h3>
        <div class="two-column">
            <div class="column">
                <p><strong style="color: #005987;">📅 Date:</strong> {event_date}</p>
                <p><strong style="color: #005987;">🕘 Time:</strong> {meeting_time} - {end_time}</p>
                <p><strong style="color: #005987;">📍 Specific Meeting Location:</strong> {meeting_location}</p>
            </div>
            <div class="column">
                <p><strong style="color: #005987;">🎯 Project:</strong></p>
                <p>{project_description}</p>
            </div>
        </div>
    </div>
    
    <div style="text-align: center;">
        <a href="#registration-form" class="register-button">REGISTER BELOW</a>
    </div>
    
    <div class="info-section">
        <div class="section-header">About Your State Parks Day</div>
        
        <img alt="Your State Parks Day Logo" src="https://friendsofgastateparks.org/sites/default/files/styles/large/public/2025-06/YSPD-LOGO---Original.png" style="float:right;max-width:150px;height:auto;margin:0 0 15px 20px;" />
        
        <p><strong>About Your State Parks Day:</strong> Join Friends of Georgia State Parks for a statewide day of service! Volunteers across all 63 Georgia State Parks and Historic Sites will come together to help preserve and enhance these treasured natural and cultural resources.</p>
        
        <div style="clear:both;"></div>
    </div>
    
    {need_to_know_combined}
    
    <div class="info-section">
        <div class="section-header">Important Information</div>
        
        <p><strong>Weather Policy:</strong> This is an outdoor event. Inclement weather may force cancellation. Check with the park if you have questions on the day of the event.</p>
        
        <p><strong>What's Provided:</strong> All tools and equipment will be provided unless otherwise noted.</p>
    </div>
    
    <div class="contact-box">
        <h3>Questions? Contact Friends of Georgia State Parks</h3>
        <p><strong>📞 Phone:</strong> (770) 383-8900<br>
        📧 <strong>Email:</strong> info@friendsofgastateparks.org<br>
        💬 <strong>Live Chat:</strong> <a href="https://direct.lc.chat/10608367/" target="_blank">Click here to chat with us</a><br>
        🌐 <strong>More Info:</strong> <a href="https://friendsofgastateparks.org/yspd2025" target="_blank">friendsofgastateparks.org/yspd2025</a></p>
    </div>
    
</body>
</html>"""
    
    return html_template