// ignore_for_file: avoid_print

import 'dart:convert'; // Import this for jsonEncode

import 'package:http/http.dart' as http;

class AuthRemoteRepository {
  Future<void> signup({
    required String name,
    required String email,
    required String password,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('http://10.0.2.2:8000/auth/signup'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'name': name, 'email': email, 'password': password}),
      );
      print(response.body);
      print(response.statusCode);
    } catch (e) {
      print(e);
    }
  }

  Future<void> login({required String email, required String password}) async {
    try {
      final response = await http.post(
        Uri.parse(
          'http://10.0.2.2:8000/auth/login',
        ), // Đây là URL cho API đăng nhập
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password}),
      );

      print('Login Response Body: ${response.body}');
      print('Login Status Code: ${response.statusCode}');
    } catch (e) {
      print(e);
    }
  }
}
