#include <QGuiApplication>
#include <QQmlApplicationEngine>


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
  engine.load(url);

  return app.exec();
}
