{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMJjDaaN+GdyR572w0T0ak8",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Mrlexintong1/Calculadora-IMC-en-Phyton/blob/main/calculadora_imc.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GvBcNoXUax35",
        "outputId": "7fc6fb56-3b5c-4397-a197-c3b3021aa08b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Escribe tu nombre: carlos\n",
            "Hola, carlos, ¿cuántos años tienes? 32\n",
            "Hola, carlos, ¿cuál es tu altura en metros? 1.70\n",
            "Hola, carlos, ¿cuál es tu peso en kilogramos? 60\n",
            "\n",
            "Hola, carlos, tienes 32 años y mides 1.7 metros.\n",
            "Tu IMC es: 20.76\n",
            "Clasificación: peso normal\n"
          ]
        }
      ],
      "source": [
        "# Programa que solicita nombre, edad y altura, y calcula el IMC\n",
        "def obtener_datos_usuario():\n",
        "    nombre = input(\"Cual es tu nombre: \")\n",
        "    edad = int(input(f\"Hola, {nombre}, ¿cuántos años tienes? \"))\n",
        "    altura = float(input(f\"Hola, {nombre}, ¿cuál es tu altura ? \"))\n",
        "    peso = float(input(f\"Hola, {nombre}, ¿cuál es tu peso en kilogramos? \"))\n",
        "\n",
        "    return nombre, edad, altura, peso\n",
        "\n",
        "def calcular_imc(peso, altura):\n",
        "    return peso / (altura ** 2)\n",
        "\n",
        "# Llamamos a las funciones\n",
        "nombre, edad, altura, peso = obtener_datos_usuario()\n",
        "\n",
        "# Mostramos los datos\n",
        "print(f\"\\nHola, {nombre}, tienes {edad} años y mides {altura} metros.\")\n",
        "\n",
        "# Calculamos y mostramos el IMC\n",
        "imc = calcular_imc(peso, altura)\n",
        "print(f\"Tu IMC es: {imc:.2f}\")\n",
        "\n",
        "# Clasificación según el IMC\n",
        "if imc < 18.5:\n",
        "    clasificacion = \"bajo peso\"\n",
        "elif 18.5 <= imc < 24.9:\n",
        "    clasificacion = \"peso normal\"\n",
        "elif 25 <= imc < 29.9:\n",
        "    clasificacion = \"sobrepeso\"\n",
        "else:\n",
        "    clasificacion = \"obesidad\"\n",
        "\n",
        "print(f\"Clasificación: {clasificacion}\")\n"
      ]
    }
  ]
}
