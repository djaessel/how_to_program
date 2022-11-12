#ifndef SYSTEMCALLER_H
#define SYSTEMCALLER_H

#include <QObject>
#include <QDesktopServices>
#include <QUrl>
#include <QQmlComponent>

class SystemCaller : public QObject
{
  Q_OBJECT
  //Q_PROPERTY(int prop1 READ prop1 WRITE setProp1 NOTIFY prop1Changed);
  QML_ELEMENT
public:
  explicit SystemCaller(QObject *parent = nullptr){/* TODO: add code if necessary */}

  Q_INVOKABLE void openUrl(QString url);

signals:
  void urlOpened(QString url);

};

#endif // SYSTEMCALLER_H
