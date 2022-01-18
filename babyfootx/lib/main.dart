import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

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
  // String url = "";
  // String name = "";
  String greetings = "";

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
          children: [
            Text (greetings,
              style: const TextStyle(fontSize:24, fontWeight: FontWeight.bold)
            ),
            Center(
              child: Container(
                width:150,
                height:60,
                child: ElevatedButton(
                  onPressed: () async {

                    final response = await http.get(Uri.parse('https://foodish-api.herokuapp.com/api/'));

                    final decoded = json.decode(response.body) as Map<String, dynamic>;

                    setState(() {
                      greetings = decoded['image'];
                    });

                  },
                  child: const Text("Press",style: TextStyle(fontSize:24)),
                )
              )
            ),
            // TextField(
            //     onChanged: (value) {
            //       url = 'http://127.0.0.1:5000/api?Query=' + value.toString();
            //       setState(() {
            //       });
            //     },
            //     decoration: InputDecoration(
            //       hintText: 'Search Anything Here',
            //       suffixIcon: GestureDetector(
            //           onTap: () async {
            //             setState((){
            //             });
            //           },
            //           child: const Icon(Icons.search,
            //               color: Colors.blue, size: 20)),
            //     )),
            const Text(
              'You have pushed the button too many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
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
