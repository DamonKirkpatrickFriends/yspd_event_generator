from utils import safe_get

def generate_14_day_template(event):
    """Generate the 14-day reminder email template with inline styling matching YSPDMain.html"""
    
    # Map CSV columns to template variables
    park_name = safe_get(event, "Chapter/Park Name")
    coordinator_name = safe_get(event, "Volunteer Coordinator Name")
    coordinator_email = safe_get(event, "Volunteer Coordinator Email")
    coordinator_phone = safe_get(event, "Volunteer Coordinator Phone")
    project_description = safe_get(event, "Describe the project(s) that are planned at your site.")
    meeting_location = safe_get(event, "Specific meeting location - e.g., Visitor Center, Group Shelter 1.")
    meeting_time = safe_get(event, "Meeting Time")
    
    event_date = "{event.start_date}"
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your State Parks Day is Almost Here!</title>
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
                                Your State Parks Day is Almost Here!
                            </h1>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 16px; color: rgba(255,255,255,0.95); font-weight: 500;">
                                Two weeks to go - {park_name} - Your State Parks Day
                            </p>
                        </td>
                    </tr>
                </table>
                
                <!-- Opening Message -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                            <p style="margin: 0;">
                                We're excited that you've registered for <strong>{park_name} - Your State Parks Day</strong>! In just two weeks, you'll join hundreds of volunteers for a statewide day of service at Georgia State Parks & Historic Sites.
                            </p>
                        </td>
                    </tr>
                </table>
                
                <!-- Project Description - Highlight Box -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 25px; background-color: #f8f9fa; border-left: 5px solid #005987; border-radius: 12px;">
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #333;">
                                <strong style="color: #005987;">Your Project:</strong> {project_description}
                            </p>
                        </td>
                    </tr>
                </table>
                
                <!-- Event Details -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
                    <tr>
                        <td style="padding: 0; font-family: Arial, sans-serif; font-size: 16px; line-height: 1.8; color: #333;">
                            <p style="margin: 0 0 8px 0;"><strong style="color: #005987;">Date & Time:</strong> {{event.start_date}} - {{event.end_date}}</p>
                            <p style="margin: 0;"><strong style="color: #005987;">Specific Meeting Location:</strong> {meeting_location}</p>
                        </td>
                    </tr>
                </table>
                
                <!-- Main Information Section - Card Style -->
                <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="padding: 25px; background-color: white; border: 2px solid #005987; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,89,135,0.1);">
                            <h2 style="margin: 0 0 20px 0; font-family: Arial, sans-serif; font-size: 20px; font-weight: 600; color: #005987; border-bottom: 2px solid #005987; padding-bottom: 8px;">
                                General Information - Your State Parks Day
                            </h2>
                            
                            <!-- Logo and About Section -->
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                                <tr>
                                    <td style="width: 120px; vertical-align: top; padding-right: 15px;">
                                        <img src="https://friendsofgastateparks.org/sites/default/files/styles/large/public/2025-06/YSPD-LOGO---Original.png" alt="Your State Parks Day Logo" style="max-width: 120px; height: auto; border: 0;">
                                    </td>
                                    <td style="vertical-align: top; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        <p style="margin: 0 0 15px 0;">
                                            <strong>About Your State Parks Day:</strong><br>
                                            Your State Parks Day is our biggest volunteer event of the year. It is a statewide celebration of stewardship. Volunteers gather at parks and historic sites across Georgia to serve, support, and celebrate these treasured places, preserving their beauty and history for generations to come. Whether it's your first time volunteering or your fiftieth, the day has a lasting impact on our parks and the people who care for them.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- About Friends Section -->
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #f8f9fa; border-left: 3px solid #005987; border-radius: 10px;">
                                        <p style="margin: 0 0 5px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                            About Friends of Georgia State Parks
                                        </p>
                                        <p style="margin: 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                            Friends of Georgia State Parks & Historic Sites is a nonprofit organization that serves, supports, and celebrates Georgia's state parks and historic sites. Through volunteer service, fundraising, and community partnerships, we help enhance visitor experiences and strengthen the connection between people and Georgia's most important treasures.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- General Guidelines -->
                            <h3 style="margin: 20px 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                General Guidelines:
                            </h3>
                            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Dress appropriately for the project and weather conditions
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Bring plenty of water and sunscreen
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • All tools and equipment will be provided unless otherwise noted
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                        • Most projects are suitable for ages 12 and up, younger volunteers will need extra help (minors must be accompanied by an adult)
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Weather Policy -->
                            <h3 style="margin: 20px 0 10px 0; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600; color: #005987;">
                                Weather Policy:
                            </h3>
                            <p style="margin: 0; font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #333;">
                                Inclement weather may force cancellation of some events. Check with the park if you have questions on the day of.
                            </p>
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
                                We can't wait to see you in two weeks!
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