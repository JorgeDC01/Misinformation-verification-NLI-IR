import nbformat
import os

def force_fix_widgets_metadata(notebook_path, save_backup=True):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Backup
    if save_backup:
        backup_path = notebook_path + ".bak"
        with open(backup_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"🛡️ Backup guardado en {backup_path}")

    # Forzar 'widgets' con clave 'state'
    if 'metadata' not in nb:
        nb['metadata'] = {}

    if 'widgets' not in nb['metadata'] or not isinstance(nb['metadata']['widgets'], dict):
        nb['metadata']['widgets'] = {}

    nb['metadata']['widgets']['state'] = nb['metadata']['widgets'].get('state', {})

    # Guardar
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"✅ Reparado: {notebook_path}")

# Uso:
force_fix_widgets_metadata("not_IR_NLI_LoRA - copia.ipynb")
