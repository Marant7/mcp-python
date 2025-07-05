#!/usr/bin/env python3
"""
Servidor MCP Mínimo - 1 Tool + 1 Prompt
Para probar conceptos básicos
"""

from mcp.server.fastmcp import FastMCP

# Crear el objeto FastMCP
mcp = FastMCP()

# ===============================
# TOOLS - Herramientas funcionales
# ===============================

@mcp.tool()
def calculadora(a: int, b: int) -> str:
    """
    Suma dos números.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        Resultado de la suma
    """
    resultado = a + b
    return f"OK {a} + {b} = {resultado}"

@mcp.tool()
def generar_saludo(nombre: str, idioma: str = "español") -> str:
    """
    Genera un saludo personalizado en diferentes idiomas.
    
    Args:
        nombre: Nombre de la persona
        idioma: "español", "ingles" o "frances"
    
    Returns:
        Saludo personalizado
    """
    saludos = {
        "español": f"Hola {nombre}, que tengas un excelente dia!",
        "ingles": f"Hello {nombre}, have a great day!",
        "frances": f"Bonjour {nombre}, passez une excellente journee!"
    }
    
    return saludos.get(idioma.lower(), saludos["español"])

if __name__ == "__main__":
    print("Servidor MCP Minimo iniciado...")
    print("2 Tools disponibles:")
    print("  - calculadora: suma dos numeros")
    print("  - generar_saludo: crea saludos personalizados")
    print("Listo para probar!")
    mcp.run()
