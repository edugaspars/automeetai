import assemblyai as aai

aai.settings.api_key = "2ff785a5e5e2443ab38839cdfa1e53f0"

FILE_URL = "9de28f2ddd1d4cab8080aac04debab23.mp3"


transcriber = aai.Transcriber()

configs = aai.TranscriptionConfig(
    speaker_labels= True,
    speakers_expected= 2,
    language_code= 'pt'
)

transcript = transcriber.transcribe(FILE_URL, config=configs)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    for utt in transcript.utterances:
        print(f"{utt.speaker}: {utt.text}")
        print('\n')