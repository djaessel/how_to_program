QT += quick

SOURCES += \
        main.cpp \
        systemcaller.cpp

resources.files = main.qml \
MenuButton.qml \
BasePage.qml \
WelcomePage.qml \
VideoTutorials.qml \
PracticeTasks.qml \
SettingsPage.qml \
UserSettingsPage.qml

resources.prefix = /$${TARGET}
RESOURCES += resources

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Additional import path used to resolve QML modules just for Qt Quick Designer
QML_DESIGNER_IMPORT_PATH =

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    BasePage.qml \
    MenuButton.qml \
    PracticeTasks.qml \
    SettingsPage.qml \
    UserSettingsPage.qml \
    VideoTutorials.qml \
    WelcomePage.qml

HEADERS += \
    systemcaller.h
