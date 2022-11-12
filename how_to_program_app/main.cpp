#include <QGuiApplication>
#include <QQmlApplicationEngine>

#include "systemcaller.h"


int main(int argc, char *argv[])
{
  QGuiApplication app(argc, argv);

  qmlRegisterType<SystemCaller>("SystemCaller", 1, 0, "SystemCaller");

  // This is auto-generated code by QtCreator
  QQmlApplicationEngine engine;
  const QUrl url(u"qrc:/how_to_program_app/main.qml"_qs);
  QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                   &app, [url](QObject *obj, const QUrl &objUrl) {
    if (!obj && url == objUrl)
      QCoreApplication::exit(-1);
  }, Qt::QueuedConnection);
  engine.load(url);

  return app.exec();
}
