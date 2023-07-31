import cv2


# Crie nosso classificador de corpos


body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Passe o quadro para nosso classificador de corpos
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exibir o quadro com os retângulos desenhados
    cv2.imshow('Detecção de áreas', frame)

    # Verifique se a tecla espaço (código ASCII 32) foi pressionada
    if cv2.waitKey(1) == 32:
        break

cap.release()
cv2.destroyAllWindows()
