import librosa
import mutagen

def extract_metadata(file):
    y, sr = librosa.load(file)
    duration = librosa.get_duration(y=y, sr=sr)
    
    audio_info = mutagen.File(file)
    return {
        'duration': duration,
        'sample_rate': sr,
        'bitrate': getattr(audio_info.info, 'bitrate', None),
        'format': file.filename.split('.')[-1].lower()
    }
