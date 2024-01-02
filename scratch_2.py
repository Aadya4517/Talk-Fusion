
import cv2
import pytesseract


# Set the Tesseract path (replace 'path_to_tesseract' with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




from googletrans import Translator

def camera_translation(target_language='fr'):
    cap = cv2.VideoCapture(0)

    with open('../../AppData/Roaming/JetBrains/PyCharm2023.3/scratches/recognized_translated_text.txt', 'a') as file:
        while True:
            ret, frame = cap.read()
            cv2.imshow('Camera', frame)

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray_frame)
            print(f"Recognized text: {text}")

            translator = Translator()
            translated_text = translator.translate(text, dest=target_language).text
            print(f"Translated text: {translated_text}")

            file.write(f"Recognized text: {text}\n")
            file.write(f"Translated text: {translated_text}\n\n")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_translation('fr')