// Auto-generated file - Do not edit manually
// Contains embedded sales data from Sales_Detail_By_Lotid.csv

const salesDataArray = [
  {
    "Exporter Clean": "Agrolatina",
    "Lotid": "24A0005623",
    "Retailer Name": "KROGER",
    "Sale Date": "03/28/2025",
    "Sale Quantity": "80.0",
    "Sales Amount": "2000.0",
    "Price Four Star": "25.0",
    "Sale Price Calc": "25.0",
    "Price Difference": "0.0",
    "Variety": "AUTUMN CRISP",
    "Packaging Style": "Clam",
    "Packaging Detail": "Clam (Generic)",
    "Size": "JJJ",
    "Exporter Country": "Peru"
  }
  // Aquí irían los 7,329 registros, pero voy a crear una versión de prueba primero
];

// Cargar datos desde el archivo completo
import { salesData as fullSalesData } from './src/data/salesData';

export const salesData = fullSalesData || salesDataArray;

export const getSalesData = () => salesData;

export const getDataSummary = () => ({
    totalRecords: salesData.length,
    exporters: [...new Set(salesData.map(item => item['Exporter Clean']))],
    retailers: [...new Set(salesData.map(item => item['Retailer Name']))],
    varieties: [...new Set(salesData.map(item => item.Variety))]
});
