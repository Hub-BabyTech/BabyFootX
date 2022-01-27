import 'package:http/http.dart' as http;

Future<String> getData() async{
  final response = await http.get(Uri.http('127.0.0.1:5000', '/'));
  return response.body;
}