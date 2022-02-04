import 'package:flutter/material.dart';

class Ball extends StatelessWidget {
  const Ball({
    Key key,
    this.width = 10,
    this.left = 0,
    this.top = 0,
  }) : super(key: key);
  final double width;
  final double left;
  final double top;

  @override
  Widget build(BuildContext context) {
    return Positioned(
      left: MediaQuery.of(context).size.width* (left/100)-5,
      top:  MediaQuery.of(context).size.width*0.65 * (top/100)-5,
      child:Image.asset("assets/images/ball.png", width: width),
    );
  }
}
