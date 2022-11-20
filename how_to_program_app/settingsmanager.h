#ifndef SETTINGSMANAGER_H
#define SETTINGSMANAGER_H

#include <QObject>
#include <QDesktopServices>
#include <QUrl>
#include <QQmlComponent>

class SettingsManager : public QObject
{
  Q_OBJECT
  //Q_PROPERTY(int prop1 READ prop1 WRITE setProp1 NOTIFY prop1Changed);
  QML_ELEMENT
public:
  explicit SettingsManager(QObject *parent = nullptr){/* TODO: add code if necessary */}

signals:

};

#endif // SETTINGSMANAGER_H
