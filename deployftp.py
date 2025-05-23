import os
from ftplib import FTP, error_perm
import fnmatch # Para la coincidencia de patrones (glob-style)

def deploy_ftp(server, username, password, local_dir, remote_path, exclude_patterns=None):
    if exclude_patterns is None:
        exclude_patterns = []

    # Añadir patrones de exclusión comunes que probablemente no quieres desplegar
    default_exclude_patterns = [
        '.git/',        # Directorio de Git
        '.github/',     # Directorio de GitHub Actions
        '__pycache__/', # Caché de Python
        '*.pyc',        # Archivos compilados de Python
        '*.DS_Store',   # Archivos de macOS
        'Thumbs.db',    # Archivos de Windows
        '.env',         # Archivos de entorno (credenciales, etc.)
        'deployftp.py' # El propio script de despliegue
    ]
    # Combina los patrones por defecto con los que se pasen
    all_exclude_patterns = default_exclude_patterns + exclude_patterns

    # Función auxiliar para comprobar si un archivo/directorio debe ser excluido
    def should_exclude(path, is_dir=False):
        # Normaliza la ruta para comparación (usa '/' como separador)
        normalized_path = path.replace("\\", "/")
        if is_dir and not normalized_path.endswith('/'):
            normalized_path += '/' # Asegura que los directorios terminen con '/' para las reglas

        for pattern in all_exclude_patterns:
            # Comprueba si la ruta coincide con el patrón
            if fnmatch.fnmatch(normalized_path, pattern):
                return True
            # Si el patrón es un directorio (termina con /) y la ruta es un archivo dentro de ese directorio
            if pattern.endswith('/') and normalized_path.startswith(pattern):
                 return True
        return False

    ftp = None
    try:
        print(f"Conectando a FTP: {server}...")
        ftp = FTP(server)
        ftp.login(user=username, passwd=password)
        print("Conexión FTP exitosa.")

        if remote_path and remote_path != '/':
            try:
                ftp.cwd(remote_path)
                print(f"Cambiado al directorio remoto: {remote_path}")
            except error_perm:
                print(f"Directorio remoto '{remote_path}' no existe, intentando crearlo...")
                parts = remote_path.strip('/').split('/')
                current_path = ''
                for part in parts:
                    current_path += '/' + part
                    try:
                        ftp.mkd(current_path)
                        print(f"Directorio creado: {current_path}")
                    except error_perm:
                        pass
                ftp.cwd(remote_path)
                print(f"Cambiado al directorio remoto: {remote_path}")

        print(f"Iniciando subida de archivos desde: {local_dir}")
        for root, dirs, files in os.walk(local_dir):
            # Obtiene la ruta relativa del directorio actual con respecto a local_dir
            relative_root = os.path.relpath(root, local_dir)
            if relative_root == ".": # Si estamos en la raíz local
                current_remote_dir = remote_path if remote_path else ''
            else:
                current_remote_dir = os.path.join(remote_path, relative_root).replace("\\", "/") if remote_path else relative_root.replace("\\", "/")


            # Filtrar directorios a visitar (para no entrar en directorios excluidos)
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(relative_root, d), is_dir=True)]

            # Crear directorios remotos
            for d in dirs:
                local_dir_path = os.path.join(relative_root, d)
                if should_exclude(local_dir_path, is_dir=True):
                    print(f"Ignorando directorio excluido: {local_dir_path}")
                    continue

                remote_sub_path = os.path.join(current_remote_dir, d).replace("\\", "/")
                try:
                    ftp.mkd(remote_sub_path)
                    print(f"Directorio remoto creado: {remote_sub_path}")
                except error_perm as e:
                    if "File exists" in str(e) or "Folder already exists" in str(e): # Algunos servidores FTP usan diferentes mensajes
                        pass
                    else:
                        raise e

            # Subir archivos
            for file in files:
                local_file_path_full = os.path.join(root, file)
                local_file_path_relative = os.path.join(relative_root, file)

                if should_exclude(local_file_path_relative):
                    print(f"Ignorando archivo excluido: {local_file_path_relative}")
                    continue

                remote_file_path = os.path.join(current_remote_dir, file).replace("\\", "/")

                with open(local_file_path_full, 'rb') as fp:
                    print(f"Subiendo: {local_file_path_relative} a {remote_file_path}")
                    ftp.storbinary(f'STOR {remote_file_path}', fp)
                print(f"Subido exitosamente: {local_file_path_relative}")

    except error_perm as e:
        print(f"Error FTP: {e}")
        exit(1)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        exit(1)
    finally:
        if ftp:
            ftp.quit()
            print("Desconexión FTP exitosa.")

if __name__ == "__main__":
    FTP_SERVER = os.environ.get('FTP_SERVER')
    FTP_USERNAME = os.environ.get('FTP_USERNAME')
    FTP_PASSWORD = os.environ.get('FTP_PASSWORD')
    FTP_REMOTE_PATH = os.environ.get('FTP_REMOTE_PATH', '').strip('/')
    LOCAL_DIR = os.environ.get('LOCAL_DIR', '.')

    # Obtener patrones de exclusión de una variable de entorno, si existe
    # Los patrones deben estar separados por comas (,)
    #EXCLUDE_PATTERNS_STR = os.environ.get('EXCLUDE_PATTERNS', '')
    #EXCLUDE_PATTERNS = [p.strip() for p in EXCLUDE_PATTERNS_STR.split(',') if p.strip()]
    EXCLUDE_PATTERNS=None

    if not all([FTP_SERVER, FTP_USERNAME, FTP_PASSWORD]):
        print("Error: Las variables de entorno FTP_SERVER, FTP_USERNAME y FTP_PASSWORD deben estar configuradas.")
        exit(1)

    deploy_ftp(FTP_SERVER, FTP_USERNAME, FTP_PASSWORD, LOCAL_DIR, FTP_REMOTE_PATH, EXCLUDE_PATTERNS)