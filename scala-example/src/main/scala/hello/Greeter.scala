package sample.hello

import akka.actor.Actor

object Greeter {
  case object Greet
  case object Done
}

class Greeter extends Actor {
  def receive = {
    case Greeter.Greet =>
      println("Hello World!")
      //context.actorSelection("/user/helloworld") ! Greeter.Done
      sender() ! Greeter.Done
  }
}
