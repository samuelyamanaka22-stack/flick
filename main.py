from flask import Flask
import random
app = Flask(__name__)
@app.route("/")
def hello_world():
    return  '<a href="/random">Profile</a>'
@app.route("/random")
def perfil():
    facts_list=["https://i.kym-cdn.com/editorials/icons/mobile/000/014/510/great-meme-reset-2026.jpg","https://uploads.dailydot.com/2024/12/FaStfat2-2024_Memes.jpg?q=65&auto=format&w=1200&ar=2:1&fit=crop","https://brobible.com/wp-content/uploads/2023/06/funny-meme-about-viral-videos.jpg?resize=354"]
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)
