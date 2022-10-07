# 1) Set email vairiables to be empty dictionary 
emails = {}

assert emails == {}, f"Expected `emails` to be {{}} but got: {repr(emails)}

# 2) Add users and emails 
emails['ashley'] = 'ashley@example.com'
emails['song'] = 'song@example.com'
emails['Gilbert'] = 'gilbert@example.com'


assert emails == {
    "ashley": "ashley@example.com",
    "song": "song@example.com",
    "gilbert": "gilbert@example.com"
}, f"Expected `emails` to be {{'ashley': 'ashley@example.com', 'song': 'song@example.com', 'gilbert': gilbert@example.com}}

## Check assigment to complete this
