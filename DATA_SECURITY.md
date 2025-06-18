# Sales Detail Report - Datos Embebidos

## 🔒 Características de Seguridad

Este proyecto ha sido configurado para cargar automáticamente los datos del CSV **sin exponer el archivo para descarga**.

### ✅ Lo que se implementó:

1. **Datos Embebidos**: Los datos del CSV `Sales_Detail_By_Lotid.csv` han sido convertidos a formato JavaScript y embebidos directamente en el código.

2. **Carga Automática**: Los datos se cargan automáticamente al inicializar el componente, sin necesidad de subir archivos.

3. **Sin Acceso al CSV**: El archivo CSV original no está incluido en el proyecto final, solo los datos procesados.

### 📁 Archivos Importantes:

- `src/data/salesData.js` - Contiene los 7,329 registros embebidos
- `convertCsvToData.js` - Script para regenerar los datos (solo para desarrollo)
- `SalesDetailReport.jsx` - Componente principal modificado

### 🔄 Regenerar Datos (solo desarrollo):

```bash
node convertCsvToData.js
```

### 📊 Datos Cargados:
- **Total registros**: 7,329
- **Exportadores**: Agrolatina, Agrovita, etc.
- **Retailers**: KROGER, COSTCO WHOLESALE, etc.
- **Variedades**: AUTUMN CRISP, TIMCO, etc.

### 🛡️ Seguridad:
- ✅ CSV no accesible para descarga
- ✅ Datos embebidos en JavaScript compilado
- ✅ No hay endpoints o archivos expuestos
- ✅ Carga automática sin intervención del usuario
