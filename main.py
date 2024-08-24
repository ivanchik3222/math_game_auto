from PIL import ImageGrab
import keyboard
import easyocr
import time


def take_screenshots(regions):
    for i in range(len(regions)):
        screenshot = ImageGrab.grab(bbox=regions[i])
        screenshot.save(f"screenshot{i}.png")  
    pass

reader = easyocr.Reader(['en'], gpu = True)#оставил true для тех, у кого есть CUDA 

if __name__ == "__main__":

    while True:

        take_screenshots([(192,64,760,137),(232,943,733,1020)])
        text_question = reader.readtext('screenshot0.png',detail=1, paragraph=True)
        
        if text_question != []:
            text_question = text_question[0][1]
        if "=" in text_question and ("+" in text_question or "-" in text_question):
            question = text_question[:text_question.index("=")]
            answer = eval(question)
            print("пример: ", question)
            print("ответ: ", answer)

            text_answers = reader.readtext('screenshot1.png',detail = 1)

            answers =[]
            for i in text_answers:
                answers.append(i[1])
            print(answers)

            if str(answer) in answers:
                to_press = str(answers.index(str(answer)) + 1)
                print("клавиша:", to_press)
                keyboard.press(to_press)
                print()
            else:
                print("не найден нужный ответ")
            time.sleep(10)