import cv2

def my():
    streamer=cv2.VideoCapture(0)
    while True:    
        a,b=streamer.read()
        if not a:
            a.release()
            cv2.destroyAllWindows()
            break;
        else:
            ret,buf=cv2.imencode('.png',b)
        b=buf.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + b + b'\r\n')