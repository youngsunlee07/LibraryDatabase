import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime, timedelta
from database_connection import connect_db, close_db

def send_email(subject, body, to_email):
    from_email = "your_email@gmail.com"
    from_password = "your_email_password"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

def check_overdue_documents():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        overdue_date = datetime.now() - timedelta(days=14)  # Documents borrowed more than 2 weeks ago
        # Find overdue documents
        cursor.execute("""
            SELECT br.member_id, br.document_id, br.due_date, u.email 
            FROM BorrowRecords br
            JOIN Users u ON br.member_id = u.id
            WHERE br.return_date IS NULL AND br.due_date < %s
        """, (overdue_date,))

        overdue_records = cursor.fetchall()
        for record in overdue_records:
            member_id, document_id, due_date, email = record
            print(f"Notice: Member {member_id} has overdue document {document_id} (due date was {due_date}).")
            send_email(
                subject="Overdue Document Notice",
                body=f"Dear Member {member_id},\n\nYou have an overdue document (ID: {document_id}). The due date was {due_date}.\n\nPlease return it as soon as possible.",
                to_email=email
            )

    except Exception as e:
        print("Failed to check overdue documents:", e)
    finally:
        cursor.close()
        close_db(conn)

# Schedule the check_overdue_documents function to run daily at 10:00 AM
schedule.every().day.at("10:00").do(check_overdue_documents)

print("Scheduler started")
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait 60 seconds between checks
