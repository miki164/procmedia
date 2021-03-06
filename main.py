import sys
from detect import Detector
import help

command = sys.argv[1]

if command == 'detect':
    try:
        obj = Detector(sys.argv[2], sys.argv[3], sys.argv[4])
    except Exception:
        obj = Detector(sys.argv[2], sys.argv[3])
    obj.detect()
elif command == 'generate-haar':
    pass
elif command == 'help':
    help.show_help()
else:
    print("Command unknown. Check detect-cli help for more information")