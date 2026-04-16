import json

with open('../../data/step4_output.json') as f:
    data = json.load(f)

overdue = len([t for t in data if t.get('sla_status') == 'OVERDUE'])
at_risk = len([t for t in data if t.get('sla_status') == 'AT RISK'])
on_track = len([t for t in data if t.get('sla_status') == 'ON TRACK'])
closed = len([t for t in data if t.get('sla_status') == 'CLOSED'])
total = len(data)
compliance = round((on_track + closed) / total * 100)

ticket_rows = ""
for t in data:
    ticket_rows += f"<tr><td>{t['ticket_id']}</td><td>{t['hostname']}</td><td>{t['owner']}</td><td>{t['sla_status']}</td></tr>\n"

html = f"""<html>
<head><style>
body {{ font-family: Arial; padding: 20px; background: #1a1a2e; color: white; }}
h1 {{ color: #2e75b6; }}
table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
th {{ background: #1b3a5c; padding: 12px; text-align: left; }}
td {{ padding: 10px; border-bottom: 1px solid #333; }}
</style></head>
<body>
<h1>Weekly TVM Report</h1>
<p>Total Tickets: {total}</p>
<p>SLA Compliance: {compliance}%</p>
<table>
<tr><th>Status</th><th>Count</th></tr>
<tr><td>Overdue</td><td>{overdue}</td></tr>
<tr><td>At Risk</td><td>{at_risk}</td></tr>
<tr><td>On Track</td><td>{on_track}</td></tr>
<tr><td>Closed</td><td>{closed}</td></tr>
</table>
<h2>Ticket Details</h2>
<table>
<tr><th>Ticket</th><th>Host</th><th>Owner</th><th>Status</th></tr>
{ticket_rows}
</table>
</body></html>"""

with open('report.html', 'w') as f:
    f.write(html)