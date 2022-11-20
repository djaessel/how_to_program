#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>

#include "systemcaller.h"
#include "settingsmanager.h"
#include "videoloader.h"
#include "taskloader.h"


int main(int argc, char *argv[])
{
  QGuiApplication app(argc, argv);

  // This is auto-generated code by QtCreator
  QQmlApplicationEngine engine;
  const QUrl url(u"qrc:/how_to_program_app/main.qml"_qs);
  QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                   &app, [url](QObject *obj, const QUrl &objUrl) {
    if (!obj && url == objUrl)
      QCoreApplication::exit(-1);
  }, Qt::QueuedConnection);

  QQmlContext* context = engine.rootContext();

  SystemCaller systemCaller;
  context->setContextProperty(QString("systemCaller"), &systemCaller);

  SettingsManager settingsManager;
  context->setContextProperty(QString("settingsManager"), &settingsManager);

  VideoLoader videoLoader;
  context->setContextProperty(QString("videoLoader"), &videoLoader);

  TaskLoader taskLoader;
  context->setContextProperty(QString("taskLoader"), &taskLoader);

  engine.load(url);

  return app.exec();
}
