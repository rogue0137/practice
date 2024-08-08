# 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = []
        for email in emails:
            email_parts = email.split('@')
            email_replace_dot = email_parts[0].replace('.','')
            email_split_plus = email_replace_dot.split('+')
            email_without_plus = email_split_plus[0]
            full_email = email_without_plus + '@' + email_parts[1]
            if full_email not in unique_emails:
                unique_emails.append(full_email)
        print(unique_emails)
        return len(unique_emails)
            