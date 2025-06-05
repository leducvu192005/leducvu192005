import 'package:client/features/auth/repositories/auth_remote_repository.dart';
import 'package:client/models/user_model.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';
import 'package:fpdart/fpdart.dart';
part 'auth_viewmodel.g.dart';

@riverpod
class AuthViewModel extends _$AuthViewModel {
  final AuthRemoteRepository _authRemoteRepository = AuthRemoteRepository();
  @override
  @override
  AsyncValue<UserModel> build() {
    return const AsyncValue<UserModel>.loading();
  }

  Future<void> signUpUser({
    required String name,
    required String email,
    required String password,
  }) async {
    final res = await _authRemoteRepository.signup(
      name: name,
      email: email,
      password: password,
    );

    final val = switch (res) {
      Left(value: final l) => l,
      Right(value: final r) => r.name,
    };

    // ignore: avoid_print
    print(val);
  }
}
