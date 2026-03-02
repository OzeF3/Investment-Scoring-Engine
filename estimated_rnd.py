
import requests

API_URL = "https://api.yourprovider.com/v1/stock/AAPL/income_statement"
API_KEY = "YOUR_API_KEY_HERE"

response = requests.get(API_URL, headers={"Authorization": f"Bearer {API_KEY}"})
data = response.json()

# רשימת רבעונים
quarters = data['data']['income_statement']

# סכום שנתי
total_revenue = sum(q['revenue'] for q in quarters)
total_opex = sum(q['operating_expense'] for q in quarters)

# שימוש ב-opex כפרוקסי ל-R&D
# אפשר לשנות את האחוז לפי הערכתך
RND_ESTIMATED_PERCENT = 0.2
estimated_rnd = total_opex * RND_ESTIMATED_PERCENT

# R&D to Revenue %
rnd_to_revenue = (estimated_rnd / total_revenue) * 100

print(f"Total Revenue (year): {total_revenue:,}")
print(f"Estimated R&D (20% of OPEX): {estimated_rnd:,}")
print(f"R&D to Revenue (%): {rnd_to_revenue:.2f}%")