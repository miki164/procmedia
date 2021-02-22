import sys
from detect import Detector
import help
import cv2
command = sys.argv[1]

if sys.argv[1] == 'detect':
    obj = Detector(sys.argv[2], sys.argv[3])
    img = obj.detect()
    cv2.imwrite("detected.jpg", img)

elif sys.argv[1] == 'generate-haar':
    pass
elif sys.argv[1] == 'help':
    help.show_help()
else:
    print("Command unknown. Check detect-cli help for more information")