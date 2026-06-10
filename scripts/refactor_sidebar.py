import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The original block is between `<nav class="tabs" aria-label="Views">` and `</nav>`
nav_start = html.find('<nav class="tabs" aria-label="Views">')
nav_end = html.find('</nav>', nav_start) + len('</nav>')

nav_block = html[nav_start:nav_end]

# Define the new groups
groups = {
    'OVERVIEW': ['overview', 'transactions'],
    'PROCESSING': ['intake', 'review', 'drive'],
    'INSIGHTS': ['reports', 'assistant'],
    'SYSTEM': ['settings']
}

# Extract all buttons and the spacer
buttons = {}
spacer = '<div class="sidebar-spacer"></div>'

for view in ['overview', 'transactions', 'intake', 'review', 'drive', 'reports', 'assistant', 'settings']:
    # Regex to extract the full button HTML for a specific data-view
    pattern = re.compile(r'(<button class="tab-button[^>]*data-view="' + view + r'"[^>]*>.*?</button>)', re.DOTALL)
    match = pattern.search(nav_block)
    if match:
        buttons[view] = match.group(1)

# Rebuild the nav block
new_nav = '<nav class="tabs" aria-label="Views">\n'

for group_name, views in groups.items():
    if group_name == 'SYSTEM':
        new_nav += f'          {spacer}\n'
    new_nav += f'          <div class="nav-group">\n'
    new_nav += f'            <span class="nav-section-title">{group_name}</span>\n'
    for view in views:
        if view in buttons:
            new_nav += '            ' + buttons[view].replace('\n', '\n            ') + '\n'
    new_nav += f'          </div>\n'

new_nav += '        </nav>'

# Replace in html
if new_nav != '<nav class="tabs" aria-label="Views">\n        </nav>':
    html = html[:nav_start] + new_nav + html[nav_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully refactored the sidebar HTML.")
else:
    print("Failed to build new nav block.")
