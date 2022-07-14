from dataclasses import dataclass
import requests
from flask import Flask

app=Flask(__name__)

@app.route('/avantika/')
def demo_page():
    result=requests.get("https://catfact.ninja/fact")
    fact=result.json()['fact']
    data='''<!DOCTYPE html>
<html>
<body>

<h1>A fact about cat</h1>
<p>Fact: {}</p>

</body>
</html>
'''.format(fact)
    return data


app.run()
