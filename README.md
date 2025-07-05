# Servidor MCP en Python 🚀

Servidor básico de **Model Context Protocol** con herramientas personalizadas para Claude Desktop.

## ¿Qué incluye?

- **Calculadora**: Suma dos números
- **Generador de saludos**: Saludos en español, inglés y francés

## Instalación rápida

```bash
# Clonar y setup
git clone https://github.com/TU_USUARIO/MCP-PYTHON.git
cd MCP-PYTHON
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt

# Ejecutar
python server_minimo.py
```

## Configurar Claude Desktop

Edita `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "MI-MCP": {
      "command": "C:\\ruta\\a\\tu\\venv\\Scripts\\python.exe",
      "args": ["C:\\ruta\\a\\tu\\server_minimo.py"]
    }
  }
}
```

Reinicia Claude Desktop y prueba:
- *"Suma 15 y 27"*
- *"Saluda a Ana en inglés"*

## Recursos

- 📖 [Artículo completo](./articulo-devto.md)
- 🌐 [Documentación MCP](https://modelcontextprotocol.io/)
