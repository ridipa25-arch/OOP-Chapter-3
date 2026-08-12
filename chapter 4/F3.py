from datetime import datetime, timedelta

today = datetime.today()

print("Today's date:", today.date())
print("Date after 7 days:", (today + timedelta(days=7)).date())