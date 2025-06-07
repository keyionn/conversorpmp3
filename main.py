import yt_dlp

def main():
    print("=== YouTube para MP3 320kbps ===")
    url = input("Cole o URL do vídeo do YouTube: ").strip()
    filename = input("Digite o nome do arquivo de saída (sem extensão): ").strip()
    
    if not url or not filename:
        print("Erro: URL e nome do arquivo são obrigatórios!")
        return
    
    print("\n▶ Iniciando download...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # Bitrate de 320kbps
        }],
        'outtmpl': f'{filename}.%(ext)s',
        'quiet': False,
        'progress_hooks': [lambda d: print(f"\r🔄 Progresso: {d.get('_percent_str', '0%')} | Tempo restante: {d.get('_eta_str', '?')}", end='', flush=True)],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✅ Download completo! Arquivo salvo como '{filename}.mp3' (320kbps)")
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")

if __name__ == "__main__":
    main()
