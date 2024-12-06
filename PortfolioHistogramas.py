import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Función para calcular la rentabilidad mensual del portafolio
def calculate_monthly_returns(data, weights):
    weights = [w / 100 for w in weights]  # Convertir pesos a proporciones
    portfolio_values = (data * weights).sum(axis=1)  # Calcular cotización ponderada diaria
    monthly_prices = portfolio_values.resample('M').last()  # Último precio de cada mes
    monthly_returns = monthly_prices.pct_change() * 100  # Rentabilidad mensual en %
    return portfolio_values, monthly_returns

# Función para calcular la rentabilidad anual acumulada
def calculate_annual_return(portfolio_values):
    return ((portfolio_values[-1] / portfolio_values[0]) - 1) * 100  # Rentabilidad anual acumulada en %

# Función para graficar todos los histogramas en una sola figura
def plot_all_years(returns_dict, annual_returns_dict):
    num_years = len(returns_dict)
    cols = 2  # Número de columnas en la cuadrícula
    rows = math.ceil(num_years / cols)  # Calcular las filas necesarias

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows), constrained_layout=True)
    axes = axes.flatten()  # Convertir los ejes a una lista para facilitar la iteración

    for i, (year, returns) in enumerate(returns_dict.items()):
        colors = ['darkgreen' if r > 0 else 'darkred' for r in returns]  # Colores para positivos y negativos
        axes[i].bar(returns.index.strftime('%b'), returns, color=colors, edgecolor='black')
        axes[i].axhline(0, color='black', linewidth=0.8, linestyle='--')  # Línea en 0 para referencia
        axes[i].set_title(f"Año {year} - Rentabilidad Anual: {annual_returns_dict[year]:.2f}%")
        axes[i].set_ylabel("Rentabilidad (%)")
        axes[i].set_xlabel("Mes")
        axes[i].grid(axis='y', linestyle='--', alpha=0.7)

    # Eliminar ejes vacíos si sobran
    for ax in axes[num_years:]:
        ax.set_visible(False)

    plt.show()

# Entrada del usuario
tickers = input("Ingrese los tickers separados por comas (ej: AAPL,MSFT): ").strip()
weights = input("Ingrese los pesos correspondientes separados por comas (ej: 50,50): ").strip()
years_input = input("Ingrese los años separados por comas (ej: 2020,2021,2022): ").strip()

try:
    # Procesar entradas
    ticker_list = [ticker.strip() for ticker in tickers.split(",")]
    weight_list = [float(weight.strip()) for weight in weights.split(",")]
    years = [int(year.strip()) for year in years_input.split(",")]

    if len(ticker_list) != len(weight_list):
        raise ValueError("El número de tickers no coincide con el número de pesos.")

    # Validar que los pesos sumen 100
    if sum(weight_list) != 100:
        raise ValueError("Los pesos no suman 100%. Por favor, ajuste los valores.")

    # Descargar datos históricos desde diciembre del año anterior al primer año hasta diciembre del último año
    start_date = f"{min(years) - 1}-12-01"
    end_date = f"{max(years)}-12-31"
    data = yf.download(ticker_list, start=start_date, end=end_date)['Adj Close']

    if data.empty:
        raise ValueError("No se encontraron datos históricos para los tickers especificados en el rango indicado.")

    # Calcular rentabilidades y métricas para cada año
    returns_dict = {}
    annual_returns_dict = {}

    for year in years:
        # Calcular rentabilidad mensual del portafolio
        portfolio_values, monthly_returns = calculate_monthly_returns(data, weight_list)

        # Filtrar las rentabilidades para el año solicitado
        monthly_returns_year = monthly_returns[f"{year}-01":f"{year}-12"]

        # Calcular la rentabilidad anual acumulada
        annual_return = calculate_annual_return(portfolio_values[portfolio_values.index.year == year])

        # Almacenar en los diccionarios
        returns_dict[year] = monthly_returns_year
        annual_returns_dict[year] = annual_return

    # Graficar todos los años juntos
    plot_all_years(returns_dict, annual_returns_dict)

except Exception as e:
    print(f"Ocurrió un error: {e}")
