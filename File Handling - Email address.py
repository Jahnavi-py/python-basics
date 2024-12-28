#Write a program to extract email addresses from a text file.
import re
with open("file_emails.txt", "w") as file:
    file.write(
        """Here are some email addresses:
        john.doe@example.com
        jane_smith123@yahoo.com
        info@company.org
        admin@my-site.net
        contact@website.io
        invalid-email@nope@extra.com
        missing-at-sign.com"""
    )
#EXTRACTING E-mail Address we need to import re - which means regex pattern.
print("Email addresses created.")
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
with open("file_emails.txt", "r") as file:
    content = file.read()
emails = re.findall(email_pattern, content)
print("Extracted Email Addresses:")
for email in emails:
    print(email)