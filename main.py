import nbformat
import os

def remove_widgets_metadata(notebook_path, save_backup=True):
    # Cargar el notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Hacer backup opcional
    if save_backup:
        backup_path = notebook_path + ".bak"
        with open(backup_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"🛡️ Backup creado: {backup_path}")

    # Eliminar widgets
    if 'widgets' in nb.get('metadata', {}):
        del nb['metadata']['widgets']
        print(f"🧹 'metadata.widgets' eliminado de {notebook_path}")

    # Guardar
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"✅ Notebook limpio y guardado: {notebook_path}")

# Ejemplo de uso:

remove_widgets_metadata("IR_NLI_LoRA.ipynb")
remove_widgets_metadata("not_IR_NLI_LoRA.ipynb")
remove_widgets_metadata("not_IR_NLI_noLoRA.ipynb")