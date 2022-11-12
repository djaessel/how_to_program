#include "systemcaller.h"

void SystemCaller::openUrl(QString url)
{
  QDesktopServices::openUrl(QUrl(url));
  this->urlOpened(url);
}
