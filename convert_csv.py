#!/usr/bin/env python3
"""
Script para convertir CSV a datos JSON embebidos en JavaScript
"""
import csv
import json
import os

def csv_to_js_data(csv_path, output_path, var_name="salesData"):
    """Convierte CSV a archivo JS con datos embebidos"""
    
    data = []
    
    # Leer CSV
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Limpiar y convertir tipos de datos
            cleaned_row = {}
            for key, value in row.items():
                # Limpiar valor
                if value == '' or value is None:
                    cleaned_row[key] = None
                elif key in ['Recvqnt', 'Issueqnt', 'Invcqnt', 'Rcptqnt', 'Saleamt', 'Chgqnt', 'Chgamt', 'Invcicqnt', 'Price Per Case Invc', 'Price Per Case Rcpt']:
                    # Campos numéricos
                    try:
                        cleaned_row[key] = float(value) if value else 0
                    except:
                        cleaned_row[key] = 0
                elif key in ['Pricepercase Cleaned']:
                    try:
                        cleaned_row[key] = float(value) if value else 0
                    except:
                        cleaned_row[key] = 0
                else:
                    cleaned_row[key] = str(value).strip() if value else ""
            
            data.append(cleaned_row)
    
    # Escribir como archivo JS
    with open(output_path, 'w', encoding='utf-8') as jsfile:
        jsfile.write(f"// Auto-generated data file - Do not edit manually\n")
        jsfile.write(f"// Generated from: {os.path.basename(csv_path)}\n")
        jsfile.write(f"// Total records: {len(data)}\n\n")
        jsfile.write(f"export const {var_name} = ")
        json.dump(data, jsfile, indent=2, ensure_ascii=False)
        jsfile.write(";\n\n")
        jsfile.write(f"export default {var_name};\n")
    
    print(f"✅ Converted {len(data)} records from {csv_path} to {output_path}")
    return len(data)

if __name__ == "__main__":
    # Rutas
    csv_path = "/Users/jp/Documents/Famus 3.0/famus-report-analysis/data/html data/CSV_Report_2024-2025/Processed_Data.csv"
    output_path = "/Users/jp/Documents/Famus 3.0/famus-report-analysis/reports/html_reports/sales-report-v2-final/data.js"
    
    # Convertir
    csv_to_js_data(csv_path, output_path)
