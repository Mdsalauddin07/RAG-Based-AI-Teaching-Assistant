#mp3 to json

import whisper
import json
import os

model = whisper.load_model("base")
audios = os.listdir("audios")

for audio in audios:
    if (" " in audio):
        number = audio.split(" ")[0]
        title = audio.split(" ")[2:]
        print(number, title)
        result = model.transcribe(audio= f"audios/{audio}", language = "hi", task = "translate", word_timestamps=False)


        chunks = []
        for segment in result["segments"]:
            chunks.append({
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })
        
            chunks_with_metadata = {"chunks": chunks, "text": result["text"], }

            json_file = audio.replace(".mp3", ".json")

        with open(f"jsons/{json_file}", "w", encoding="utf-8") as f:
            json.dump(chunks_with_metadata, f, indent=4)

