Pruebas con AWS Textract DetectDocumentText sobre las imágenes extraídas de los documentos pdf.
#

### Dataset
#
https://data.controlciudadanopy.org/municipalidad/

### Formato: documentos a ser analizados
#
downloadDate(%y-%MM-%dd)_hashDocument_(%Mon_%y).pdf

### SDK
#
- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- https://docs.aws.amazon.com/textract/latest/dg/detecting-document-text.html

### TODO
#
- Realizar extracción de datos del block file basado en patrones del documento
- Analizar resultados con el modo AnalyzeDocument
- Probar el modo asíncrono
- Probar con archivo pdf de múltiples paginas
- Parsear resultados por página
