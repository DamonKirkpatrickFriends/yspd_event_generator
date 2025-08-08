from utils import safe_get

def generate_3_day_template(event):
    """Generate the 3-day reminder email template with inline styling matching YSPDMain.html"""
    
    park_name = safe_get(event, "Chapter/Park Name")
    coordinator_name = safe_get(event, "Volunteer Coordinator Name")
    coordinator_email = safe_get(event, "Volunteer Coordinator Email")
    coordinator_phone = safe_get(event, "Volunteer Coordinator Phone")
    project_description = safe_get(event, "Describe the project(s) that are planned at your site.")
    meeting_location = safe_get(event, "Specific meeting location - e.g., Visitor Center, Group Shelter 1.")
    meeting_time = safe_get(event, "Meeting Time")
    what_to_bring = safe_get(event, "What Should A Volunteer Bring for the Day? e.g., gloves, sun screen, bug spray, etc.")
    special_instructions = safe_get(event, "Special Instructions: e.g., closed-toe shoes, working near water, bring a change of clothes if desired, etc.")
    refreshments = safe_get(event, "Will snacks, lunch, water, be provided?")
    
    event_date = "{event.start_date}"
    
    # Convert what_to_bring to bullet points
    if what_to_bring:
        bring_items = [item.strip() for item in what_to_bring.split(',') if item.strip()]
    else:
        bring_items = ["Work gloves", "Water bottle", "Closed-toe shoes"]
    
    bring_list = "".join([f"<tr><td style='padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;'>• {item}</td></tr>" for item in bring_items])
    
    # Handle special instructions section and other "Need to know" items
    need_to_know_items = []
    
    if special_instructions:
        need_to_know_items.append(f'''
        <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
            <strong style="color: #005987;">Special Instructions:</strong> {special_instructions}
        </p>''')
    
    if refreshments:
        need_to_know_items.append(f'''
        <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
            <strong style="color: #005987;">Refreshments provided:</strong> {refreshments}
        </p>''')
    
    # Note: Family-friendly sections would be added here if they exist in the data
    
    need_to_know_section = f"""
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
        <tr>
            <td style="padding: 20px; background-color: #f8f9fa; border-left: 3px solid #005987; border-radius: 10px; font-family: Arial, sans-serif;">
                <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                    Need to Know:
                </p>
                {''.join(need_to_know_items)}
            </td>
        </tr>
    </table>
    """ if need_to_know_items else ''
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This Weekend: Your State Parks Day!</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f8f9fa;">
    
    <!-- Main Container Table -->
    <table style="width: 100%; max-width: 800px; margin: 0 auto; border-collapse: collapse; background-color: #f8f9fa;">
        <tr>
            <td style="padding: 20px;">
                
                <!-- Header Section - Styled like countdown section -->
                <table style="width: 100%; border-collapse: collapse; background: linear-gradient(135deg, #005987 0%, #007bb8 100%); border-radius: 12px; margin-bottom: 30px;">
                    <tr>
                        <td style="padding: 30px 20px; text-align: center;">
                            <h1 style="margin: 0 0 10px 0; font-family: Arial, sans-serif; font-size: 28px; font-weight: 600; color: white; line-height: 1.2;">
                                This Weekend: Your State Parks Day!
                            </h1>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 16px; color: rgba(255,255,255,0.95); font-weight: 500;">
                                {park_name} - Your State Parks Day
                            </p>
                        </td>
                    </tr>
                </table>
                
                <!-- Opening Message -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                            <p style="margin: 0;">
                                Your State Parks Day volunteer project at <strong>{park_name}</strong> is just 3 days away! Here are the important details:
                            </p>
                        </td>
                    </tr>
                </table>
                
                <!-- Event Details - Highlight Box -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 25px; background-color: #f8f9fa; border-left: 5px solid #005987; border-radius: 12px;">
                            <table style="width: 100%; border-collapse: collapse;">
                                <tr>
                                    <td style="padding: 8px 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                                        <strong style="color: #005987;">Project:</strong> {project_description}
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                                        <strong style="color: #005987;">Date & Time:</strong> {{event.start_date}} - {{event.end_date}}
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                                        <strong style="color: #005987;">Specific Meeting Location:</strong> {meeting_location}
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                
                <!-- Logo -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="text-align: center;">
                            <img src="https://friendsofgastateparks.org/sites/default/files/styles/large/public/2025-06/YSPD-LOGO---Original.png" alt="Your State Parks Day Logo" style="max-width: 120px; height: auto; border: 0;">
                        </td>
                    </tr>
                </table>
                
                <!-- What to Bring Section - Card Style -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="padding: 25px; background-color: white; border: 2px solid #005987; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
                            <h2 style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 18px; font-weight: 600; color: #005987;">
                                What to Bring:
                            </h2>
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                                {bring_list}
                            </table>
                            
                            {need_to_know_section}
                        </td>
                    </tr>
                </table>
                
                <!-- Contact Footer - Styled like main page footer -->
                <table style="width: 100%; border-collapse: collapse; background: linear-gradient(135deg, #005987 0%, #007bb8 100%); border-radius: 12px; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 25px; text-align: center;">
                            <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 18px; font-weight: 600; color: white;">
                                Questions?
                            </p>
                            <table style="width: 100%; border-collapse: collapse;">
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: rgba(255,255,255,0.95); text-align: center;">
                                        📞 Phone: (770) 383-8900
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: rgba(255,255,255,0.95); text-align: center;">
                                        📧 Email: info@friendsofgastateparks.org
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; text-align: center;">
                                        💬 Live Chat: <a href="https://direct.lc.chat/10608367/" target="_blank" style="color: #d4af37; text-decoration: none; font-weight: 600;">Click here to chat with us</a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; text-align: center;">
                                        🌐 More Info: <a href="https://friendsofgastateparks.org/yspd2025" target="_blank" style="color: #d4af37; text-decoration: none; font-weight: 600;">friendsofgastateparks.org/yspd2025</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                
                <!-- Closing Message -->
                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 20px 0; text-align: center;">
                            <p style="margin: 0 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                                See you this weekend!
                            </p>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #666;">
                                <strong style="color: #005987;">Friends of Georgia State Parks</strong>
                            </p>
                        </td>
                    </tr>
                </table>
                
            </td>
        </tr>
    </table>
    
</body>
</html>"""
    
    return html_template