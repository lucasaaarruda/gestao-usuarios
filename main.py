from flask import Flask
from configuracao import configure_tudo

# Incialização
app = Flask(__name__)

# Rotas - Blueprints
configure_tudo(app)

# Execução
app.run(debug=True)