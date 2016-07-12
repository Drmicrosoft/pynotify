#/usr/bin/python
import pynotify
try:
    import pynotify
    if pynotify.init("My Application Name"):
        Alert = pynotify.Notification("Important", "This Is DrMicrosoft")
        Alert.show()
    else:
        print "Error starting pynotify"
except:
    print "pynotify not installed"
