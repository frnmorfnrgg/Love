from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'banco_de_dados.json'

DEFAULT_DATA = {
    "startDate": "2025-06-12T20:00",
    "nextMilestoneName": "Nosso Aniversário de Namoro 💖",
    "nextMilestoneDate": "2026-06-12T00:00",
    "dailyMessages": [
        "Domingo lindo! Só consigo pensar em ficar coladinho com você assistindo filme. Te amo, Klara! ❤️",
        "Boa segunda, minha princesa! Que sua semana seja leve assim como o seu sorriso. 🥰",
        "Passando na sua terça pra lembrar que você é o amor da minha vida inteira! 🌹",
        "Quarta-feira! Metade da semana e meu amor por você só cresce a cada segundo. 💖",
        "Quinta-feira pede um abraço bem apertado daqueles que só você sabe dar. ✨",
        "Sextoooou! Mal posso esperar para passar o fim de semana rindo ao seu lado. 🥂",
        "Sábado é dia de celebrar a sorte que tenho de ter você na minha vida. 🧸"
    ],
    "mainLetter": {
        "title": "Para a Klara, o amor da minha vida...",
        "text": "Escrevi esse cantinho para registrar um pouquinho do infinito que sinto por você. Obrigado por ser minha companheira e o meu porto seguro mais lindo. Te amo!"
    },
    "sealedLetters": [
        { "title": "Feliz Aniversário, meu amor! 🎉", "text": "Hoje o dia é todo seu, mas o presente quem ganhou fui eu quando você entrou na minha vida. Parabéns, linda! 🎂" },
        { "title": "Para quando o dia estiver cinza... ☁️", "text": "Ei, olha para mim. Respira fundo. Lembre-se de que você é uma mulher forte e incrível. Vai dar tudo certo! 🧸" },
        { "title": "Feliz Nosso Aniversário de Namoro! 💖", "text": "Mais um marco para a nossa conta! Olho para trás e sinto um orgulho imenso de tudo o que superamos. Feliz nosso dia!" }
    ],
    "timeline": [
        { "date": "12/03/2025", "title": "O Dia que te Conheci", "desc": "Aquele olhar que mudou completamente o rumo da minha história.", "img": "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=500" },
        { "date": "20/04/2025", "title": "Nosso Primeiro Beijo", "desc": "A certeza de que eu não queria mais largar você.", "img": "https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=500" }
    ],
    "galleryCategories": ["Todos", "Viagens", "Encontros"],
    "gallery": [
        { "cat": "Viagens", "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=500", "caption": "Nossa primeira viagem vendo o mar juntos!" },
        { "cat": "Encontros", "img": "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?w=500", "caption": "Aquele jantar onde rimos até a barriga doer." }
    ],
    "playlist": [
        { "title": "Partilhar", "artist": "Rubel", "desc": "Quando eu só queria dividir a vida com você.", "cover": "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=150", "src": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" }
    ],
    "quiz": [
        { "q": "Onde foi o nosso primeiro encontro oficial?", "opts": ["No Cinema", "No Parque", "Numa Lanchonete"], "ans": 1 },
        { "q": "Quem disse 'Te amo' primeiro?", "opts": ["Eu", "Você", "Os dois juntos"], "ans": 0 }
    ],
    "dreams": [
        { "text": "Fazer uma viagem juntos", "done": False },
        { "text": "Adotar um filhote", "done": True }
    ],
    "hugPhrases": ["Abraço forte enviado! ❤️", "Queria estar aí contigo agora... 🥰", "Recarga de carinho efetuada! ✨"]
}

def load_db():
    if not os.path.exists(DATA_FILE):
        save_db(DEFAULT_DATA)
        return DEFAULT_DATA
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_db(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/api/dados', methods=['GET'])
def get_dados():
    return jsonify(load_db())

@app.route('/api/salvar', methods=['POST'])
def salvar_dados():
    nova_config = request.json
    save_db(nova_config)
    return jsonify({"status": "sucesso", "message": "Dados salvos!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
