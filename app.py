import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

# Crear una ventana básica de Tkinter
root = tk.Tk()
root.withdraw() # Esconde la ventana principal
# Abrir un cuadro de diálogo para seleccionar archivos PDF
file_paths = filedialog.askopenfilenames(title="Selecciona archivos PDF para unir", filetypes=[("PDF files", "*.pdf")])

# Si el usuario seleccionó al menos un archivo
if file_paths:
    merger = PdfMerger()

    # Añadir los archivos seleccionados al PdfFileMerger
    for file_path in file_paths:
        merger.append(file_path)

    # Guardar el PDF resultante
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_path:
        merger.write(output_path)
        merger.close()
        print(f"PDF unido guardado en: {output_path}")
    else:
        print("Operación de guardado cancelada.")
else:
    print("No se seleccionó ningún archivo.")

