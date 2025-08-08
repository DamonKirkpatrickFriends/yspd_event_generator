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
    <div style="background-color: white; padding: 25px; border: 2px solid #005987; margin: 20px 0; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
        <div style="color: #005987; font-size: 1.25rem; font-weight: 600; margin-bottom: 15px; border-bottom: 2px solid #005987; padding-bottom: 8px;">What to Expect</div>
        {''.join(need_to_know_sections)}
    </div>''' if need_to_know_sections else ''
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your State Parks Day 2025 - {park_name}</title>
</head>
<body>
    
    <!-- Main Container -->
    <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; background-color: #f8f9fa;">
    
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #005987 0%, #007bb8 100%); color: white; padding: 30px; text-align: center; border-radius: 12px; margin-bottom: 30px;">
            <h1 style="margin: 0 0 10px 0; font-size: 2rem; font-weight: 600; line-height: 1.2;">Your State Parks Day 2025</h1>
            <h2 style="margin: 0 0 15px 0; font-size: 1.5rem; font-weight: 500;">{park_name}</h2>
            <p style="font-size: 1.1rem; margin: 0; opacity: 0.95;">Join us for a day of service and stewardship!</p>
        </div>
    
    <!-- Event Details -->
    <div style="background-color: #f8f9fa; padding: 25px; border-radius: 12px; margin: 20px 0; border-left: 5px solid #005987;">
        <h3 style="color: #005987; margin-top: 0; font-size: 1.3rem; font-weight: 600;">Event Details</h3>
        <div style="display: flex; gap: 30px; margin: 20px 0; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px;">
                <p style="margin: 0 0 8px 0;"><strong style="color: #005987;">📅 Date:</strong> {event_date}</p>
                <p style="margin: 0 0 8px 0;"><strong style="color: #005987;">🕘 Time:</strong> {meeting_time} - {end_time}</p>
                <p style="margin: 0;"><strong style="color: #005987;">📍 Specific Meeting Location:</strong> {meeting_location}</p>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <p style="margin: 0 0 8px 0;"><strong style="color: #005987;">🎯 Project:</strong></p>
                <p style="margin: 0;">{project_description}</p>
            </div>
        </div>
    </div>
    
    <!-- Register Button -->
    <div style="text-align: center;">
        <a href="#registration-form" style="background: linear-gradient(135deg, #005987 0%, #007bb8 100%); color: white; padding: 15px 30px; font-size: 1.1rem; font-weight: 600; text-decoration: none; border-radius: 8px; display: inline-block; margin: 20px 0; transition: all 0.3s ease;">REGISTER BELOW</a>
    </div>
    
    <!-- About Your State Parks Day -->
    <div style="background-color: white; padding: 25px; border: 2px solid #005987; margin: 20px 0; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
        <div style="color: #005987; font-size: 1.25rem; font-weight: 600; margin-bottom: 15px; border-bottom: 2px solid #005987; padding-bottom: 8px;">About Your State Parks Day</div>
        
        <img alt="Your State Parks Day Logo" src="https://friendsofgastateparks.org/sites/default/files/styles/large/public/2025-06/YSPD-LOGO---Original.png" style="float:right;max-width:150px;height:auto;margin:0 0 15px 20px;" />
        
        <p><strong>About Your State Parks Day:</strong> Join Friends of Georgia State Parks for a statewide day of service! Volunteers across all 63 Georgia State Parks and Historic Sites will come together to help preserve and enhance these treasured natural and cultural resources.</p>
        
        <div style="clear:both;"></div>
    </div>
    
    {need_to_know_combined}
    
    <!-- Important Information -->
    <div style="background-color: white; padding: 25px; border: 2px solid #005987; margin: 20px 0; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
        <div style="color: #005987; font-size: 1.25rem; font-weight: 600; margin-bottom: 15px; border-bottom: 2px solid #005987; padding-bottom: 8px;">Important Information</div>
        
        <p style="margin: 0 0 15px 0;"><strong>Weather Policy:</strong> This is an outdoor event. Inclement weather may force cancellation. Check with the park if you have questions on the day of the event.</p>
        
        <p style="margin: 0;"><strong>What's Provided:</strong> All tools and equipment will be provided unless otherwise noted.</p>
    </div>
    
    <!-- Registration Form Anchor -->
    <div id="registration-form" </div>
    
    </div> <!-- End Main Container -->
    
</body>
</html>"""
    
    return html_template