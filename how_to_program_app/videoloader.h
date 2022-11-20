#ifndef VIDEOLOADER_H
#define VIDEOLOADER_H

#include <QObject>
#include <QDesktopServices>
#include <QUrl>
#include <QQmlComponent>

class VideoLoader : public QObject
{
  Q_OBJECT
  //Q_PROPERTY(int prop1 READ prop1 WRITE setProp1 NOTIFY prop1Changed);
  QML_ELEMENT
public:
  explicit VideoLoader(QObject *parent = nullptr){/* TODO: add code if necessary */}

signals:

};

#endif // VIDEOLOADER_H
