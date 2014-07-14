package sample.hello

import akka.actor.ActorSystem
import akka.actor.Props
import akka.actor.ActorRef
import akka.actor.Actor
import akka.actor.ActorLogging
import akka.actor.Terminated

object Main2 {

  def main(args: Array[String]): Unit = {
    val system = ActorSystem("Hello")
    val a = system.actorOf(Props[HelloWorld], "helloWorld")
    val b = system.actorOf(Props[HelloWorld])
    system.actorOf(Props(classOf[Terminator], a), "terminator")
    system.actorOf(Props(classOf[Terminator], b), "terminator1")
  }

  class Terminator(ref: ActorRef) extends Actor with ActorLogging {
    context watch ref
    def receive = {
      case Terminated(_) =>
        //log.info("{} has terminated, shutting down system", ref.path)
        println("Finished")
        context.system.shutdown()
    }
  }

}
