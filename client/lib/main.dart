import 'package:client/core/theme/theme.dart';
import 'package:client/features/auth/view/pages/signup_page.dart';
import 'package:flutter/material.dart';
<<<<<<< HEAD
import 'package:flutter_riverpod/flutter_riverpod.dart'; // <--- Thêm import này

void main() {
  runApp(
    const ProviderScope(
      // <--- Bọc ứng dụng của bạn bằng ProviderScope ở đây
      child: MyApp(),
    ),
  );
=======
import 'package:flutter_riverpod/flutter_riverpod.dart';

void main() {
  runApp(ProviderScope(child: const MyApp()));
>>>>>>> 9d67ce7879a8403be177255c4a9e2f8e49e29ba7
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: AppTheme.darkThemeMode,
      home: const SignupPage(),
    );
  }
}
