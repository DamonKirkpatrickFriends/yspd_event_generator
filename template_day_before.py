from utils import safe_get

def generate_day_before_template(event):
    """Generate the day before reminder email template with inline styling matching YSPDMain.html"""
    
    park_name = safe_get(event, "Chapter/Park Name")
    coordinator_name = safe_get(event, "Volunteer Coordinator Name")
    coordinator_phone = safe_get(event, "Volunteer Coordinator Phone")
    meeting_location = safe_get(event, "Specific meeting location - e.g., Visitor Center, Group Shelter 1.")
    meeting_time = safe_get(event, "Meeting Time")
    park_zip = safe_get(event, "Park Zip Code", "")
    
    event_date = "{event.start_date}"
    
    # Create weather URL if we have a zip code
    weather_url = f"https://forecast.weather.gov/zipcity.php?inputstring={park_zip}" if park_zip else "https://forecast.weather.gov/"
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tomorrow: Your State Parks Day!</title>
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
                                Tomorrow: Your State Parks Day!
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
                                We're excited to see you tomorrow at <strong>{park_name}</strong> for Your State Parks Day!
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
                                        <strong style="color: #005987;">Tomorrow:</strong> {{event.start_date}} - {{event.end_date}}
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
                
                <!-- Weather Warning Box - Using yellow highlight color -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 20px; background-color: #fff3cd; border-left: 3px solid #ffc107; border-radius: 10px;">
                            <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #333;">
                                🌤️ Weather Check:
                            </p>
                            <p style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                This is an outdoor volunteer project. 
                                <a href="{weather_url}" target="_blank" style="color: #005987; text-decoration: none; font-weight: 600;">
                                Click here to check tomorrow's weather forecast
                                </a> and dress appropriately!
                            </p>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                If conditions look unsafe, use your best judgement. For any last-minute cancellations, contact us using the information below.
                            </p>
                        </td>
                    </tr>
                </table>
                
                <!-- Quick Reminders - Card Style -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="padding: 25px; background-color: white; border: 2px solid #005987; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
                            <h2 style="margin: 0 0 15px 0; font-family: Arial, sans-serif; font-size: 18px; font-weight: 600; color: #005987;">
                                Quick Reminders:
                            </h2>
                            <table style="width: 100%; border-collapse: collapse;">
                                <tr>
                                    <td style="padding: 8px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        ✓ Bring your work gloves, water bottle, and closed-toe shoes
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        ✓ Dress for outdoor work and weather conditions
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 8px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        ✓ Arrive at {meeting_location} by {meeting_time}
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
                                Last-minute questions?
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
                                Thank you for helping serve, support, and celebrate Georgia's state parks and historic sites,
                            </p>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                                <strong style="color: #005987;">See you tomorrow!</strong><br>
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