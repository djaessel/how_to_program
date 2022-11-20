#ifndef TASKLOADER_H
#define TASKLOADER_H

#include <QObject>
#include <QDesktopServices>
#include <QUrl>
#include <QQmlComponent>

class TaskLoader : public QObject
{
  Q_OBJECT
  //Q_PROPERTY(int prop1 READ prop1 WRITE setProp1 NOTIFY prop1Changed);
  QML_ELEMENT
public:
  explicit TaskLoader(QObject *parent = nullptr){/* TODO: add code if necessary */}

signals:

};

#endif // TASKLOADER_H
