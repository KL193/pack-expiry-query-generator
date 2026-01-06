from datetime import datetime
import calendar

# Get current year & month
now = datetime.now()
year = now.year
month = now.month

# Get last day of the current month
last_day = calendar.monthrange(year, month)[1]
end_date = f"{year}-{month:02d}-{last_day}"

# Build query
query = f'''
SELECT JSON_UNQUOTE(JSON_EXTRACT(pack_definitions, "$.shortCode"))
FROM ops_revamp.ops_pack
WHERE LOWER(JSON_UNQUOTE(JSON_EXTRACT(pack_definitions, "$.endDate"))) = "{end_date}"
  AND deactivation = 0
  AND status = 1
LIMIT 250;
'''

print("Auto-generated End Date:", end_date)
print(query)
