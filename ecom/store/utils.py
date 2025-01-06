# utils.py
import trimesh

def process_model(file_path, size_option, quality_option):
    mesh = trimesh.load(file_path)

    # Redimensionar el modelo según la opción seleccionada
    if size_option == 'small':
        scale_factor = 0.5
    elif size_option == 'medium':
        scale_factor = 1.0
    elif size_option == 'large':
        scale_factor = 1.5
    mesh.apply_scale(scale_factor)

    # Ajustar la calidad (por ejemplo, reducir el número de vértices)
    if quality_option == 'low':
        mesh = mesh.simplify_quadratic_decimation(1000)  # Reduce a 1000 caras
    elif quality_option == 'medium':
        mesh = mesh.simplify_quadratic_decimation(5000)  # Reduce a 5000 caras
    elif quality_option == 'high':
        pass  # No se aplica simplificación para alta calidad

    processed_file_path = file_path.replace('.obj', '_processed.obj')
    mesh.export(processed_file_path)
    return processed_file_path
