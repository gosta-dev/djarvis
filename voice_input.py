import speech_recognition as sr
import ai_repuller

WAKE_WORD = "джарвис"
recognizer = sr.Recognizer()
recognizer.energy_threshold = 350
recognizer.dynamic_energy_threshold = False
recognizer.pause_threshold = 2.5
recognizer.phrase_threshold = 0.3

try:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        while True:
            print("\nСлушаю")
            try:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=8)
                text = recognizer.recognize_google(audio, language="ru-RU").lower().strip()
                text = text.replace(",", "").replace(".", "")
                print(f"Услышал: {text}")

                if WAKE_WORD in text:
                    start_index = text.find(WAKE_WORD) + len(WAKE_WORD)
                    command = text[start_index:].strip()

                    if command:
                        print(f"Выполнение: {command}")
                        ai_repuller.main(command)

            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"Ошибка сети / Google API: {e}")

except KeyboardInterrupt:
    print("\nПрограмма остановлена.")
