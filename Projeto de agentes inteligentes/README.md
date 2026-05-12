Python maior que 3.11

# Instalar uv no terminal 
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.zshrc
    uv --version

# Criar ambiente virtual
    uv venv .venv

# Ativar ambiente virtual 
    .venv/bin/activate

uv init

# Instalar Pacote dotenv
uv add python-dotenv

uv add rich
