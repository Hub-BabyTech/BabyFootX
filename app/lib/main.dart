import 'package:flutter/material.dart';

import 'package:app/widgets/ball.dart';

import 'API.dart';
import 'dart:convert';
import 'dart:async';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String url = 'http://127.0.0.1:5000/api';

  var Data;

  String ScoreText = '0 - 0';
  String PossessionRed = '50%';
  String PossessionBlue = '50%';

  // List a = [
  //   // Ball(top: 0.0, left: 0.0),
  //   // Ball(top: 100.0, left: 100.0),
  //   // Ball(top: 50.0, left: 23.0),
  //   Ball(top: 50.0, left: 50.0),
  //   // Ball(top: 30.0, left: 50.0),
  //   // Ball(top: 50.0, left: 80.0),
  //   // Ball(top: 40.0, left: 45.0),
  // ];

  List<Ball> balls = <Ball>[];

  @override
  void initState() {
    Timer.periodic(Duration(seconds: 2), (timer) async {
      Data = await Getdata(url);
      var DecodedData = jsonDecode(Data);
      setState(() {
        ScoreText = DecodedData['Score'];
        PossessionRed = DecodedData['Red'];
        PossessionBlue = DecodedData['Blue'];
        var newBalls = DecodedData['Balls'];
        for (var ball in newBalls)
          balls.add(Ball(top: ball[0].toDouble(), left: ball[1].toDouble()));
      });
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color(0xFFF7DBA7),
        appBar: AppBar(
          backgroundColor: Colors.black,
          title: Text('BABY FOOT X'),
        ),
        body: Column(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.all(10.0),
              child: Text(
                "SCORE",
                style: TextStyle(
                    fontSize: 30.0,
                    fontWeight: FontWeight.bold,
                    fontFamily: "Sportive"),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(" Team Red ",
                    style: TextStyle(
                        fontSize: 25.0,
                        color: Colors.red,
                        fontFamily: 'Sportive')),
                Text(ScoreText,
                    style: TextStyle(fontSize: 20.0, fontFamily: 'Sportive')),
                Text("Team Blue ",
                    style: TextStyle(
                        fontSize: 25.0,
                        color: Colors.blue,
                        fontFamily: 'Sportive')),
              ],
            ),
            Stack(children: [
              Image.asset("assets/images/stade.jpg"),
              for (var ball in balls) ball,
              // ListView.builder(
              //   itemBuilder: (BuildContext ctx, int index) {
              //     return a[index];
              //   },
              //   itemCount: a.length,
              // )
            ]),
            SizedBox(height: 20.0),
            Text("Possessions",
                style: TextStyle(
                    color: Colors.black,
                    fontSize: 25.0,
                    fontFamily: "Sportive")),
            SizedBox(height: 10.0),
            Stack(children: [
              Image.asset("assets/images/stade.jpg"),
              // SizedBox(
              //   height: 200,
              //   width: 100,
              //   child: const DecoratedBox(
              //     decoration: const BoxDecoration(color: Color(0x80F7DBA7)),
              //   ),
              // ),
              Positioned(
                  left: 75,
                  top: 110,
                  child: Text(PossessionRed,
                      style: TextStyle(
                          color: Colors.black,
                          fontFamily: "Sportive",
                          fontSize: 30.0))),
              Positioned(
                left: 230,
                top: 110,
                child: Text(PossessionBlue,
                    style: TextStyle(
                        color: Colors.black,
                        fontFamily: "Sportive",
                        fontSize: 30.0)),
              ),
            ]),
            // Text("test"),
            // ListView.builder(
            //     padding: const EdgeInsets.all(8),
            //     itemCount: text.length,
            //     itemBuilder: (BuildContext ctx, int index) {
            //       return text[index];
            //     })
          ],
        ),
      ),
    );
  }
}
