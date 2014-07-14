package example.future

import scala.concurrent._
import ExecutionContext.Implicits.global
import scala.concurrent.duration._

object Main {
  def main(args: Array[String]) {
    val s = "Hello"
    val f: Future[String] = Future {
      s + " future!"
    }
    //f onSuccess {
    //  case msg => println(msg)
    //}
    println(Await.result(f, 6 millis))
    val tasks = for (i <- 1 to 10) yield Future {
      i * i
    }
    val results = tasks.map(Await.result(_, 6 millis))
    println(results)
  }
}
