# PortfolioHistogramas

## Descripción

**PortfolioHistogramas** es una herramienta en Python diseñada para analizar la rentabilidad mensual de un portafolio de activos financieros en múltiples años. Este programa genera histogramas que muestran las rentabilidades mensuales para cada año especificado por el usuario, coloreando en verde oscuro los meses con rentabilidad positiva y en rojo oscuro los meses con rentabilidad negativa. Todos los gráficos se presentan en una única figura organizada en una cuadrícula.

## Características

- Permite analizar la rentabilidad mensual de un portafolio compuesto por múltiples activos financieros.
- Soporta múltiples años en una sola ejecución.
- Genera histogramas organizados en una cuadrícula, mostrando:
  - Rentabilidad mensual por mes.
  - Rentabilidad anual acumulada en el título de cada gráfico.
- Descarga automáticamente datos históricos de los activos desde Yahoo Finance.

## Requisitos

- Python 3.7 o superior.
- Paquetes necesarios:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`

Para instalar las dependencias, utiliza el siguiente comando:

```bash
pip install yfinance pandas numpy matplotlib
