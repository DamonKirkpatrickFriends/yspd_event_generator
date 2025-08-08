from utils import safe_get

def generate_registration_confirmation(event):
    """Generate the registration confirmation email with inline styling matching YSPDMain.html"""
    
    park_name = safe_get(event, "Chapter/Park Name")
    coordinator_name = safe_get(event, "Volunteer Coordinator Name")
    coordinator_email = safe_get(event, "Volunteer Coordinator Email")
    coordinator_phone = safe_get(event, "Volunteer Coordinator Phone")
    project_description = safe_get(event, "Describe the project(s) that are planned at your site.")
    meeting_location = safe_get(event, "Specific meeting location - e.g., Visitor Center, Group Shelter 1.")
    meeting_time = safe_get(event, "Meeting Time")
    what_to_bring = safe_get(event, "What Should A Volunteer Bring for the Day? e.g., gloves, sun screen, bug spray, etc.")
    special_instructions = safe_get(event, "Special Instructions: e.g., closed-toe shoes, working near water, bring a change of clothes if desired, etc.")
    
    event_date = "{event.start_date}"
    
    # Improved what_to_bring list generation
    bring_items = ["Work gloves (if you have them)", "Water bottle", "Sunscreen and bug spray", "Closed-toe shoes"]
    
    # Check for additional user-provided items and avoid duplicates
    if what_to_bring:
        user_items = [item.strip() for item in what_to_bring.split(',') if item.strip()]
        for item in user_items:
            # Check if it's not a duplicate of standard items
            if item.lower() not in [b.split(' ')[0].lower() for b in bring_items]:
                bring_items.append(item)
    
    bring_list = "".join([f"<tr><td style='padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;'>• {item}</td></tr>" for item in bring_items])
    
    # Handle special instructions section and other "Need to know" items
    need_to_know_items = []
    
    if special_instructions:
        need_to_know_items.append(f'''
        <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
            <strong style="color: #005987;">Special Instructions:</strong> {special_instructions}
        </p>''')
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Confirmed - Your State Parks Day</title>
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
                                ✅ Registration Confirmed!
                            </h1>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 16px; color: rgba(255,255,255,0.95); font-weight: 500;">
                                Your State Parks Day - {park_name}
                            </p>
                        </td>
                    </tr>
                </table>
                
                <!-- Success Message - Card Style -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px; background-color: white; border-radius: 12px;" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="padding: 25px; border: 2px solid #005987; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
                            <h2 style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 22px; font-weight: 600; color: #005987; line-height: 1.3;">
                                Thank you for registering!
                            </h2>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                                You're all set for <strong>{park_name} - Your State Parks Day</strong>! We're excited to have you join us for this statewide day of service.
                            </p>
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
                
                <!-- What Happens Next Section - Card Style -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 25px; background-color: white; border: 2px solid #005987; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
                            <h3 style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 20px; font-weight: 600; color: #005987; border-bottom: 2px solid #005987; padding-bottom: 8px;">
                                What Happens Next?
                            </h3>
                            
                            <p style="margin: 0 0 20px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                We'll send you reminder emails leading up to the event with all the important details. In the meantime, here's what you need to know:
                            </p>
                            
                            <p style="margin: 0 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                What to Bring:
                            </p>
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                                {bring_list}
                            </table>
                            
                            <p style="margin: 20px 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                Need to Know:
                            </p>
                            {''.join(need_to_know_items) if need_to_know_items else ''}
                            
                            <p style="margin: 20px 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                General Guidelines:
                            </p>
                            <table style="width: 100%; border-collapse: collapse;">
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Dress appropriately for outdoor work and weather conditions
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • All tools and equipment will be provided unless otherwise noted
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Most projects are suitable for ages 12 and up (minors must be accompanied by an adult)
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Event may be cancelled due to severe weather
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                
                <!-- Important Safety and Legal Information - Card Style -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 25px; background-color: white; border: 2px solid #005987; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
                            <h3 style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 20px; font-weight: 600; color: #005987; border-bottom: 2px solid #005987; padding-bottom: 8px;">
                                Important Information
                            </h3>
                            
                            <p style="margin: 0 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                Your Safety Matters:
                            </p>
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Volunteer activities involve some natural risks (outdoor work, equipment use, etc.)
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • You're responsible for following safety guidelines and using equipment properly
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Friends of Georgia State Parks provides guidance but cannot guarantee against all risks
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 20px 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                Photo Permission:
                            </p>
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • We may take photos/videos during volunteer activities
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • These help us share the great work volunteers do and apply for grants
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Your participation gives us permission to use these images
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 20px 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                The Legal Stuff:
                            </p>
                            <table style="width: 100%; border-collapse: collapse;">
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • As a volunteer, you're not an employee and aren't covered by workers' compensation
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • You agree not to hold us liable for injuries that might occur
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                
                <!-- Contact Footer - Styled like main page footer -->
                <table style="width: 100%; border-collapse: collapse; background: linear-gradient(135deg, #005987 0%, #007bb8 100%); border-radius: 12px; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 25px; text-align: center;">
                            <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 18px; font-weight: 600; color: white;">
                                Questions before the event?
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
                                We can't wait to see you on Your State Parks Day!
                            </p>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #666;">
                                Thank you for helping serve, support, and celebrate Georgia's state parks and historic sites,<br>
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