import 'package:flutter/material.dart';
import 'API.dart';
// import 'dart:convert';
// import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'BabyFootX',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Baby Foot X'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  // var url;
  // var Data;
  // String res = 'Here';
  // String text = '';
  String name = "";
  String final_response = "";
  final _formkey = GlobalKey<FormState>();

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text("test"),
            Container(width:350,
              child: Form(key: _formkey,
                child: TextFormField(
                  decoration: InputDecoration(
                    labelText: 'Enter your name',
                    enabledBorder: _inputformdeco(),
                    focusedBorder: _inputformdeco(),
                  ),
                ),
              ),
            ),
            // TextField(
            //     onChanged: (value) {
            //       url = 'http://127.0.0.1:5000/api?Query=' + value.toString();
            //       setState(() {
            //         // res = url;
            //       });
            //     },
            //     decoration: InputDecoration(
            //       hintText: 'Search Anything Here',
            //       suffixIcon: GestureDetector(
            //           onTap: () async {
            //             // Data = await http.post('http://127.0.0.1:5000/');
            //             // print(await http.read('http://127.0.0.1:5000/'));
            //             String response = await myPythonBack();
            //             // var DecodedData = jsonDecode(Data);
            //             setState((){
            //               text = response;
            //             });
            //           },
            //           child: const Icon(Icons.search,
            //               color: Colors.blue, size: 20)),
            //     )),
            // const Text(
            //   'You have pushed the button too many times:',
            // ),
            // Text(
            //   '$_counter',
            //   style: Theme.of(context).textTheme.headline4,
            // ),
            // // Text(res),
            // Text(text)
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
