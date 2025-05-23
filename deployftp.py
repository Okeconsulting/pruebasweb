import os
from ftplib import FTP, error_perm
import fnmatch # Para la coincidencia de patrones (glob-style)

def deploy_ftp(server, username, password, local_dir, remote_path):

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
        'deployftp.py', # El propio script de despliegue
        'README.md' 
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
                # Crear directorios recursivamente si no existen
                parts = remote_path.strip('/').split('/')
                current_path = ''
                for part in parts:
                    current_path += '/' + part
                    try:
                        ftp.mkd(current_path)
                        print(f"Directorio creado: {current_path}")
                    except error_perm:
                        # Si ya existe, simplemente continúa
                        pass
                ftp.cwd(remote_path)
                print(f"Cambiado al directorio remoto: {remote_path}")

        print(f"Iniciando subida de archivos desde: {local_dir}")
        for root, dirs, files in os.walk(local_dir):
            relative_path = os.path.relpath(root, local_dir)
            remote_sub_path = os.path.join(remote_path, relative_path).replace("\\", "/") if remote_path else relative_path.replace("\\", "/")

            if relative_path == ".":
                # Si es el directorio base local, no cambiar el remoto
                pass
            else:
                try:
                    ftp.mkd(remote_sub_path)
                    print(f"Directorio remoto creado: {remote_sub_path}")
                except error_perm as e:
                    if "File exists" in str(e):
                        # print(f"Directorio remoto ya existe: {remote_sub_path}")
                        pass
                    else:
                        raise e # Re-lanzar si es otro tipo de error

            for file in files:
                local_file_path = os.path.join(root, file)
                remote_file_path = os.path.join(remote_sub_path, file).replace("\\", "/")
                
                # Ignorar archivos ocultos o de control de versiones
                if file.startswith('.') or file.endswith('.pyc') or file == '__pycache__':
                    print(f"Ignorando archivo: {local_file_path}")
                    continue

                with open(local_file_path, 'rb') as fp:
                    print(f"Subiendo: {local_file_path} a {remote_file_path}")
                    ftp.storbinary(f'STOR {remote_file_path}', fp)
                print(f"Subido exitosamente: {local_file_path}")

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
    FTP_REMOTE_PATH = os.environ.get('FTP_REMOTE_PATH', '').strip('/') # Asegúrate que no tenga slash al inicio si es vacío
    LOCAL_DIR = os.environ.get('LOCAL_DIR', '.') # Directorio local por defecto es el actual

    if not all([FTP_SERVER, FTP_USERNAME, FTP_PASSWORD]):
        print("Error: Las variables de entorno FTP_SERVER, FTP_USERNAME y FTP_PASSWORD deben estar configuradas.")
        exit(1)

    deploy_ftp(FTP_SERVER, FTP_USERNAME, FTP_PASSWORD, LOCAL_DIR, FTP_REMOTE_PATH)
