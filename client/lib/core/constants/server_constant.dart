import 'dart:io';

class ServerConstant {
  static String serverURl =
      Platform.isAndroid ? 'http://10.0.2.2:8000' : 'http://127.0.0.:8000';
}
